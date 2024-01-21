from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name="blog-home"),
    path('user/<str:username>', UserPostListView.as_view(), name="user-posts"),
    path('post/<int:pk>', PostDetailView.as_view(), name="post-detail"),
    path('post/new', PostCreateView.as_view(), name="post-create"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),
    path("about/", views.about, name="blog-about")
]

# <pk> means primary key
# path('post/<int:pk>', PostDetailView.as_view(), name="post-detail") specifying pk variable in the url that allows us
# to grab that value from the url use it in our view function and this case we're using a class-based view so that will
# be passed to the class-based view
