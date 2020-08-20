from .models import Album, Image
from rest_framework import serializers


class AlbumSerializer(serializers.ModelSerializer):
    images = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='image-detail'
    )

    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'images']


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ['url', 'id', 'order', 'title', 'album']
