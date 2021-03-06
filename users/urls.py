from django.urls import path
from users import views as user_view
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'users'

urlpatterns = [
    path('register/', user_view.register, name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('activate/<uidb64>/<token>', user_view.ActivateAccountView.as_view(), name='activate')
]