from django.urls import path
# from .views import movie_list, movie_details
from .views import WatchListAV, WatchDetailAV, StreamPlatformAV


urlpatterns = [
    # path('list/', movie_list, name='movie-list'),
    # path('<int:pk>', movie_details, name='movie_details'),
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>', WatchDetailAV.as_view(), name='movie_details'),
    path('stream/', StreamPlatformAV.as_view(), name='stream')
]