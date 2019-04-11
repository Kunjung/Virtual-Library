from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book/<int:book_id>', views.book, name='book'),
    path('person/<int:person_id>', views.person, name='person'),
    path('wishlist/<int:person_id>', views.wishlist, name='wishlist')
]
