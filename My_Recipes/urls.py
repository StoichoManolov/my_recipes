from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('My_Recipes.common.urls')),
    path('account/', include('My_Recipes.accounts.urls')),
    path('article/', include('My_Recipes.articles.urls')),
    path('recipe/', include('My_Recipes.recipes.urls')),
    path('ingredients/', include('My_Recipes.recipe_ingredients.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
