from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from datetime import date
from django.db.models import Count, Q

@login_required
def dashboard(request):
    user = request.user
    tasks = Task.objects.filter(owner=user)
    total = tasks.count()
    completed = tasks.filter(completed=True).count()
    pending = tasks.filter(completed=False).count()
    overdue = tasks.filter(due_date__lt=date.today(), completed=False).count()
    
    context = {
        'total': total,
        'completed': completed,
        'pending': pending,
        'overdue': overdue,
    }
    return render(request, 'tasks/dashboard.html', context)


@login_required
def task_list(request):
    user = request.user
    tasks = Task.objects.filter(owner=user)
    q = request.GET.get('q', '').strip()
    status = request.GET.get('status', 'all')
    priority = request.GET.get('priority', '')

    if q:
        tasks = tasks.filter(Q(title__icontains=q) | Q(description__icontains=q))
    if status == 'pending':
        tasks = tasks.filter(completed=False)
    elif status == 'completed':
        tasks = tasks.filter(completed=True)
    if priority in ('L', 'M', 'H'):
        tasks = tasks.filter(priority=priority)

    tasks = tasks.distinct()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)  # create task but not save yet
            task.owner = request.user       # link task to logged-in user
            task.save()                     # now save
            return redirect('tasks:task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form, 'create': True})


@login_required
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks:task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form, 'create': False})


@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk, owner=request.user)
    return render(request, 'tasks/task_detail.html', {'task': task})


@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, owner=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks:task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})


@login_required
def toggle_complete(request, pk):
    task = get_object_or_404(Task, pk=pk, owner=request.user)
    task.completed = not task.completed
    task.save()
    return redirect(request.META.get('HTTP_REFERER', '/'))