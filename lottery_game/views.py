from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
from otree.api import safe_json


class WaitForStart(Page):
    def is_displayed(self):
        return self.player.round_number == 1

class Instructions(Page):

    def is_displayed(self):
        return self.player.round_number == 1

    def vars_for_template(self):
        return {'points_example': Constants.point_conversion*300}

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
        return {'lottery1_condition':Constants.lotteries[0]['condition'],
                'lottery1_return':Constants.lotteries[0]['return per point invested'],
                'lottery1_description':Constants.lotteries[0]['description'],
                'lottery2_condition':Constants.lotteries[1]['condition'],
                'lottery2_return':Constants.lotteries[1]['return per point invested'],
                'lottery2_description':Constants.lotteries[1]['description'],
                'lottery3_condition':Constants.lotteries[2]['condition'],
                'lottery3_return':Constants.lotteries[2]['return per point invested'],
                'lottery3_description':Constants.lotteries[2]['description'],
                'lottery4_condition':Constants.lotteries[3]['condition'],
                'lottery4_return':Constants.lotteries[3]['return per point invested'],
                'lottery4_description':Constants.lotteries[3]['description'],
                'lottery5_condition':Constants.lotteries[4]['condition'],
                'lottery5_return':Constants.lotteries[4]['return per point invested'],
                'lottery5_description':Constants.lotteries[4]['description'],
                'lottery6_condition':Constants.lotteries[5]['condition'],
                'lottery6_return':Constants.lotteries[5]['return per point invested'],
                'lottery6_description':Constants.lotteries[5]['description'],
                }

    form_model = models.Player
    form_fields = ['lotteryChoiceOwn']


class RestrictionChoice(Page):
    form_model = models.Player
    form_fields = ['restrictionChoiceLottery{}'.format(i) for i in range(1,7)]

    def vars_for_template(self):
        return {'lottery1_condition':Constants.lotteries[0]['condition'],
                'lottery1_return':Constants.lotteries[0]['return per point invested'],
                'lottery1_description':Constants.lotteries[0]['description'],
                'lottery2_condition':Constants.lotteries[1]['condition'],
                'lottery2_return':Constants.lotteries[1]['return per point invested'],
                'lottery2_description':Constants.lotteries[1]['description'],
                'lottery3_condition':Constants.lotteries[2]['condition'],
                'lottery3_return':Constants.lotteries[2]['return per point invested'],
                'lottery3_description':Constants.lotteries[2]['description'],
                'lottery4_condition':Constants.lotteries[3]['condition'],
                'lottery4_return':Constants.lotteries[3]['return per point invested'],
                'lottery4_description':Constants.lotteries[3]['description'],
                'lottery5_condition':Constants.lotteries[4]['condition'],
                'lottery5_return':Constants.lotteries[4]['return per point invested'],
                'lottery5_description':Constants.lotteries[4]['description'],
                'lottery6_condition':Constants.lotteries[5]['condition'],
                'lottery6_return':Constants.lotteries[5]['return per point invested'],
                'lottery6_description':Constants.lotteries[5]['description'],
                "player_scores": safe_json(self.session.vars['player_scores']),
                "player_rank": safe_json(self.player.rank)
                }

class WaitForRestrictions(WaitPage):
    wait_for_all_groups = True

    def after_all_players_arrive(self):
        self.subsession.setRestrictions()

class LotteryChoiceOwnRestricted(Page):
    form_model = models.Player
    form_fields = ['restrictedChoice']

    def vars_for_template(self):
        return {'lottery1_condition':Constants.lotteries[0]['condition'],
                'lottery1_return':Constants.lotteries[0]['return per point invested'],
                'lottery1_description':Constants.lotteries[0]['description'],
                'lottery2_condition':Constants.lotteries[1]['condition'],
                'lottery2_return':Constants.lotteries[1]['return per point invested'],
                'lottery2_description':Constants.lotteries[1]['description'],
                'lottery3_condition':Constants.lotteries[2]['condition'],
                'lottery3_return':Constants.lotteries[2]['return per point invested'],
                'lottery3_description':Constants.lotteries[2]['description'],
                'lottery4_condition':Constants.lotteries[3]['condition'],
                'lottery4_return':Constants.lotteries[3]['return per point invested'],
                'lottery4_description':Constants.lotteries[3]['description'],
                'lottery5_condition':Constants.lotteries[4]['condition'],
                'lottery5_return':Constants.lotteries[4]['return per point invested'],
                'lottery5_description':Constants.lotteries[4]['description'],
                'lottery6_condition':Constants.lotteries[5]['condition'],
                'lottery6_return':Constants.lotteries[5]['return per point invested'],
                'lottery6_description':Constants.lotteries[5]['description'],
                }
    def before_next_page(self):
        self.player.setPayoffs()

        if self.round_number == self.session.config['number_of_rounds']:
            self.player.setTotalPayoffs()

class ResultsWaitPage(WaitPage):
    pass

class Results(Page):
    def is_displayed(self):
        return self.round_number == self.session.config['number_of_rounds']

class Finished(Page):
    def is_displayed(self):
        return self.round_number == self.session.config['number_of_rounds']


page_sequence = [
    WaitForStart,
    Instructions,
    Test,
    TestWaitPage,
    TestGuessPage,
    TestFeedback,
    LotteryChoiceOwn,
    RestrictionChoice,
    WaitForRestrictions,
    LotteryChoiceOwnRestricted,
    ResultsWaitPage,
    Results,
    Finished,
    ]
