from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "account"

urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    #path('login/', auth_views.LoginView.as_view(template_name='account/login2.html'), name='user_login'),
    path('register/', views.register, name='user_register'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'),name='user_logout'),
    # path('logout/', auth_views.LogoutView.as_view(), name='user_logout'),
    path('password-change/',
         auth_views.PasswordChangeView.as_view(
             template_name="account/password_change_form.html",
             success_url="/account/password-change-done"),
         name='password_change'
         ),
    path('password-change-done/',
         auth_views.PasswordChangeDoneView.as_view(
             template_name="account/password_change_done.html"),
         name='password_change_done'),
    path('my-information/', views.myself, name="my_information"),
    path('edit-my-information/', views.myself_edit, name="edit_my_information"),
    path('my-image', views.my_image, name="my_image"),
    path('my-test', views.mytest, name="my_test"),
]