from django.urls import path

from My_Recipes.common.views import Homepage

urlpatterns = [
    path('', Homepage.as_view(), name='home'),
]