from django.urls import path
from posts.views import *

urlpatterns = [
    path('', view_posts),
    path('create', view_create_post),
    path('create/save', create_post),
    path('update/<int:id>', view_update_post),
    path('update/save/<int:id>', update_post),
    path('delete/<int:id>', delete_post),
    path('search', search_post),
]
