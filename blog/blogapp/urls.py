from django.contrib import admin
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
from django.conf import settings
from django.conf.urls.static import static
# import blogapp.views

urlpatterns = [
    path('<int:blog_id>/', views.detail, name="detail"),
    path('new/', views.new, name="new"),
    path('create', views.create, name="create"),
    path('update/<int:pk>', views.update, name="update"),
    path('delete/<int:pk>', views.delete, name="delete"),
    path('newblog/', views.blogpost, name="newblog"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)