from django.contrib import admin
from django.urls import include, path
from musicdb.views import user_create, UserView, SongView, YearView, RatingView
from rest_framework import routers 

router = routers.DefaultRouter()
router.register(r'users', UserView, 'users')
router.register(r'songs', SongView, 'songs')
router.register(r'ratings', RatingView, 'ratings')
router.register(r'years', YearView, 'years')

urlpatterns = [
    path('musicdb/', include('musicdb.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
