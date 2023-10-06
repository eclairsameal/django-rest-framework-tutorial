from rest_framework import serializers
from .models import Singer, Album, Music


class SingerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Singer
        # fields = '__all__'
        fields = ('name', 'debut_year')


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        # fields = '__all__'
        fields = ('name', 'singer', 'release_date')


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        # fields = '__all__'
        fields = ('id', 'song', 'singer', 'album', 'album_no', 'song_length')
