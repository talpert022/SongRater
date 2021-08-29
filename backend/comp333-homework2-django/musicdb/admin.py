from django.contrib import admin

from .models import Users, Songs, Years, Ratings

admin.site.register(Users)
admin.site.register(Songs)
admin.site.register(Ratings)
admin.site.register(Years)