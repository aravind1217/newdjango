from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   
    path('',views.get_articles,name='articles'),
    path('new', views.article_form,name='article_insert'), 
    path('<int:id>/', views.article_form,name='article_update'),
    path('delete/<int:id>/',views.article_delete,name='article_delete'),
    path('register', views.register_user,name='register'),
     path('login', auth_views.LoginView.as_view(template_name='Login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='Logout.html'), name='logout'),

]
