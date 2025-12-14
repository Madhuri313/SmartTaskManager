// Small script for keyboard quick actions
document.addEventListener('DOMContentLoaded', function(){
  document.addEventListener('keydown', function(e){
    if(e.key === 'n' && e.ctrlKey){ // Ctrl+N to create new task
      var link = document.querySelector('a[href$="/tasks/new/"]');
      if(link) window.location = link.href;
    }
  });
});
