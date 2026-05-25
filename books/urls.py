from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register_user),
    path('change-password/', change_password),

    path('books/', book_list),
    path('books/<int:pk>/', book_detail),

    path('books/<int:book_id>/reviews/', book_reviews),
    path('reviews/<int:pk>/', review_detail),
]