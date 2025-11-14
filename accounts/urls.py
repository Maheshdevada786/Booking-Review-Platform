from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(next_page=reverse_lazy('myapp:home')), name='logout'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/delete/', views.delete_profile, name='delete_profile'),
]