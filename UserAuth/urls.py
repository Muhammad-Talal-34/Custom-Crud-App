from django.urls import path
from UserAuth import views
urlpatterns = [
path('', views.LandingPage,name=('landindpage')),
path('login/',views.LoginUser, name=('login')),
path('logout/',views.LogoutUser, name=('logout')),
path('dashboard/',views.Dashboard , name=('dashboard')),
path('register/',views.RegisterUser, name=('register')),
path('profile/',views.UserProfile, name=('profile')),
path('manageusers/', views.manage_users, name='manageusers'),
path('change-role/<int:user_id>/', views.change_role, name='change_role'),
path('delete-user/<int:user_id>/', views.delete_user, name='delete_user'),
]