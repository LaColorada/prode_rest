from django.contrib import admin

from prode.models import Match, Forecast, Team, Player

# Register your models here.

admin.site.register(Match)
admin.site.register(Forecast)
admin.site.register(Team)
admin.site.register(Player)