from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
from otree.api import safe_json



class WaitForArrival(WaitPage):
    wait_for_all_groups = True

class WaitForStart(Page):
    pass

class Instructions(Page):

    def is_displayed(self):
        return self.player.round_number == 1

    def vars_for_template(self):
        return {'points_example': Constants.point_conversion*300, 'quiz_max': Constants.quiz_points*Constants.num_questions}

    form_model = models.Player
    form_fields = ['control{}'.format(i) for i in range(1,7)]

    def control1_error_message(self, value):
        if not (value == 10):
            return 'This is not correct'
    def control2_error_message(self, value):
        if not (value == 14):
            return 'This is not correct'
    def control3_error_message(self, value):
        if not (value == 5):
            return 'This is not correct'
    def control4_error_message(self, value):
        if not (value == True):
            return 'This is not correct'
    def control5_error_message(self, value):
        if not (value == False):
            return 'This is not correct'
    def control6_error_message(self, value):
        if not (value == False):
            return 'This is not correct'


class Test(Page):

    def is_displayed(self):
        return self.player.round_number == 1

    timeout_seconds = Constants.minutes_for_quiz*60
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
        self.player.check_correct()

class TestWaitPage(WaitPage):

    wait_for_all_groups = True
    def after_all_players_arrive(self):
        self.subsession.set_scores_after_round1()
        self.subsession.calc_stats()
        self.subsession.get_player_scores()
        self.subsession.get_partner_score()

class TestGuessPage(Page):

    def is_displayed(self):
        return self.round_number == 1

    form_model = models.Player
    form_fields = ['score_guess']

    def vars_for_template(self):
        return {
            "player_scores": safe_json(self.session.vars['player_scores'])
            }

class TestFeedback(Page):

    def is_displayed(self):
        return self.round_number == 1 and self.player.treatment == "full"

    def vars_for_template(self):
        return {
            "player_scores": safe_json(self.session.vars['player_scores']),
            "player_rank": safe_json(self.player.rank)
            }

class LotteryChoiceOwn(Page):

    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return {'lottery11_condition':Constants.lotteries[0]['condition'],
                'lottery11_return':Constants.lotteries[0]['return per point invested'],
                'lottery11_description':Constants.lotteries[0]['description'],
                'lottery12_condition':Constants.lotteries[1]['condition'],
                'lottery12_return':Constants.lotteries[1]['return per point invested'],
                'lottery12_description':Constants.lotteries[1]['description'],
                'lottery21_condition':Constants.lotteries[2]['condition'],
                'lottery21_return':Constants.lotteries[2]['return per point invested'],
                'lottery21_description':Constants.lotteries[2]['description'],
                'lottery22_condition':Constants.lotteries[3]['condition'],
                'lottery22_return':Constants.lotteries[3]['return per point invested'],
                'lottery22_description':Constants.lotteries[3]['description'],
                'lottery23_condition':Constants.lotteries[4]['condition'],
                'lottery23_return':Constants.lotteries[4]['return per point invested'],
                'lottery23_description':Constants.lotteries[4]['description'],
                'lottery31_condition':Constants.lotteries[5]['condition'],
                'lottery31_return':Constants.lotteries[5]['return per point invested'],
                'lottery31_description':Constants.lotteries[5]['description'],
                'lottery32_condition':Constants.lotteries[6]['condition'],
                'lottery32_return':Constants.lotteries[6]['return per point invested'],
                'lottery32_description':Constants.lotteries[6]['description'],
                'lottery41_condition':Constants.lotteries[7]['condition'],
                'lottery41_return':Constants.lotteries[7]['return per point invested'],
                'lottery41_description':Constants.lotteries[7]['description'],
                'lottery42_condition':Constants.lotteries[8]['condition'],
                'lottery42_return':Constants.lotteries[8]['return per point invested'],
                'lottery42_description':Constants.lotteries[8]['description'],
                'lottery43_condition':Constants.lotteries[9]['condition'],
                'lottery43_return':Constants.lotteries[9]['return per point invested'],
                'lottery43_description':Constants.lotteries[9]['description'],
                "player_scores": safe_json(self.session.vars['player_scores']),
                "player_rank": safe_json(self.player.rank)
                }

    form_model = models.Player
    form_fields = ['unrestrictedChoiceLoseMoney', 'unrestrictedChoiceFirstOrderDominance', 'unrestrictedChoiceSecondOrderDominance', 'unrestrictedChoiceVariableRisk']

class RestrictionChoice(Page):

    def is_displayed(self):
        return self.round_number <= self.session.config['number_of_rounds_lottery']

    form_model = models.Player
    form_fields = ['restrictionChoiceLoseMoney','restrictionChoiceFirstOrderDominance','restrictionChoiceSecondOrderDominance','restrictionChoiceVariableRisk']

    def vars_for_template(self):
        return {'lottery11_condition':Constants.lotteries[0]['condition'],
                'lottery11_return':Constants.lotteries[0]['return per point invested'],
                'lottery11_description':Constants.lotteries[0]['description'],
                'lottery12_condition':Constants.lotteries[1]['condition'],
                'lottery12_return':Constants.lotteries[1]['return per point invested'],
                'lottery12_description':Constants.lotteries[1]['description'],
                'lottery21_condition':Constants.lotteries[2]['condition'],
                'lottery21_return':Constants.lotteries[2]['return per point invested'],
                'lottery21_description':Constants.lotteries[2]['description'],
                'lottery22_condition':Constants.lotteries[3]['condition'],
                'lottery22_return':Constants.lotteries[3]['return per point invested'],
                'lottery22_description':Constants.lotteries[3]['description'],
                'lottery23_condition':Constants.lotteries[4]['condition'],
                'lottery23_return':Constants.lotteries[4]['return per point invested'],
                'lottery23_description':Constants.lotteries[4]['description'],
                'lottery31_condition':Constants.lotteries[5]['condition'],
                'lottery31_return':Constants.lotteries[5]['return per point invested'],
                'lottery31_description':Constants.lotteries[5]['description'],
                'lottery32_condition':Constants.lotteries[6]['condition'],
                'lottery32_return':Constants.lotteries[6]['return per point invested'],
                'lottery32_description':Constants.lotteries[6]['description'],
                'lottery41_condition':Constants.lotteries[7]['condition'],
                'lottery41_return':Constants.lotteries[7]['return per point invested'],
                'lottery41_description':Constants.lotteries[7]['description'],
                'lottery42_condition':Constants.lotteries[8]['condition'],
                'lottery42_return':Constants.lotteries[8]['return per point invested'],
                'lottery42_description':Constants.lotteries[8]['description'],
                'lottery43_condition':Constants.lotteries[9]['condition'],
                'lottery43_return':Constants.lotteries[9]['return per point invested'],
                'lottery43_description':Constants.lotteries[9]['description'],
                "player_scores": safe_json(self.session.vars['player_scores']),
                "player_rank": safe_json(self.player.rank)
                }

class WaitForRestrictions(WaitPage):
    wait_for_all_groups = True

    def after_all_players_arrive(self):
        self.subsession.setRestrictions()

class LotteryChoiceOwnRestricted(Page):

    def is_displayed(self):
        return self.round_number <= self.session.config['number_of_rounds_lottery']

    form_model = models.Player
    form_fields = ['restrictedChoiceLoseMoney','restrictedChoiceFirstOrderDominance','restrictedChoiceSecondOrderDominance','restrictedChoiceVariableRisk']

    def vars_for_template(self):
        return {'lottery11_condition':Constants.lotteries[0]['condition'],
                'lottery11_return':Constants.lotteries[0]['return per point invested'],
                'lottery11_description':Constants.lotteries[0]['description'],
                'lottery12_condition':Constants.lotteries[1]['condition'],
                'lottery12_return':Constants.lotteries[1]['return per point invested'],
                'lottery12_description':Constants.lotteries[1]['description'],
                'lottery21_condition':Constants.lotteries[2]['condition'],
                'lottery21_return':Constants.lotteries[2]['return per point invested'],
                'lottery21_description':Constants.lotteries[2]['description'],
                'lottery22_condition':Constants.lotteries[3]['condition'],
                'lottery22_return':Constants.lotteries[3]['return per point invested'],
                'lottery22_description':Constants.lotteries[3]['description'],
                'lottery23_condition':Constants.lotteries[4]['condition'],
                'lottery23_return':Constants.lotteries[4]['return per point invested'],
                'lottery23_description':Constants.lotteries[4]['description'],
                'lottery31_condition':Constants.lotteries[5]['condition'],
                'lottery31_return':Constants.lotteries[5]['return per point invested'],
                'lottery31_description':Constants.lotteries[5]['description'],
                'lottery32_condition':Constants.lotteries[6]['condition'],
                'lottery32_return':Constants.lotteries[6]['return per point invested'],
                'lottery32_description':Constants.lotteries[6]['description'],
                'lottery41_condition':Constants.lotteries[7]['condition'],
                'lottery41_return':Constants.lotteries[7]['return per point invested'],
                'lottery41_description':Constants.lotteries[7]['description'],
                'lottery42_condition':Constants.lotteries[8]['condition'],
                'lottery42_return':Constants.lotteries[8]['return per point invested'],
                'lottery42_description':Constants.lotteries[8]['description'],
                'lottery43_condition':Constants.lotteries[9]['condition'],
                'lottery43_return':Constants.lotteries[9]['return per point invested'],
                'lottery43_description':Constants.lotteries[9]['description'],
                }

    def before_next_page(self):
        self.player.setPayoffs()

        if self.round_number == self.session.config['number_of_rounds_lottery']:
            self.player.setTotalPayoffs()

class ResultsWaitPage(WaitPage):
    pass

class Results(Page):
    def is_displayed(self):
        return self.round_number == self.session.config['number_of_rounds_lottery']

    def vars_for_template(self):
        return {'test_return': Constants.quiz_points*self.player.test_score}

class Finished(Page):
    def is_displayed(self):
        return self.round_number == self.session.config['number_of_rounds_lottery']


page_sequence = [
    WaitForArrival,
    Instructions,
    Test,
    TestWaitPage,
    TestGuessPage,
    LotteryChoiceOwn,
    RestrictionChoice,
    WaitForRestrictions,
    LotteryChoiceOwnRestricted,
    ResultsWaitPage,
    Results
    ]
