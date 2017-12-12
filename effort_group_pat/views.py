from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class WaitForArrival(WaitPage):
    wait_for_all_groups = True

class WaitForStart(Page):
    def is_displayed(self):
        return self.player.round_number == 1

class Instructions(Page):
    def is_displayed(self):
        return self.player.round_number == 1

    def vars_for_template(self):
        return {'dkk': Constants.points_per_task_number * Constants.point_conversion}

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
        return self.player.commit_choice_first

    form_model = models.Player
    form_fields = ['remove_option_own']

class MembershipChoice(Page):

    form_model = models.Player
    form_fields = ['leave_group_choice']

class CommitChoiceSecond(Page):
    def is_displayed(self):
        return self.player.commit_choice_first == False

    form_model = models.Player
    form_fields = ['remove_option_own']

class Vote(Page):

    def is_displayed(self):
        return self.player.placed_in_group == True and self.player.leave_group_choice == False

    form_model = models.Player
    form_fields = ['vote_to_remove']

class VoteWait(WaitPage):
    wait_for_all_groups = True

class GroupBelief(Page):
    form_model = models.Player
    form_fields = ['group_decision_belief']

    def before_next_page(self):
        self.subsession.determineVote()
        self.player.setOption()

class ImplementationFeedback(Page):
    pass

class Task(Page):

    timeout_seconds = Constants.worktime_minutes * 60

    form_model = models.Player
    form_fields = ['tasks_completed','play_choice1','play_choice2','play_choice3','play_choice4','play_choice5']

class Happiness(Page):

    form_model = models.Player
    form_fields = ['restrospective_preference']

    def before_next_page(self):
        self.player.setPayoff()

class TextFeedback(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    form_model = models.Player
    form_fields = ['text_feedback']

    timeout_seconds = 180

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
    # TrialPage,
    # CommitChoiceFirst,
    # MembershipChoice,
    # CommitChoiceSecond,
    # Vote,
    # VoteWait,
    # GroupBelief,
    # ImplementationFeedback,
    Task,
    Happiness,
    TextFeedback,
    ResultsWaitPage,
    Results
]
