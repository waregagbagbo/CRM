from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),
    path('profile/', views.profile, name="profile"),
    path('products/', views.products, name='products'),
    path('customer/<str:pk_test>/', views.customer, name="customer"),

    path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),

    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="passwords/reset_password.html"), name='password_reset'),

    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="passwords/password_confirm.html"), name='password_confirm'),

    path('accounts/password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name="passwords/password_reset_done.html"),name ='reset_password_done'),
    
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name="passwords/recent_complete.html"),name='reset_complete'),
    
]

