from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('learn_app.urls')),
    path('accounts/', include('allauth.urls')),
    path('social-auth/', include('social_django.urls')),
]
