from django.shortcuts import render
from rest_framework import generics
from .models import Singer, Album, Music
from .serializers import SingerSerializer, AlbumSerializer, MusicSerializer
from django.db import connection
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

# Singer Views
class SingerCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new Singer
    queryset = Singer.objects.all(),
    serializer_class = SingerSerializer


class SingerList(generics.ListAPIView):
    #  API endpoint that allows Singer to be viewed.
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer


class SingerDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single Singer by name.
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer


class SingerUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a Singer record to be updated.
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer


class SingerDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a Singer record to be deleted.
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer

# Album Views


class AlbumCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new Album
    queryset = Album.objects.all(),
    serializer_class = AlbumSerializer


class AlbumList(generics.ListAPIView):
    #  API endpoint that allows Album to be viewed.
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class AlbumDetail(generics.RetrieveAPIView):
    # API endpoint that returns an Album by name.
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class AlbumUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows an Album record to be updated.
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class AlbumDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows an Album record to be deleted.
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

# Music Views


class MusicCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new Music
    queryset = Music.objects.all(),
    serializer_class = MusicSerializer


class MusicList(generics.ListAPIView):
    #  API endpoint that allows Music to be viewed.
    queryset = Music.objects.all()
    serializer_class = MusicSerializer


class MusicDetail(generics.RetrieveAPIView):
    # API endpoint that returns a Music by name.
    queryset = Music.objects.all()
    serializer_class = MusicSerializer


class MusicUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a Music record to be updated.
    queryset = Music.objects.all()
    serializer_class = MusicSerializer


class MusicDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a Music record to be deleted.
    queryset = Music.objects.all()
    serializer_class = MusicSerializer


# SQL
class RawSQLQueryView(APIView):
    def get(self, request, format=None):
        with connection.cursor() as cursor:
            # Write your SQL query
            sql_query = "SELECT name, release_date FROM public.db_crud_album;"

            # Execute SQL query
            cursor.execute(sql_query)

            # Get query results
            result = cursor.fetchall()

            # 返回结果
            return Response(result, status=status.HTTP_200_OK)