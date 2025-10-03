from django.urls import path
from .views import register_user, get_user_info

urlpatterns = [
    path('register/', register_user),              # POST
    path('user/<int:user_id>/', get_user_info),   # GET
]
