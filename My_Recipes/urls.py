from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static

from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('My_Recipes.common.urls')),
    path('account/', include('My_Recipes.accounts.urls')),
    path('article/', include('My_Recipes.articles.urls')),
    path('recipe/', include('My_Recipes.recipes.urls')),
    path('ingredients/', include('My_Recipes.recipe_ingredients.urls')),
    path('comment/', include('My_Recipes.comments.urls')),
    path('review/', include('My_Recipes.reviews.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if not settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),
    ]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
