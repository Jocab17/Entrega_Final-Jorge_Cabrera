from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_details'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
]
