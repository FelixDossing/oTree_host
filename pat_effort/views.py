from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


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

    timeout_seconds = 5

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
        return self.player.id_in_group == 2

    form_model = models.Player
    form_fields = ['commit_decision1', 'commit_decision2', 'commit_decision3', 'commit_decision4']


class DecisionForPartner(Page):
    form_model = models.Player
    form_fields = ['decisionForPartner']

class PartnerBeliefPage(Page):
    form_model = models.Player
    form_fields = ['partner_belief']

class DecisionWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.handleImplementation()

class ImplementationFeedback(Page):
    pass

class TaskPrep(Page):

    timeout_seconds = 5

class RealEffortPage(Page):

    timeout_seconds = 5

    form_model = models.Player
    form_fields = ['tasksCompleted']


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.calculatePayoffs()

class Results(Page):
    pass


page_sequence = [
    Instructions,
    TrialPrep,
    TrialPage,
    TrialResults,
    CommitDecisionPageFirst,
    PaternaleeDecisionPage,
    CommitDecisionPageSecond,
    DecisionForPartner,
    DecisionWaitPage,
    PartnerBeliefPage,
    ImplementationFeedback,
    TaskPrep,
    RealEffortPage,
    ResultsWaitPage,
    Results
]
