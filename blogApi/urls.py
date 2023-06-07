from django.urls import path
from .views import PostView, DetailArticleView, createPostView, updatePostView, delPostView, CategoryView, likeDislikeView, authorProfileView, editAuthorProfileView, createAuthorProfileView, addParentCommentView, addChildComment, deleteCommentView
urlpatterns = [
    path('<int:pk>/', DetailArticleView.as_view(), name='article-detail'),
    path('', PostView.as_view(), name='myview'),
    path('createPost/', createPostView, name='create-post'),
    path('updatePost/<int:pk>/', updatePostView, name='update-post'),
    path('delete/<int:pk>', delPostView, name='delete-post'),
    path('add-category/', CategoryView.createCategoryView, name = 'add-category'),
    path('category/<str:pk>', CategoryView.allCategoryView, name = 'get-category'),
    path('like-dislike/<int:pk>', likeDislikeView, name='hit-the-like-dislike'),
    path('profile/<int:pk>', authorProfileView, name='author_profile'),
    path('edit-profile/<int:pk>', editAuthorProfileView, name='edit_author_profile'),
    path('create_profile/', createAuthorProfileView, name='create_author_profile'),
    path('article/<int:pk>/add_parent_comment', addParentCommentView, name='add-parent-comment'),
    path('delete-comment/<int:pk>', deleteCommentView, name='delete-comment'),
    path('article/<int:pk>/add_child_comment', addChildComment, name='add-child-comment'),
    ]