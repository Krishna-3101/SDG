from django.urls import path
from .views import submit_metadata, success_page, search_projects

urlpatterns = [
    path('', submit_metadata, name='submit_metadata'),
    path('success/', success_page, name='success'),
    path('', submit_metadata, name='submit_metadata'),
    path('success/', success_page, name='success'),
    path('search/', search_projects, name='search_projects'),
]