from django.urls import include, path
from .views import SingerCreate, SingerList, SingerDetail, SingerUpdate, SingerDelete
from .views import AlbumCreate, AlbumList, AlbumDetail, AlbumUpdate, AlbumDelete
from .views import MusicCreate, MusicList, MusicDetail, MusicUpdate, MusicDelete
from .views import RawSQLQueryView

urlpatterns = [
    # Singer URLs
    path('singers/create/', SingerCreate.as_view(), name='singer-create'),
    path('singers/', SingerList.as_view(), name='singer-list'),
    path('singers/<str:pk>/', SingerDetail.as_view(), name='singer-detail'),
    path('singers/<str:pk>/update/', SingerUpdate.as_view(), name='singer-update'),
    path('singers/<str:pk>/delete/', SingerDelete.as_view(), name='singer-delete'),

    # Album URLs
    path('albums/create/', AlbumCreate.as_view(), name='album-create'),
    path('albums/', AlbumList.as_view(), name='album-list'),
    path('albums/<str:pk>/', AlbumDetail.as_view(), name='album-detail'),
    path('albums/<str:pk>/update/', AlbumUpdate.as_view(), name='album-update'),
    path('albums/<str:pk>/delete/', AlbumDelete.as_view(), name='album-delete'),

    # Music URLs
    path('music/create/', MusicCreate.as_view(), name='music-create'),
    path('music/', MusicList.as_view(), name='music-list'),
    path('music/<str:pk>/', MusicDetail.as_view(), name='music-detail'),
    path('music/<str:pk>/update/', MusicUpdate.as_view(), name='music-update'),
    path('music/<str:pk>/delete/', MusicDelete.as_view(), name='music-delete'),

    # SQL URLs
    path('sql/raw_sql_query/', RawSQLQueryView.as_view(), name='raw-sql-query'),
]
