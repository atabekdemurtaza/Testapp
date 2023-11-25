from django.urls import path
from accounts.api.views import UserListView, UserDetailView

urlpatterns = [
    path(
        route='accounts/',
        view=UserListView.as_view(),
        name='accounts-list'),
    path(
        route='accounts/<int:pk>/',
        view=UserDetailView.as_view(),
        name='account-detail'),
    path(
        route='register/',
        view=UserListView.as_view(),
        name='user-register'
    ),
]
