from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        if self.player.id_in_group == 1:
            yield (views.Test, {'submitted_answer1':'1/2', 'submitted_answer2':'1/6', 'submitted_answer3':'20%', 'submitted_answer4':'3/13'})
        else:
            yield (views.Test, {'submitted_answer1':'1/2', 'submitted_answer2':'1/6', 'submitted_answer3':'20%', 'submitted_answer4':'12/52'})
