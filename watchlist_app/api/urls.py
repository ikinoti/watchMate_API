from django.urls import path
# from .views import movie_list, movie_details
from .views import MovieListAV, MovieDetailAV


urlpatterns = [
    # path('list/', movie_list, name='movie-list'),
    # path('<int:pk>', movie_details, name='movie_details'),
    path('list/', MovieListAV.as_view(), name='movie-list'),
    path('<int:pk>', MovieDetailAV.as_view(), name='movie_details')
]