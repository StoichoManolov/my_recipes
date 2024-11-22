from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from My_Recipes.accounts.views import CreateAccountView, DetailAccountView, EditAccountView, DeleteAccountView

urlpatterns = [
    path('create/', CreateAccountView.as_view(), name='create-account'),
    path('login/', LoginView.as_view(), name='login-account'),
    path('logout/', LogoutView.as_view(), name='logout-account'),
    path('<int:pk>/', include([
        path('detail/', DetailAccountView.as_view(), name='detail-account'),
        path('edit/', EditAccountView.as_view(), name='edit-account'),
        path('delete/', DeleteAccountView.as_view(), name='delete-account'),
    ])),
]