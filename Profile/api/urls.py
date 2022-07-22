from django.urls import path
from .views import signin,logoutview,editProfile,registerview,viewProfile,getUsers
urlpatterns =[
    path('',signin,name="signin"),
    path('register/',registerview,name="register"),
    path('users/',getUsers,name="users"),
    path('logout/',logoutview,name="logout"),
    path('profile/',viewProfile,name="view-profile"),
    path('profile/edit/',editProfile,name="edit-profile"),
]