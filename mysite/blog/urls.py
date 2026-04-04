from django.urls import path

from blog import views
from blog.views.post_view import PostView

urlpatterns = [
    path('', views.PostView.as_view(), name='home'),
]