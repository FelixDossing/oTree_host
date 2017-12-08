from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class WaitForArrival(WaitPage):
    wait_for_all_groups = True

class WaitForStart(Page):
    pass

class Instructions(Page):
    def is_displayed(self):
        return self.player.round_number == 1

class TrialPrep(Page):
    def is_displayed(self):
        return self.player.round_number == 1

    timeout_seconds = 5

class TrialPage(Page):
    def is_displayed(self):
        return self.player.round_number == 1

    timeout_seconds = Constants.trial_minutes*60

class CommitChoiceFirst(Page):
    def is_displayed(self):
        return commit_choice_first

    form_model = models.Player
    form_fields = ['remove_option_own']

class MemberShipChoice(Page):

    form_model = models.Player
    form_fields = ['leave_group_choice']

class CommitChoiceSecond(Page):
    def is_displayed(self):
        return commit_choice_first == False

    form_model = models.Player
    form_fields = ['remove_option_own']

class Vote(Page):
    form_model = models.Player
    form_fields = ['vote_to_remove']

class GroupBelief(Page):
    form_model = models.Player
    form_fields = ['group_decision_belief']

class TaskPrep(Page):

    timeout_seconds = 5

class Task(Page):

    # timeout_seconds = Constants.worktime_minutes * 60

    form_model = models.Player
    form_fields = ['tasks_completed','play_choice1','play_choice2','play_choice3','play_choice4','play_choice5','play_choice6']

class Happiness(Page):

    form_model = models.Player
    form_fields = ['restrospective_preference']

class TextFeedback(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    form_model = models.Player
    form_fields = ['text_feedback']

class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds


page_sequence = [
    # WaitForArrival,
    # WaitForStart,
    # Instructions,
    # TrialPrep,
    # TrialPage,
    # CommitChoiceFirst,
    # MembershipChoice,
    # CommitChoiceSecond,
    # Vote,
    # GroupBelief,
    # TaskPrep,
    Task,
    Happiness,
    TextFeedback,
    ResultsWaitPage,
    Results
]
