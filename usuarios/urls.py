from django.urls import path
from usuarios.views import *

urlpatterns = [
    path('users/', get_users, name="get_users"),
    path('user/<int:pk>/', get_user_id, name="get_user_id"),
    path('user-create/', create_user, name="create_user"),
]