from django.conf.urls import url
from django.urls import include

from games.views import AttackView
from games.views import CreateGameView
from games.views import GameView

urlpatterns = [
    url(r'^(?P<game_id>.+)/attack/$', AttackView.as_view(), name='attack'),
#    url(r'^(?P<game_id>.+)/attack/$', include(AttackView.post()), name='attack'),
    url(r'^create_game/$', CreateGameView.as_view(), name='create_game'),
    url(r'^(?P<game_id>.+)/$', GameView.as_view(), name='game'),
]
