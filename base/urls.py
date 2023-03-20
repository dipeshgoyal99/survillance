from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="home"),
    path('room/', views.room),
    path('get_token/', views.getToken),

    path('create_member/', views.createMember),
    path('get_member/', views.getMember),
    path('delete_member/', views.deleteMember),
    path('dashboard',views.dashboard),
    path('register', views.register, name="register"),
    path('complaint', views.lobby,name="complaint"),
 
]