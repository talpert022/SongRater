from django.urls import path, include
from . import views
from musicdb.views import index, user_create, retrieve_years, UserView, retrieve_ratings


urlpatterns = [
    path('', index, name='index'),
    path('register/', user_create, name='user_create'),
    path('retrieve/', retrieve_ratings, name='retrieve_ratings'),
    path('retrieve-by-year/', retrieve_years, name='retrieve_years')
]