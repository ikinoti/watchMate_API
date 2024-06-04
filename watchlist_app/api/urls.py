from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import movie_list, movie_details
from .views import (WatchListAV, WatchDetailAV,
                    StreamPlatformAV,StreamPlatformDetailAV, StreamPlatformVS, ReviewList,
                    ReviewDetail, ReviewCreate, UserReview)

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')


urlpatterns = [
    # path('list/', movie_list, name='movie-list'),
    # path('<int:pk>', movie_details, name='movie_details'),
    path('list/', WatchListAV.as_view(), name='movie_list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie_details'),

    path('', include(router.urls)),

    # path('stream/', StreamPlatformAV.as_view(), name='stream'),
    # path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='stream_detail'),
    
    # path('review/', ReviewList.as_view(), name='review_list'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name='review_detail'),

    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review_create'),
    path('<int:pk>/reviews/', ReviewList.as_view(), name='review_list'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review_detail'),

    path('reviews/', UserReview.as_view(), name='user-review-detail')
]