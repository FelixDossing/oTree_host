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
    num_rounds = 3

    points_per_task = c(100)
    points_per_task_number = 100
    point_conversion = 0.2

    worktime_minutes = 15
    trial_minutes = 2
    temptation_interval_minutes = 3



class Subsession(BaseSubsession):

    group_voted_remove = models.BooleanField()
    voted_for = models.IntegerField()
    voted_against = models.IntegerField()

    def creating_session(self):


        ## Determine whether player is placed in group
        for p in self.get_players():
            p.placed_in_group = random.choice([True,False])
            p.commit_choice_first = random.choice([True,False])


    def determineVote(self):
        self.voted_for = 0
        self.voted_against = 0

        for p in self.get_players():
            print(p)
            if p.placed_in_group == True and p.leave_group_choice == False:
                if p.vote_to_remove == True:
                    self.voted_for = self.voted_for + 1
                else:
                    self.voted_against = self.voted_against + 1
        if self.voted_for > self.voted_against:
            self.group_voted_remove = True
        elif self.voted_for < self.voted_against:
            self.group_voted_remove = False
        elif self.voted_for == self.voted_against:
            self.group_voted_remove = random.choice([True,False])


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    def setOption(self):
        if self.placed_in_group == False:
            if self.remove_option_own == True:
                self.option_available = False
            else:
                self.option_available = True
        elif self.placed_in_group == True:
            if self.leave_group_choice == True:
                self.option_available = True
            elif self.subsession.group_voted_remove == True:
                self.option_available = False
            elif self.subsession.group_voted_remove == False:
                self.option_available = True

    def setPayoffs(self):
        self.payoff = c(int(self.tasks_completed)*Constants.points_per_task)

    placed_in_group = models.BooleanField()
    option_available = models.BooleanField(initial=True)

    leave_group_choice = models.BooleanField()
    remove_option_own = models.BooleanField()
    vote_to_remove = models.BooleanField()
    commit_choice_first = models.BooleanField()

    tasks_completed = models.CharField()
    play_choice1 = models.CharField()
    play_choice2 = models.CharField()
    play_choice3 = models.CharField()
    play_choice4 = models.CharField()
    play_choice5 = models.CharField()
    play_choice6 = models.CharField()
    group_decision_belief = models.IntegerField(
        choices=[0,10,20,30,40,50,60,70,80,90,100],
        widget=widgets.RadioSelectHorizontal
    )
    text_feedback = models.TextField()
    restrospective_preference = models.BooleanField()
