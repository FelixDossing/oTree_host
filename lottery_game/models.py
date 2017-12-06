from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import csv, random, itertools


author = 'Felix Sebastian Døssing'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'lotterygame'
    players_per_group = None
    num_rounds = 9

    minutes_for_quiz = 30

    with open('lottery_game/probability_quiz.csv') as q:
        questions = list(csv.DictReader(q))

    with open('lottery_game/lotteries.csv') as g:
        lotteries = list(csv.DictReader(g))

    num_questions = len(questions)

    quiz_points = 20 # Points for each correct answer in the quiz (if points are given for quiz answers
    point_conversion = 0.2

    # Conversion rate: 1 point = 4 DKK
    endowment = c(80)

    minutes_ownChoice = 5


class Subsession(BaseSubsession):

    num_players = models.IntegerField()
    total_score = models.IntegerField()
    average_score = models.FloatField()

    quiz_payoff_draw = models.IntegerField()

    die1round1 = models.IntegerField()
    die2round1 = models.IntegerField()
    die1round2 = models.IntegerField()
    die2round2 = models.IntegerField()
    die1round3 = models.IntegerField()
    die2round3 = models.IntegerField()
    die1round4 = models.IntegerField()
    die2round4 = models.IntegerField()
    die1round5 = models.IntegerField()
    die2round5 = models.IntegerField()
    die1round6 = models.IntegerField()
    die2round6 = models.IntegerField()
    die1round7 = models.IntegerField()
    die2round7 = models.IntegerField()
    die1round8 = models.IntegerField()
    die2round8 = models.IntegerField()
    die1round9 = models.IntegerField()
    die2round9 = models.IntegerField()
    die1round10 = models.IntegerField()
    die2round10 = models.IntegerField()

    firstOrderDraw = models.IntegerField()
    variableRiskDraw = models.IntegerField()


    def creating_session(self):

        for p in self.get_players():
            p.restrictedLottery_draw = random.randint(1,4)
            p.unrestrictedLottery_draw = random.randint(1,4)

        #Die1Round1, Die2Round1, Die1Round2, Die2Round2 ...
        if self.round_number == 1:
            self.die1round1 = random.randint(1,6)
            self.die2round1 = random.randint(1,6)
            self.die1round2 = random.randint(1,6)
            self.die2round2 = random.randint(1,6)
            self.die1round3 = random.randint(1,6)
            self.die2round3 = random.randint(1,6)
            self.die1round4 = random.randint(1,6)
            self.die2round4 = random.randint(1,6)
            self.die1round5 = random.randint(1,6)
            self.die2round5 = random.randint(1,6)
            self.die1round6 = random.randint(1,6)
            self.die2round6 = random.randint(1,6)
            self.die1round7 = random.randint(1,6)
            self.die2round7 = random.randint(1,6)
            self.die1round8 = random.randint(1,6)
            self.die2round8 = random.randint(1,6)
            self.die1round9 = random.randint(1,6)
            self.die2round9 = random.randint(1,6)
            self.die1round10 = random.randint(1,6)
            self.die2round10 = random.randint(1,6)
        elif self.round_number > 1:
            self.die1round1 = self.in_round(1).die1round1
            self.die2round1 = self.in_round(1).die2round1
            self.die1round2 = self.in_round(1).die1round2
            self.die2round2 = self.in_round(1).die2round2
            self.die1round3 = self.in_round(1).die1round3
            self.die2round3 = self.in_round(1).die2round3
            self.die1round4 = self.in_round(1).die1round4
            self.die2round4 = self.in_round(1).die2round4
            self.die1round5 = self.in_round(1).die1round5
            self.die2round5 = self.in_round(1).die2round5
            self.die1round6 = self.in_round(1).die1round6
            self.die2round6 = self.in_round(1).die2round6
            self.die1round7 = self.in_round(1).die1round7
            self.die2round7 = self.in_round(1).die2round7
            self.die1round8 = self.in_round(1).die1round8
            self.die2round8 = self.in_round(1).die2round8
            self.die1round9 = self.in_round(1).die1round9
            self.die2round9 = self.in_round(1).die2round9
            self.die1round10 = self.in_round(1).die1round10
            self.die2round10 = self.in_round(1).die2round10


            self.session.vars['dicerolls'] = [[self.die1round1,self.die2round1],[self.die1round2,self.die2round2],[self.die1round3,self.die2round3],[self.die1round4,self.die2round4],
                                              [self.die1round5,self.die2round5],[self.die1round6,self.die2round6],[self.die1round7,self.die2round7],[self.die1round8,self.die2round8],
                                              [self.die1round9,self.die2round9],[self.die1round10,self.die2round10]]

        self.num_players = len(self.get_players())

        if self.round_number == 1:
            self.session.vars['players_list'] = []
            for i in range(1,self.num_players+1):
                self.session.vars['players_list'].append(i)
            random.shuffle(self.session.vars['players_list'])

        ## Set player id
        if self.round_number == 1:
            for i in range(0,self.num_players):
                self.get_players()[i].player_id = i+1
        else:
            for i in range(0,self.num_players):
                self.get_players()[i].player_id = self.get_players()[i].in_round(1).player_id

        self.session.vars['players_list_extended'] = self.session.vars['players_list'] + self.session.vars['players_list']

        for p in self.get_players():
            if (self.round_number <= (self.num_players-2)/2):
                position = self.session.vars['players_list'].index(p.player_id)
                p.partner_id = self.session.vars['players_list_extended'][position+self.round_number]
            ## In case there are too many rounds compared to players
            else:
                p.partner_id = p.in_round(self.round_number-1).partner_id

        ## set parternalist id
        for p in self.get_players():
            for q in self.get_players():
                if q.partner_id == p.player_id:
                    p.paternalist_id = q.player_id

        ## Set treatments
        if self.round_number == 1:
            treatments = itertools.cycle(['partner', 'full', 'full'])
            for p in self.get_players():
                p.treatment = next(treatments)
        else:
            for p in self.get_players():
                p.treatment = p.in_round(1).treatment

        self.session.vars['questions'] = Constants.questions
        self.session.vars['lotteries'] = Constants.lotteries

        self.session.vars['likert'] = ['Strongly disagree', 'Disagree', 'Neither agree nor disagree', 'Agree', 'Strongly agree']

        self.quiz_payoff_draw = random.randint(1, self.num_players)

        ## set payoff round number
        for p in self.get_players():
            if self.round_number == 1:
                p.restricted_payoff_round = random.randint(1, self.session.config['number_of_rounds_lottery'])
            else:
                p.restricted_payoff_round = p.in_round(1).restricted_payoff_round

        ## Set test questions
        for p in self.get_players():
            question_data = self.session.vars['questions']
            p.question1 = question_data[0]['question']
            p.question2 = question_data[1]['question']
            p.question3 = question_data[2]['question']
            p.question4 = question_data[3]['question']
            p.question5 = question_data[4]['question']
            p.question6 = question_data[5]['question']
            p.question7 = question_data[6]['question']
            p.question8 = question_data[7]['question']
            p.question9 = question_data[8]['question']
            p.question10 = question_data[9]['question']
            p.question11 = question_data[10]['question']
            p.question12 = question_data[11]['question']
            p.question13 = question_data[12]['question']
            p.question14 = question_data[13]['question']
            p.question15 = question_data[14]['question']
            p.question16 = question_data[15]['question']
            p.question17 = question_data[16]['question']
            p.question18 = question_data[17]['question']
            p.question19 = question_data[18]['question']
            p.question20 = question_data[19]['question']

            p.solution1 = question_data[0]['solution']
            p.solution2 = question_data[1]['solution']
            p.solution3 = question_data[2]['solution']
            p.solution4 = question_data[3]['solution']
            p.solution5 = question_data[4]['solution']
            p.solution6 = question_data[5]['solution']
            p.solution7 = question_data[6]['solution']
            p.solution8 = question_data[7]['solution']
            p.solution9 = question_data[8]['solution']
            p.solution10 = question_data[9]['solution']
            p.solution11 = question_data[10]['solution']
            p.solution12 = question_data[11]['solution']
            p.solution13 = question_data[12]['solution']
            p.solution14 = question_data[13]['solution']
            p.solution15 = question_data[14]['solution']
            p.solution16 = question_data[15]['solution']
            p.solution17 = question_data[16]['solution']
            p.solution18 = question_data[17]['solution']
            p.solution19 = question_data[18]['solution']
            p.solution20 = question_data[19]['solution']

            p.rank = len(self.get_players())

        for p in self.get_players():
            p.quiz_payoff_bool = True if p.participant.id_in_session == self.quiz_payoff_draw else False

        ## Determining choice order
        for p in self.get_players():
            if p.round_number == 1:
                p.participant.vars['choicelist'] = ['loseMoney', 'firstOrderDominance', 'secondOrderDominance', 'variableRisk']
                random.shuffle(p.participant.vars['choicelist'])
                p.first_choice = p.participant.vars['choicelist'][0]
                p.second_choice = p.participant.vars['choicelist'][1]
                p.third_choice = p.participant.vars['choicelist'][2]
                p.fourth_choice = p.participant.vars['choicelist'][3]
            else:
                p.first_choice = p.in_round(1).first_choice
                p.second_choice = p.in_round(1).second_choice
                p.third_choice = p.in_round(1).third_choice
                p.fourth_choice = p.in_round(1).fourth_choice


        ## Determining lottery order
        if self.round_number == 1:
            self.firstOrderDraw = random.randint(1,2)
            self.variableRiskDraw = random.randint(1,3)

        for p in self.get_players():
            if p.round_number == 1:

                p.participant.vars['twonumberlist'] = [1,2]

                random.shuffle(p.participant.vars['twonumberlist'])
                p.lottery11_placement = p.participant.vars['twonumberlist'][0]
                p.lottery12_placement = p.participant.vars['twonumberlist'][1]

                random.shuffle(p.participant.vars['twonumberlist'])

                if self.firstOrderDraw == 1:
                    ### Lotter 21 and 23
                    p.lottery21_placement = p.participant.vars['twonumberlist'][0]
                    p.lottery23_placement = p.participant.vars['twonumberlist'][1]
                    p.lottery22_placement = 0
                elif self.firstOrderDraw == 2:
                    ### Lottery 22 and 23
                    p.lottery22_placement = p.participant.vars['twonumberlist'][0]
                    p.lottery23_placement = p.participant.vars['twonumberlist'][1]
                    p.lottery21_placement = 0

                random.shuffle(p.participant.vars['twonumberlist'])
                p.lottery31_placement = p.participant.vars['twonumberlist'][0]
                p.lottery32_placement = p.participant.vars['twonumberlist'][1]

                random.shuffle(p.participant.vars['twonumberlist'])
                if self.variableRiskDraw == 1:
                    ### 41 and 42
                    p.lottery41_placement = p.participant.vars['twonumberlist'][0]
                    p.lottery42_placement = p.participant.vars['twonumberlist'][1]
                    p.lottery43_placement = 0
                elif self.variableRiskDraw == 2:
                    ### 41 and 43
                    p.lottery41_placement = p.participant.vars['twonumberlist'][0]
                    p.lottery43_placement = p.participant.vars['twonumberlist'][1]
                    p.lottery42_placement = 0
                elif self.variableRiskDraw == 3:
                    #¤¤ 42 and 43
                    p.lottery43_placement = p.participant.vars['twonumberlist'][0]
                    p.lottery42_placement = p.participant.vars['twonumberlist'][1]
                    p.lottery41_placement = 0

            else:
                p.lottery11_placement = p.in_round(1).lottery11_placement
                p.lottery12_placement = p.in_round(1).lottery12_placement
                p.lottery21_placement = p.in_round(1).lottery21_placement
                p.lottery22_placement = p.in_round(1).lottery22_placement
                p.lottery23_placement = p.in_round(1).lottery23_placement
                p.lottery31_placement = p.in_round(1).lottery31_placement
                p.lottery32_placement = p.in_round(1).lottery32_placement
                p.lottery41_placement = p.in_round(1).lottery41_placement
                p.lottery42_placement = p.in_round(1).lottery42_placement
                p.lottery43_placement = p.in_round(1).lottery43_placement


    def calc_stats(self):
        self.total_score = sum(p.test_score for p in self.get_players())
        self.average_score = self.total_score / self.num_players
        for p in self.get_players():
            for q in self.get_players():
                if p.test_score > q.test_score:
                    p.rank -= 1

    def get_player_scores(self):
        self.session.vars['player_scores'] = []
        for p in self.get_players():
            self.session.vars['player_scores'].append(p.test_score)
        self.session.vars['player_scores'].sort()

    def get_partner_score(self):
        for p in self.get_players():
            for q in self.get_players():
                if p.partner_id == q.player_id:
                    p.partner_test_score = q.test_score

    def setRestrictions(self):




        for p in self.get_players():
            for q in self.get_players():
                if p.partner_id == q.player_id:
                    p.partnerRestrictionLoseMoney = q.restrictionChoiceLoseMoney
                    p.partnerRestrictionFirstOrderDominance = q.restrictionChoiceFirstOrderDominance
                    p.partnerRestrictionSecondOrderDominance = q.restrictionChoiceSecondOrderDominance
                    p.partnerRestrictionVariableRisk = q.restrictionChoiceVariableRisk

    def set_scores_after_round1(self):
        if self.round_number > 1:
            for p in self.get_players():
                p.test_score = p.in_round(1).test_score


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    treatment = models.CharField()
    player_id = models.IntegerField()

    partner_id = models.IntegerField()
    paternalist_id = models.IntegerField()

    restricted_payoff_round = models.IntegerField()

    #----# FOR TEST #-----#

    control1 = models.IntegerField()
    control2 = models.IntegerField()
    control3 = models.IntegerField()
    control4 = models.BooleanField()
    control5 = models.BooleanField() # The Orange player got a better score than the blue player
    control6 = models.BooleanField() # The Orange player got the second-worst score among all players

    feedback_control_own_score = models.BooleanField()
    feedback_control_partner_score = models.BooleanField()
    feedback_control_expected_partner = models.BooleanField()
    feedback_control_compare = models.BooleanField()

    rank = models.IntegerField(initial=0)

    question_id = models.PositiveIntegerField()

    question1 = models.CharField()
    question2 = models.CharField()
    question3 = models.CharField()
    question4 = models.CharField()
    question5 = models.CharField()
    question6 = models.CharField()
    question7 = models.CharField()
    question8 = models.CharField()
    question9 = models.CharField()
    question10 = models.CharField()
    question11 = models.CharField()
    question12 = models.CharField()
    question13 = models.CharField()
    question14 = models.CharField()
    question15 = models.CharField()
    question16 = models.CharField()
    question17 = models.CharField()
    question18 = models.CharField()
    question19 = models.CharField()
    question20 = models.CharField()

    solution1 = models.CharField()
    solution2 = models.CharField()
    solution3 = models.CharField()
    solution4 = models.CharField()
    solution5 = models.CharField()
    solution6 = models.CharField()
    solution7 = models.CharField()
    solution8 = models.CharField()
    solution9 = models.CharField()
    solution10 = models.CharField()
    solution11 = models.CharField()
    solution12 = models.CharField()
    solution13 = models.CharField()
    solution14 = models.CharField()
    solution15 = models.CharField()
    solution16 = models.CharField()
    solution17 = models.CharField()
    solution18 = models.CharField()
    solution19 = models.CharField()
    solution20 = models.CharField()

    submitted_answer1 = models.CharField(widget=widgets.RadioSelect())
    submitted_answer2 = models.CharField(widget=widgets.RadioSelect())
    submitted_answer3 = models.CharField(widget=widgets.RadioSelect())
    submitted_answer4 = models.CharField(widget=widgets.RadioSelect())
    submitted_answer5 = models.CharField(widget=widgets.RadioSelect())
    submitted_answer6 = models.CharField(widget=widgets.RadioSelect())
    submitted_answer7 = models.CharField(widget=widgets.RadioSelect())
    submitted_answer8 = models.CharField(widget=widgets.RadioSelect())
    submitted_answer9 = models.CharField(widget=widgets.RadioSelect())
    submitted_answer10 = models.CharField(widget=widgets.RadioSelect())
    submitted_answer11 = models.CharField(widget=widgets.RadioSelect())
    submitted_answer12 = models.CharField(widget=widgets.RadioSelect())
    submitted_answer13 = models.CharField(widget=widgets.RadioSelect())
    submitted_answer14 = models.CharField(widget=widgets.RadioSelect())
    submitted_answer15 = models.CharField(widget=widgets.RadioSelect())
    submitted_answer16 = models.CharField(widget=widgets.RadioSelect())
    submitted_answer17 = models.CharField(widget=widgets.RadioSelect())
    submitted_answer18 = models.CharField(widget=widgets.RadioSelect())
    submitted_answer19 = models.CharField(widget=widgets.RadioSelect())
    submitted_answer20 = models.CharField(widget=widgets.RadioSelect())

    # submitted_answer1 = models.CharField(initial = "1/5", widget=widgets.RadioSelect())
    # submitted_answer2 = models.CharField(initial = "1/3", widget=widgets.RadioSelect())
    # submitted_answer3 = models.CharField(initial = "4", widget=widgets.RadioSelect())
    # submitted_answer4 = models.CharField(initial = "3/13", widget=widgets.RadioSelect())
    # submitted_answer5 = models.CharField(initial = "Lisa (20%), Jim (40%), Andreas (-10%), Caroline (50%)", widget=widgets.RadioSelect())
    # submitted_answer6 = models.CharField(initial = "35%", widget=widgets.RadioSelect())
    # submitted_answer7 = models.CharField(initial = "12/15", widget=widgets.RadioSelect())
    # submitted_answer8 = models.CharField(initial = "1/3", widget=widgets.RadioSelect())
    # submitted_answer9 = models.CharField(initial = "10", widget=widgets.RadioSelect())
    # submitted_answer10 = models.CharField(initial = "10%", widget=widgets.RadioSelect())
    # submitted_answer11 = models.CharField(initial = "1/3", widget=widgets.RadioSelect())
    # submitted_answer12 = models.CharField(initial = "12.8%", widget=widgets.RadioSelect())
    # submitted_answer13 = models.CharField(initial = "1/4", widget=widgets.RadioSelect())
    # submitted_answer14 = models.CharField(initial = "About 15%", widget=widgets.RadioSelect())
    # submitted_answer15 = models.CharField(initial = "65%", widget=widgets.RadioSelect())
    # submitted_answer16 = models.CharField(initial = "17.25 points", widget=widgets.RadioSelect())
    # submitted_answer17 = models.CharField(initial = "25%", widget=widgets.RadioSelect())
    # submitted_answer18 = models.CharField(initial = "About 35%", widget=widgets.RadioSelect())
    # submitted_answer19 = models.CharField(initial = "84", widget=widgets.RadioSelect())
    # submitted_answer20 = models.CharField(initial = "About 22.5%", widget=widgets.RadioSelect())

    # For testing
    def set_test_values(self):
        self.submitted_answer1 = "1/4" if random.random() > 0.5 else "1/5"
        self.submitted_answer2 = "1/2" if random.random() > 0.5 else "1"
        self.submitted_answer3 = "1/6" if random.random() > 0.5 else "0.4"
        self.submitted_answer4 = "12/52" if random.random() > 0.5 else "3/13"
        self.submitted_answer5 = "Lisa (0%), Jim (25%), Andreas (40%), Caroline (35%)" if random.random() > 0.5 else "Lisa (20%), Jim (30%), Andreas (0%), Caroline (0%)"
        self.submitted_answer6 = "35%" if random.random() > 0.5 else "1/6"
        self.submitted_answer7 = "15/16" if random.random() > 0.5 else "12/15"
        self.submitted_answer8 = "1/9" if random.random() > 0.5 else "1/3"
        self.submitted_answer9 = "10" if random.random() > 0.5 else "151200"
        self.submitted_answer10 = "20%" if random.random() > 0.5 else "0"
        self.submitted_answer11 = "1/6" if random.random() > 0.5 else "1/20"
        self.submitted_answer12 = "6.25%" if random.random() > 0.5 else "12.8%"
        self.submitted_answer13 = "1/24" if random.random() > 0.5 else "20%"
        self.submitted_answer14 = "About 11%" if random.random() > 0.5 else "About 15%"
        self.submitted_answer15 = "94%" if random.random() > 0.5 else "6%"
        self.submitted_answer16 = "17.25 points" if random.random() > 0.5 else "45.5 points"
        self.submitted_answer17 = "37.5%" if random.random() > 0.5 else "51.2%"
        self.submitted_answer18 = "1/210" if random.random() > 0.5 else "1/10000"
        self.submitted_answer19 = "About 22.5%" if random.random() > 0.5 else "50%"
        self.submitted_answer20 = "About 27%" if random.random() > 0.5 else "50%"

    is_correct1 = models.BooleanField()
    is_correct2 = models.BooleanField()
    is_correct3 = models.BooleanField()
    is_correct4 = models.BooleanField()
    is_correct5 = models.BooleanField()
    is_correct6 = models.BooleanField()
    is_correct7 = models.BooleanField()
    is_correct8 = models.BooleanField()
    is_correct9 = models.BooleanField()
    is_correct10 = models.BooleanField()
    is_correct11 = models.BooleanField()
    is_correct12 = models.BooleanField()
    is_correct13 = models.BooleanField()
    is_correct14 = models.BooleanField()
    is_correct15 = models.BooleanField()
    is_correct16 = models.BooleanField()
    is_correct17 = models.BooleanField()
    is_correct18 = models.BooleanField()
    is_correct19 = models.BooleanField()
    is_correct20 = models.BooleanField()


    test_score = models.IntegerField()
    partner_test_score = models.IntegerField()

    score_guess = models.IntegerField()

    quiz_payoff_bool = models.BooleanField() # Boolean true if player recieves payoff from quiz

    outcome_happiness = models.CharField(widget=widgets.RadioSelectHorizontal)
    partner_rectriction_happiness = models.CharField(widget=widgets.RadioSelectHorizontal)
    own_restriction_happiness = models.CharField(widget=widgets.RadioSelectHorizontal)

    def check_correct(self):
        self.is_correct1 = self.submitted_answer1 == self.solution1
        self.is_correct2 = self.submitted_answer2 == self.solution2
        self.is_correct3 = self.submitted_answer3 == self.solution3
        self.is_correct4 = self.submitted_answer4 == self.solution4
        self.is_correct5 = self.submitted_answer5 == self.solution5
        self.is_correct6 = self.submitted_answer6 == self.solution6
        self.is_correct7 = self.submitted_answer7 == self.solution7
        self.is_correct8 = self.submitted_answer8 == self.solution8
        self.is_correct9 = self.submitted_answer9 == self.solution9
        self.is_correct10 = self.submitted_answer10 == self.solution10
        self.is_correct11 = self.submitted_answer11 == self.solution11
        self.is_correct12 = self.submitted_answer12 == self.solution12
        self.is_correct13 = self.submitted_answer13 == self.solution13
        self.is_correct14 = self.submitted_answer14 == self.solution14
        self.is_correct15 = self.submitted_answer15 == self.solution15
        self.is_correct16 = self.submitted_answer16 == self.solution16
        self.is_correct17 = self.submitted_answer17 == self.solution17
        self.is_correct18 = self.submitted_answer18 == self.solution18
        self.is_correct19 = self.submitted_answer19 == self.solution19
        self.is_correct20 = self.submitted_answer20 == self.solution20


        self.test_score = sum([self.is_correct1, self.is_correct2, self.is_correct3, self.is_correct4,
                               self.is_correct5, self.is_correct6, self.is_correct7, self.is_correct8,
                               self.is_correct9, self.is_correct10, self.is_correct11, self.is_correct12,
                               self.is_correct13, self.is_correct14, self.is_correct15, self.is_correct16,
                               self.is_correct17, self.is_correct18, self.is_correct19, self.is_correct20])


    #----# FOR LOTTERY & Restriction #----#
    first_choice = models.CharField()
    second_choice = models.CharField()
    third_choice = models.CharField()
    fourth_choice = models.CharField()

    lottery11_placement = models.IntegerField()
    lottery12_placement = models.IntegerField()
    lottery21_placement = models.IntegerField()
    lottery22_placement = models.IntegerField()
    lottery23_placement = models.IntegerField()
    lottery31_placement = models.IntegerField()
    lottery32_placement = models.IntegerField()
    lottery41_placement = models.IntegerField()
    lottery42_placement = models.IntegerField()
    lottery43_placement = models.IntegerField()

    unrestrictedChoiceLoseMoney = models.CharField()
    unrestrictedChoiceFirstOrderDominance = models.CharField()
    unrestrictedChoiceSecondOrderDominance = models.CharField()
    unrestrictedChoiceVariableRisk = models.CharField()

    restrictionChoiceLoseMoney = models.CharField()
    restrictionChoiceFirstOrderDominance = models.CharField()
    restrictionChoiceSecondOrderDominance = models.CharField()
    restrictionChoiceVariableRisk = models.CharField()

    partnerRestrictionLoseMoney = models.CharField()
    partnerRestrictionFirstOrderDominance = models.CharField()
    partnerRestrictionSecondOrderDominance = models.CharField()
    partnerRestrictionVariableRisk = models.CharField()

    restrictedChoiceLoseMoney = models.CharField()
    restrictedChoiceFirstOrderDominance = models.CharField()
    restrictedChoiceSecondOrderDominance = models.CharField()
    restrictedChoiceVariableRisk = models.CharField()

    unrestricted_payoff = models.CurrencyField()
    restricted_payoff = models.CurrencyField()

    unrestrictedLottery_draw = models.IntegerField()
    restrictedLottery_draw = models.IntegerField()

    def setPayoffs(self):
        die1 = self.session.vars['dicerolls'][self.round_number-1][0]
        die2 = self.session.vars['dicerolls'][self.round_number-1][1]
        dice_sum = die1 + die2


        ## Unrestricted
        if self.round_number == 1:
            self.unrestrictedLottery_draw = random.randint(1,4) # 1=losemoney, 2=firstorder, 3=secondorder, 4=variableRisk
            if self.unrestrictedLottery_draw == 1:
                if self.unrestrictedChoiceLoseMoney == "Lottery 1.1":
                    if die1 < 3 and die2 < 3:
                        self.unrestricted_payoff = Constants.endowment * dice_sum
                    else:
                        self.unrestricted_payoff = 0
                elif self.unrestrictedChoiceLoseMoney == "Lottery 1.2":
                    if die1 > 4 or die2 > 4:
                        self.unrestricted_payoff = Constants.endowment * max(die1, die2)
                    else:
                        self.unrestricted_payoff = 0
            elif self.unrestrictedLottery_draw == 2:
                if self.unrestrictedChoiceFirstOrderDominance == "Lottery 2.1":
                    if die1 > 3 or die2 > 3:
                        self.unrestricted_payoff = Constants.endowment * dice_sum
                    else:
                        self.unrestricted_payoff = 0
                elif self.unrestrictedChoiceFirstOrderDominance == "Lottery 2.2":
                    if die1 > 2 and die2 > 2:
                        self.unrestricted_payoff = Constants.endowment * dice_sum
                    else:
                        self.unrestricted_payoff = 0
                elif self.unrestrictedChoiceFirstOrderDominance == "Lottery 2.3":
                    if die1 < 5 and die2 < 5:
                        self.unrestricted_payoff = Constants.endowment * dice_sum
                    else:
                        self.unrestricted_payoff = 0
            elif self.unrestrictedLottery_draw == 3:
                if self.unrestrictedChoiceSecondOrderDominance == "Lottery 3.1":
                    if die1 < 3 or die2 < 3:
                        self.unrestricted_payoff = dice_sum * Constants.endowment
                    else:
                        self.unrestricted_payoff = 0
                elif self.unrestrictedChoiceSecondOrderDominance == "Lottery 3.2":
                    if die1 < 3 or die2 < 3:
                        self.unrestricted_payoff = (dice_sum - die1 + die2) * Constants.endowment
                    else:
                        self.unrestricted_payoff = 0
            elif self.unrestrictedLottery_draw == 4:
                if self.unrestrictedChoiceVariableRisk == "Lottery 4.1":
                    self.unrestricted_payoff = Constants.endowment * 1.25
                elif self.unrestrictedChoiceVariableRisk == "Lottery 4.2":
                    if die1 < 3 or die2 < 3:
                        self.unrestricted_payoff = Constants.endowment * dice_sum
                    else:
                        self.unrestricted_payoff = 0
                elif self.unrestrictedChoiceVariableRisk == "Lottery 4.3":
                    if die1 > 2 and die2 > 2:
                        self.unrestricted_payoff = Constants.endowment * dice_sum
                    else:
                        self.unrestricted_payoff = 0

        ### restricted

        if self.restrictedLottery_draw == 1:
            if self.restrictedChoiceLoseMoney == "Lottery 1.1":
                if die1 < 3 and die2 < 3:
                    self.restricted_payoff = Constants.endowment * dice_sum
                else:
                    self.restricted_payoff = 0
            elif self.restrictedChoiceLoseMoney == "Lottery 1.2":
                if die1 > 4 or die2 > 4:
                    self.restricted_payoff = Constants.endowment * max(die1, die2)
                else:
                    self.restricted_payoff = 0
        elif self.restrictedLottery_draw == 2:
            if self.restrictedChoiceFirstOrderDominance == "Lottery 2.1":
                if die1 > 3 or die2 > 3:
                    self.restricted_payoff = Constants.endowment * dice_sum
                else:
                    self.restricted_payoff = 0
            elif self.restrictedChoiceFirstOrderDominance == "Lottery 2.2":
                if die1 > 2 and die2 > 2:
                    self.restricted_payoff = Constants.endowment * dice_sum
                else:
                    self.restricted_payoff = 0
            elif self.restrictedChoiceFirstOrderDominance == "Lottery 2.3":
                if die1 < 5 and die2 < 5:
                    self.restricted_payoff = Constants.endowment * dice_sum
                else:
                    self.restricted_payoff = 0
        elif self.restrictedLottery_draw == 3:
            if self.restrictedChoiceSecondOrderDominance == "Lottery 3.1":
                if die1 < 3 or die2 < 3:
                    self.restricted_payoff = dice_sum * Constants.endowment
                else:
                    self.restricted_payoff = 0
            elif self.restrictedChoiceSecondOrderDominance == "Lottery 3.2":
                if die1 < 3 or die2 < 3:
                    self.restricted_payoff = (dice_sum - die1 + die2) * Constants.endowment
                else:
                    self.restricted_payoff = 0
        elif self.restrictedLottery_draw == 4:
            if self.restrictedChoiceVariableRisk == "Lottery 4.1":
                self.restricted_payoff = Constants.endowment * 1.25
            elif self.restrictedChoiceVariableRisk == "Lottery 4.2":
                if die1 < 3 or die2 < 3:
                    self.restricted_payoff = Constants.endowment * dice_sum
                else:
                    self.restricted_payoff = 0
            elif self.restrictedChoiceVariableRisk == "Lottery 4.3":
                if die1 > 2 and die2 > 2:
                    self.restricted_payoff = Constants.endowment * dice_sum
                else:
                    self.restricted_payoff = 0


    def setTotalPayoffs(self):
        self.payoff = c(self.in_round(1).unrestricted_payoff) + c(self.in_round(self.restricted_payoff_round).restricted_payoff)

        if self.quiz_payoff_bool == True:
            self.payoff = c(self.payoff) + c(Constants.quiz_points*self.test_score)

    #----# FOR LOTTERY (END) #----#
