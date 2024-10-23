from django.urls import path
from .views import UserListCreateView, UserMeView, UserBanView, UserUnBanView, UserToAdminView, AdminToUserView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='users-list-create'),
    path('/me', UserMeView.as_view(), name='users-me'),
    path('/<int:pk>/ban', UserBanView.as_view(), name='users-ban'),
    path('/<int:pk>/unban', UserUnBanView.as_view(), name='users-unban'),
    path('/<int:pk>/to_admin', UserToAdminView.as_view(), name='user-to-admin'),
    path('/<int:pk>/to_user', AdminToUserView.as_view(), name='admin-to-user'),
]