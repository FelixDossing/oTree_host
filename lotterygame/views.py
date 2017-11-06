from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
from otree.api import safe_json


class Instructions(Page):
    form_model = models.Player
    form_fields = ['lev_instr','control1','control2','control3','control4','control5',
                   'control6','control7','control8','control9','control10','control11',
                   'control12']

    def control1_error_message(self, value):
        if not (value == 10):
            return 'This is not correct'

    def control2_error_message(self, value):
        if not (value == 7):
            return 'This is not correct'

    def control3_error_message(self, value):
        if not (value == 7):
            return 'This is not correct'

    def control4_error_message(self, value):
        if not (value == 0):
            return 'This is not correct'

    def control5_error_message(self, value):
        if not (value == 10):
            return 'This is not correct'

    def control6_error_message(self, value):
        if not (value == 0):
            return 'This is not correct'

    def control7_error_message(self, value):
        if not (value == 10):
            return 'This is not correct'

    def control8_error_message(self, value):
        if not (value == 14):
            return 'This is not correct'

    def control9_error_message(self, value):
        if not (value == 5):
            return 'This is not correct'

    def control10_error_message(self, value):
        if not (value == True):
            return 'This is not correct'

    def control11_error_message(self, value):
        if not (value == False):
            return 'This is not correct'

    def control12_error_message(self, value):
        if not (value == False):
            return 'This is not correct'


class Test(Page):
    timeout_seconds = 1800 # 30 min
    form_model = models.Player
    form_fields = ['submitted_answer{}'.format(i) for i in range (1,21)]

    def submitted_answer1_choices(self):
        qd1 = self.session.vars['questions'][0]
        return [
            qd1['choice1'],
            qd1['choice2'],
            qd1['choice3'],
            qd1['choice4'],
            qd1['choice5'],
        ]
    def submitted_answer2_choices(self):
        qd2 = self.session.vars['questions'][1]
        return [
            qd2['choice1'],
            qd2['choice2'],
            qd2['choice3'],
            qd2['choice4'],
            qd2['choice5'],
        ]
    def submitted_answer3_choices(self):
        qd2 = self.session.vars['questions'][2]
        return [
            qd2['choice1'],
            qd2['choice2'],
            qd2['choice3'],
            qd2['choice4'],
            qd2['choice5'],
        ]

    def submitted_answer4_choices(self):
        qd2 = self.session.vars['questions'][3]
        return [
            qd2['choice1'],
            qd2['choice2'],
            qd2['choice3'],
            qd2['choice4'],
            qd2['choice5'],
        ]

    def submitted_answer5_choices(self):
        qd1 = self.session.vars['questions'][4]
        return [
            qd1['choice1'],
            qd1['choice2'],
            qd1['choice3'],
            qd1['choice4'],
            qd1['choice5'],
        ]
    def submitted_answer6_choices(self):
        qd2 = self.session.vars['questions'][5]
        return [
            qd2['choice1'],
            qd2['choice2'],
            qd2['choice3'],
            qd2['choice4'],
            qd2['choice5'],
        ]

    def submitted_answer7_choices(self):
        qd2 = self.session.vars['questions'][6]
        return [
            qd2['choice1'],
            qd2['choice2'],
            qd2['choice3'],
            qd2['choice4'],
            qd2['choice5'],
        ]

    def submitted_answer8_choices(self):
        qd2 = self.session.vars['questions'][7]
        return [
            qd2['choice1'],
            qd2['choice2'],
            qd2['choice3'],
            qd2['choice4'],
            qd2['choice5'],
        ]

    def submitted_answer9_choices(self):
        qd1 = self.session.vars['questions'][8]
        return [
            qd1['choice1'],
            qd1['choice2'],
            qd1['choice3'],
            qd1['choice4'],
            qd1['choice5'],
        ]
    def submitted_answer10_choices(self):
        qd2 = self.session.vars['questions'][9]
        return [
            qd2['choice1'],
            qd2['choice2'],
            qd2['choice3'],
            qd2['choice4'],
            qd2['choice5'],
        ]

    def submitted_answer11_choices(self):
        qd2 = self.session.vars['questions'][10]
        return [
            qd2['choice1'],
            qd2['choice2'],
            qd2['choice3'],
            qd2['choice4'],
            qd2['choice5'],
        ]

    def submitted_answer12_choices(self):
        qd2 = self.session.vars['questions'][11]
        return [
            qd2['choice1'],
            qd2['choice2'],
            qd2['choice3'],
            qd2['choice4'],
            qd2['choice5'],
        ]
    def submitted_answer13_choices(self):
        qd1 = self.session.vars['questions'][12]
        return [
            qd1['choice1'],
            qd1['choice2'],
            qd1['choice3'],
            qd1['choice4'],
            qd1['choice5'],
        ]
    def submitted_answer14_choices(self):
        qd2 = self.session.vars['questions'][13]
        return [
            qd2['choice1'],
            qd2['choice2'],
            qd2['choice3'],
            qd2['choice4'],
            qd2['choice5'],
        ]

    def submitted_answer15_choices(self):
        qd2 = self.session.vars['questions'][14]
        return [
            qd2['choice1'],
            qd2['choice2'],
            qd2['choice3'],
            qd2['choice4'],
            qd2['choice5'],
        ]

    def submitted_answer16_choices(self):
        qd2 = self.session.vars['questions'][15]
        return [
            qd2['choice1'],
            qd2['choice2'],
            qd2['choice3'],
            qd2['choice4'],
            qd2['choice5'],
        ]
    def submitted_answer17_choices(self):
        qd1 = self.session.vars['questions'][16]
        return [
            qd1['choice1'],
            qd1['choice2'],
            qd1['choice3'],
            qd1['choice4'],
            qd1['choice5'],
        ]
    def submitted_answer18_choices(self):
        qd2 = self.session.vars['questions'][17]
        return [
            qd2['choice1'],
            qd2['choice2'],
            qd2['choice3'],
            qd2['choice4'],
            qd2['choice5'],
        ]

    def submitted_answer19_choices(self):
        qd2 = self.session.vars['questions'][18]
        return [
            qd2['choice1'],
            qd2['choice2'],
            qd2['choice3'],
            qd2['choice4'],
            qd2['choice5'],
        ]

    def submitted_answer20_choices(self):
        qd2 = self.session.vars['questions'][19]
        return [
            qd2['choice1'],
            qd2['choice2'],
            qd2['choice3'],
            qd2['choice4'],
            qd2['choice5'],
        ]


    def before_next_page(self):
        # self.player.set_test_values()
        self.player.check_correct()

class TestWaitPage(WaitPage):
    wait_for_all_groups = True
    def after_all_players_arrive(self):
        self.subsession.calc_stats()
        self.subsession.get_player_scores()

class TestGuessPage(Page):
    form_model = models.Player
    form_fields = ['score_guess']

    def vars_for_template(self):
        return {
            "player_scores": safe_json(self.session.vars['player_scores'])
            }

    def before_next_page(self):
        self.player.get_partner_score()

class SelfFeedback(Page):

    def is_displayed(self):
        return self.group.treatment == "self"

    form_model = models.Player
    form_fields = ['feedback_control_own_score', 'feedback_control_expected_partner']

    def vars_for_template(self):
        return {
            "player_scores": safe_json(self.session.vars['player_scores']),
            "player_rank": safe_json(self.player.rank)
            }

    def feedback_control_own_score_error_message(self, value):
        if self.player.test_score > self.subsession.average_score:
            if not (value == True):
                return 'This is not correct'
        else:
            if not (value == False):
                return 'This is not correct'

    def feedback_control_expected_partner_error_message(self, value):
        if self.player.test_score > self.subsession.average_score:
            if not (value == False):
                return 'This is not correct'
        else:
            if not (value == True):
                return 'This is not correct'

class PartnerFeedback(Page):

    def is_displayed(self):
        return self.group.treatment == "partner"

    form_model = models.Player
    form_fields = ['feedback_control_partner_score']

    def vars_for_template(self):
        return {
            "player_scores": safe_json(self.session.vars['player_scores']),
            "player_rank": safe_json(self.player.rank)
            }

    def feedback_control_partner_score(self, value):
        if self.player.partner_test_score > self.subsession.average_score:
            if not (value == True):
                return 'This is not correct'
        else:
            if not (value == False):
                return 'This is not correct'


class FullFeedback(Page):

    def is_displayed(self):
        return self.group.treatment == "full"

    form_model = models.Player
    form_fields = ['feedback_control_own_score', 'feedback_control_partner_score', 'feedback_control_compare']

    def vars_for_template(self):
        return {
            "player_scores": safe_json(self.session.vars['player_scores']),
            "player_rank": safe_json(self.player.rank)
            }

    def feedback_control_own_score_error_message(self, value):
        if self.player.test_score > self.subsession.average_score:
            if not (value == True):
                return 'This is not correct'
        else:
            if not (value == False):
                return 'This is not correct'

    def feedback_control_partner_score(self, value):
        if self.player.partner_test_score > self.subsession.average_score:
            if not (value == True):
                return 'This is not correct'
        else:
            if not (value == False):
                return 'This is not correct'

    def feedback_control_compare_error_message(self, value):
        if self.player.test_score > self.player.partner_test_score:
            if not (value == True):
                return 'This is not correct'
        else:
            if not (value == False):
                return 'This is not correct'



class LeviathanChoice(Page):

    def is_displayed(self):
        return self.player.role() == 'Leviathan'

    form_model = models.Group
    form_fields = ['lev_gamble1','lev_gamble2']

class WaitForLeviathan(WaitPage):
    pass

class LeviathanGamble(Page):
    def is_displayed(self):
        return self.player.role() == 'Leviathan'
    form_model = models.Player
    form_fields = ['lev_gamble1_own', 'lev_gamble2_own']


class GamblerChoice(Page):

    form_model = models.Group
    form_fields = ['gam_gamble1','gam_gamble2']

    def is_displayed(self):
        return self.player.role() == 'Gambler'

    def gam_gamble1_choices(self):
        if self.group.lev_gamble1 < 0:
            return currency_range(
                c(0),
                c(10) + self.group.lev_gamble1,
                c(1)
            )
        elif self.group.lev_gamble1 >= 0:
            return currency_range(
                self.group.lev_gamble1,
                c(10),
                c(1)
            )
        elif self.group.lev_gamble1 == -10:
            return currency_range(
                c(0),
                c(0),
                c(1)
            )
        elif self.group.lev_gamble1 == 10:
            return currency_range(
                c(10),
                c(10),
                c(1)
            )

    def gam_gamble2_choices(self):
        if self.group.lev_gamble2 < 0:
            return currency_range(
                c(0),
                c(10) + self.group.lev_gamble2,
                c(1)
            )
        elif self.group.lev_gamble2 >= 0:
            return currency_range(
                self.group.lev_gamble2,
                c(10),
                c(1)
            )
        elif self.group.lev_gamble2 == -10:
            return currency_range(
                c(0),
                c(0),
                c(1)
            )
        elif self.group.lev_gamble2 == 10:
            return currency_range(
                c(10),
                c(10),
                c(1)
            )

class GamblerFreeChoice(Page):

    def is_displayed(self):
        return self.player.role() == 'Gambler'

    form_model = models.Player
    form_fields = ['gam_gamble_free1','gam_gamble_free2']

class GambleQuestions(Page):
    form_model = models.Player
    form_fields = ['lev_gamble1_evaluation', 'lev_gamble2_evaluation']

class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_gambles()
        self.group.set_payoffs()


class Results(Page):
    pass

class Evaluation(Page):
    form_model = models.Player
    form_fields = ['outcome_happiness', 'restriction_happiness']

    def outcome_happiness_choices(self):
        return self.session.vars['likert']
    def restriction_happiness_choices(self):
        return self.session.vars['likert']


page_sequence = [
    Instructions,
    Test,
    TestWaitPage,
    TestGuessPage,
    SelfFeedback,
    PartnerFeedback,
    FullFeedback,
    LeviathanChoice,
    WaitForLeviathan,
    LeviathanGamble,
    GamblerFreeChoice,
    GamblerChoice,
    GambleQuestions,
    ResultsWaitPage,
    Results,
    Evaluation
]
