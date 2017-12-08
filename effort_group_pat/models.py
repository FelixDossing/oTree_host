from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'effort_group_pat'
    players_per_group = None
    num_rounds = 2

    points_per_slider = 20
    point_conversion = 0.2

    worktime_minutes = 30
    trial_minutes = 3
    temptation_interval_minutes = 2



class Subsession(BaseSubsession):

    def creating_session(self):

        ## Determine whether player is placed in group
        for p in self.get_players():
            p.placed_in_group = random.choice([True,False])
            p.group_choice_first = random.choice([True,False])


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    placed_in_group = models.BooleanField()
    option_available = models.BooleanField()

    leave_group_choice = models.BooleanField()
    remove_option_own = models.BooleanField()
    vote_to_remove = models.BooleanField()
    commit_choice_first = models.BooleanField()

    tasks_completed = models.IntegerField()
    play_choice1 = models.BooleanField(initial=False)
    play_choice2 = models.BooleanField(initial=False)
    play_choice3 = models.BooleanField(initial=False)
    play_choice4 = models.BooleanField(initial=False)
    play_choice5 = models.BooleanField(initial=False)
    play_choice6 = models.BooleanField(initial=False)
    group_decision_belief = models.IntegerField()

    text_feedback = models.TextField()
    restrospective_preference = models.BooleanField()
