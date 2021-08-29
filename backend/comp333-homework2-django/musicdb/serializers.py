from rest_framework import serializers
from .models import Users, Songs, Years, Ratings

# The serializer translates an object into a format that
# can be stored in our database. We use one for each model.
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = Users
    fields = ('username', 'password')

class SongSerializer(serializers.ModelSerializer):
  class Meta:
    model = Songs
    fields = ('song', 'artist')

class RatingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Ratings
    fields = ('username', 'song', 'rating')

class YearSerializer(serializers.ModelSerializer):
  class Meta:
    model = Years
    fields = ('year', 'song', 'president')