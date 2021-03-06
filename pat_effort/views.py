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

    def vars_for_template(self):
        return {'points_example': 1000 * Constants.point_conversion}

class TrialPrep(Page):
    def is_displayed(self):
        return self.player.round_number == 1

    timeout_seconds = 5

class TrialPage(Page):
    def is_displayed(self):
        return self.player.round_number == 1

    timeout_seconds = Constants.trial_minutes*60

    form_model = models.Player
    form_fields = ['tasksCompleted_trial']

class TrialResults(Page):
    def is_displayed(self):
        return self.player.round_number == 1

class CommitDecisionPageFirst(Page):

    def is_displayed(self):
        return self.player.role() == 'commit_first'

    form_model = models.Player
    form_fields = ['commit_decision1', 'commit_decision2', 'commit_decision3', 'commit_decision4']

class PaternaleeDecisionPage(Page):
    form_model = models.Player
    form_fields = ['paternalee_decision1', 'paternalee_decision2', 'paternalee_decision3', 'paternalee_decision4']

class CommitDecisionPageSecond(Page):

    def is_displayed(self):
        return self.player.role() == 'paternalee_first'

    form_model = models.Player
    form_fields = ['commit_decision1', 'commit_decision2', 'commit_decision3', 'commit_decision4']

class PartnerBeliefPage(Page):
    form_model = models.Player
    form_fields = ['partner_belief']

class DecisionForPartner(Page):
    form_model = models.Player
    form_fields = ['decisionForPartner']


class DecisionWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.handleImplementation()


class ImplementationFeedback(Page):
    pass

class TaskPrep(Page):

    timeout_seconds = 5

class RealEffortPage(Page):

    timeout_seconds = Constants.worktime_minutes*60

    form_model = models.Player
    form_fields = ['tasksCompleted', 'surf_timing', 'productivity']


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.calculatePayoffs()

class Results(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def before_next_page(self):
        if self.round_number == Constants.num_rounds:
            self.group.compensatePayoffs()

class Happiness(Page):

    form_model = models.Player
    form_fields = ['button_present_happiness']

class TextFeedback(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    timeout_seconds = 180

    form_model = models.Player
    form_fields = ['textFeedback']


page_sequence = [
    WaitForArrival,
    WaitForStart,
    Instructions,
    TrialPrep,
    TrialPage,
    TrialResults,
    CommitDecisionPageFirst,
    PaternaleeDecisionPage,
    CommitDecisionPageSecond,
    PartnerBeliefPage,
    DecisionForPartner,
    DecisionWaitPage,
    ImplementationFeedback,
    TaskPrep,
    RealEffortPage,
    ResultsWaitPage,
    Results,
    Happiness,
    TextFeedback
]
