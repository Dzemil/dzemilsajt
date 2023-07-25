from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    path('add_post/', views.PostNew.as_view(), name='add_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('update_post/<slug:slug>/', views.PostUpdate.as_view(), name='update_post'),  
    path('delete_post/<slug:slug>/', views.PostDelete.as_view(), name='delete_post'),  
]