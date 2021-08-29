from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from musicdb.forms import UserForm, RetrieveByYearForm
from musicdb.models import Users, Years, Songs, Ratings
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from musicdb.serializers import UserSerializer, SongSerializer, YearSerializer, RatingSerializer


class UserView (viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = Users.objects.all()

class SongView(viewsets.ModelViewSet):
    serializer_class = SongSerializer
    queryset = Songs.objects.all()

    @action(detail=True)
    def songs_by_artist(self, request, pk=None):
      artist_songs = Songs.objects.filter(artist=pk)
      page = self.paginate_queryset(artist_songs)

      if page is not None:
          serializer = self.get_serializer(page, many=True)
          return self.get_paginated_response(serializer.data)

      serializer = self.get_serializer(artist_songs, many=True)
      return Response(serializer.data)

    @action(detail=True)
    def songs_by_title(self, request, pk=None):
      title_songs = Songs.objects.filter(song=pk)
      page = self.paginate_queryset(title_songs)

      if page is not None:
          serializer = self.get_serializer(page, many=True)
          return self.get_paginated_response(serializer.data)

      serializer = self.get_serializer(title_songs, many=True)
      return Response(serializer.data)

class RatingView (viewsets.ModelViewSet):
    serializer_class = RatingSerializer
    queryset = Ratings.objects.all()

class YearView (viewsets.ModelViewSet):
    serializer_class = YearSerializer
    queryset = Years.objects.all()


def index(request):
    return render(request, 'index.html')


def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_create')
    else:
        form = UserForm()
    return render(request, 'user_create.html', {'form': form})


def retrieve_ratings(request):
    form = RetrieveRatingsForm(request.GET or None)
    ratings = None
    if request.method == 'GET':
        if form.is_valid():
            # return HttpResponse("POST SUCCESSFUL")
            ratings = Ratings.objects.filter(
                username=form.cleaned_data.get('username'))

    return render(request, 'retrieve_ratings.html', {'form': form, 'ratings': ratings})


def retrieve_years(request):
    form = RetrieveByYearForm(request.GET or None)
    year = None
    if request.method == 'GET':
        if form.is_valid():
            year = Years.objects.filter(year=form.cleaned_data.get('year'))

    return render(request, 'retrieve_years.html', {'form': form, 'year': year})
