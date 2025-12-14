from django.urls import path
from .views import signup, custom_login, custom_logout
from django.contrib.auth import views as auth_views

app_name = 'accounts'
urlpatterns = [
    path('signup/', signup, name='signup'),
   # path('login/', CustomLoginView.as_view(), name='login'),
   # path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('login/', custom_login, name='login'),
    path('logout/', custom_logout, name='logout'),
]
