from django.urls import path
from assignment_app import views


urlpatterns = [
    path('home/', views.home,name='homepage'),
    path('latest-post/', views.latest_post,name='postpage'),
]

