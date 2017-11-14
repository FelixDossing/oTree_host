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
    name_in_url = 'lgame1'
    players_per_group = 2
    num_rounds = 1

    minutes_for_quiz = 30

    with open('lotterygame/probability_quiz.csv') as q:
        questions = list(csv.DictReader(q))

    with open('lotterygame/lotteries.csv') as g:
        lotteries = list(csv.DictReader(g))


    num_questions = len(questions)

    points_per_lottery = 10
    quiz_points = 1 # Points for each correct answer in the quiz (if points are given for quiz answers

    # Conversion rate: 1 point = 4 DKK

    lottery1_return_high_likely = 6
    lottery1_return_high_unlikely = 12
    lottery1_return_low_likely = 1.5
    lottery1_return_low_unlikely = 3

    lottery2_return_high_likely = 6
    lottery2_return_high_unlikely = 12
    lottery2_return_low_likely = 1.5
    lottery2_return_low_unlikely = 3

    lottery1_prob_likely = 1/3
    lottery1_prob_unlikely = 1/6

    lottery2_prob_likely = 1/3
    lottery2_prob_unlikely = 1/6

    endowment = c(10)


class Subsession(BaseSubsession):

    num_players = models.IntegerField()
    total_score = models.IntegerField()
    average_score = models.FloatField()

    quiz_payoff_draw = models.IntegerField()

    def before_session_starts(self):

        self.num_players = len(self.get_players())

        self.group_randomly()
        self.session.vars['questions'] = Constants.questions
        self.session.vars['lotteries'] = Constants.lotteries

        self.session.vars['likert'] = ['Strongly disagree', 'Disagree', 'Neither agree nor disagree', 'Agree', 'Strongly agree']

        self.quiz_payoff_draw = random.randint(1, self.num_players)

        self.session.vars['free_choice_draws'] = random.sample(range(int(self.num_players/2)),int(self.num_players/4))
        # self.free_choice_draw = random.randint(1, self.num_players/2)


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

        # treat = itertools.cycle(['partner','self','full'])
        treat = itertools.cycle(['partner', 'full', 'full'])

        group_id_list = []
        for i in range(0,int(self.num_players/2)):
            group_id_list.append(i)

        group_id_list = itertools.cycle(group_id_list)
        lottery_data = self.session.vars['lotteries']

        for g in self.get_groups():
            g.treatment = next(treat)
            g.group_id = next(group_id_list)

            g.lottery1_returntype = 'high' if random.random() > 0.5 else 'low'
            g.lottery1_likelyhood = 'likely' if random.random() > 0.5 else 'unlikely'
            g.lottery2_returntype = 'high' if random.random() > 0.5 else 'low'
            g.lottery2_likelyhood = 'likely' if random.random() > 0.5 else 'unlikely'

            for p in g.get_players():
                if g.lottery1_returntype == 'high':
                    p.lottery1 = lottery_data[0]['high_likely'] if g.lottery1_likelyhood == 'likely' else lottery_data[0]['high_unlikely']
                elif g.lottery1_returntype == 'low':
                    p.lottery1 = lottery_data[0]['low_likely'] if g.lottery1_likelyhood == 'likely' else lottery_data[0]['low_unlikely']

                if g.lottery2_returntype == 'high':
                    p.lottery2 = lottery_data[1]['high_likely'] if g.lottery2_likelyhood == 'likely' else lottery_data[1]['high_unlikely']
                elif g.lottery2_returntype == 'low':
                    p.lottery2 = lottery_data[1]['low_likely'] if g.lottery2_likelyhood == 'likely' else lottery_data[1]['low_unlikely']


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

class Group(BaseGroup):

    treatment = models.CharField()

    group_id = models.IntegerField()

    lottery1_returntype = models.CharField()
    lottery1_likelyhood = models.CharField()

    lottery2_returntype = models.CharField()
    lottery2_likelyhood = models.CharField()

    lottery1_outcome = models.IntegerField()
    lottery2_outcome = models.IntegerField()

    # Setting up decision part
    lev_gamble1 = models.IntegerField( #Represents the restriction of the leviathan
        initial = 0,
        widget=widgets.SliderInput(attrs={'min':str(-10),
                                          'max':str(10)})
    )
    lev_gamble2 = models.IntegerField(
        initial = 0,
        widget=widgets.SliderInput(attrs={'min':str(-10),
                                          'max':str(10)})
    )

    gam_gamble1 = models.CurrencyField(initial=0) # Represents the restricted gamble choice of the gambler
    gam_gamble2 = models.CurrencyField(initial=0)

    def set_gambles(self):
        if self.lottery1_likelyhood == 'likely':
            self.lottery1_outcome = 1 if random.random() <= Constants.lottery1_prob_likely else 0
        else:
            self.lottery1_outcome = 1 if random.random() <= Constants.lottery1_prob_unlikely else 0
        if self.lottery2_likelyhood == 'likely':
            self.lottery2_outcome = 1 if random.random() <= Constants.lottery2_prob_likely else 0
        else:
            self.lottery2_outcome = 1 if random.random() <= Constants.lottery2_prob_unlikely else 0

        ## Make conditional on high/low lottery
    def set_payoffs(self):
        gambler = self.get_player_by_role('Gambler')

        def payoffcalc_lottery1(self, gamble, returnvalue):
            gambler.payoff_lottery1 = Constants.points_per_lottery - gamble +\
                                      (self.lottery1_outcome * gamble * returnvalue)

        def payoffcalc_lottery2(self, gamble, returnvalue):
            gambler.payoff_lottery2 = Constants.points_per_lottery - gamble +\
                                      (self.lottery2_outcome * gamble * returnvalue)

        if gambler.restricted_choice == True:
            ## Lottery 1
            if self.lottery1_returntype == 'high':
                if self.lottery1_likelyhood == 'likely':
                    payoffcalc_lottery1(self, self.gam_gamble1, Constants.lottery1_return_high_likely)
                else:
                    payoffcalc_lottery1(self, self.gam_gamble1, Constants.lottery1_return_high_unlikely)
            else:
                if self.lottery1_likelyhood == 'likely':
                    payoffcalc_lottery1(self,self.gam_gamble1, Constants.lottery1_return_low_likely)
                else:
                    payoffcalc_lottery1(self,self.gam_gamble1, Constants.lottery1_return_low_unlikely)
            ## Lottery 2
            if self.lottery2_returntype == 'high':
                if self.lottery2_likelyhood == 'likely':
                    payoffcalc_lottery2(self, self.gam_gamble2, Constants.lottery2_return_high_likely)
                else:
                    payoffcalc_lottery2(self, self.gam_gamble2, Constants.lottery2_return_high_unlikely)
            else:
                if self.lottery2_likelyhood == 'likely':
                    payoffcalc_lottery2(self,self.gam_gamble2, Constants.lottery2_return_low_likely)
                else:
                    payoffcalc_lottery2(self,self.gam_gamble2, Constants.lottery2_return_low_unlikely)

        # Free choice
        elif gambler.restricted_choice == False:
            ## Lottery 1
            if self.lottery1_returntype == 'high':
                if self.lottery1_likelyhood == 'likely':
                    payoffcalc_lottery1(self, gambler.gam_gamble_free1, Constants.lottery1_return_high_likely)
                else:
                    payoffcalc_lottery1(self, gambler.gam_gamble_free1, Constants.lottery1_return_high_unlikely)
            else:
                if self.lottery1_likelyhood == 'likely':
                    payoffcalc_lottery1(self, gambler.gam_gamble_free1, Constants.lottery1_return_low_likely)
                else:
                    payoffcalc_lottery1(self, gambler.gam_gamble_free1, Constants.lottery1_return_low_unlikely)
            ## Lottery 2
            if self.lottery2_returntype == 'high':
                if self.lottery2_likelyhood == 'likely':
                    payoffcalc_lottery2(self, gambler.gam_gamble_free2, Constants.lottery2_return_high_likely)
                else:
                    payoffcalc_lottery2(self, gambler.gam_gamble_free2, Constants.lottery2_return_high_unlikely)
            else:
                if self.lottery2_likelyhood == 'likely':
                    payoffcalc_lottery2(self, gambler.gam_gamble_free2, Constants.lottery2_return_low_likely)
                else:
                    payoffcalc_lottery2(self, gambler.gam_gamble_free2, Constants.lottery2_return_low_unlikely)

        gambler.payoff = gambler.payoff_lottery1 + gambler.payoff_lottery2

        if gambler.quiz_payoff_bool == True:
            gambler.payoff_quiz = gambler.test_score * Constants.quiz_points
            gambler.payoff += gambler.payoff_quiz


        leviathan = self.get_player_by_role('Leviathan')
        leviathan.payoff_lottery1 = 0
        leviathan.payoff_lottery2 = 0

        if leviathan.quiz_payoff_bool == True:
            leviathan.payoff_quiz = leviathan.test_score * Constants.quiz_points
            leviathan.payoff += leviathan.payoff_quiz

        def payoffcalclev_lottery1(self, gamble, returnvalue):
            leviathan.payoff_lottery1 = Constants.points_per_lottery - gamble +\
                                      (self.lottery1_outcome * gamble * returnvalue)

        def payoffcalclev_lottery2(self, gamble, returnvalue):
            leviathan.payoff_lottery2 = Constants.points_per_lottery - gamble +\
                                      (self.lottery2_outcome * gamble * returnvalue)


        if leviathan.leviathan_gamble_bool == True:
            if self.lottery1_returntype == 'high':
                if self.lottery1_likelyhood == 'likely':
                    payoffcalclev_lottery1(self, leviathan.lev_gamble1_own, Constants.lottery1_return_high_likely)
                else:
                    payoffcalclev_lottery1(self, leviathan.lev_gamble1_own, Constants.lottery1_return_high_unlikely)
            else:
                if self.lottery1_likelyhood == 'likely':
                    payoffcalclev_lottery1(self, leviathan.lev_gamble1_own, Constants.lottery1_return_low_likely)
                else:
                    payoffcalclev_lottery1(self, leviathan.lev_gamble1_own, Constants.lottery1_return_low_unlikely)

            if self.lottery2_returntype == 'high':
                if self.lottery1_likelyhood == 'likely':
                    payoffcalclev_lottery2(self, leviathan.lev_gamble2_own, Constants.lottery2_return_high_likely)
                else:
                    payoffcalclev_lottery2(self, leviathan.lev_gamble2_own, Constants.lottery2_return_high_unlikely)
            else:
                if self.lottery2_likelyhood == 'likely':
                    payoffcalclev_lottery2(self, leviathan.lev_gamble2_own, Constants.lottery2_return_low_likely)
                else:
                    payoffcalclev_lottery2(self, leviathan.lev_gamble2_own, Constants.lottery2_return_low_unlikely)

        leviathan.payoff = Constants.leviathanfee + Constants.showupfee + leviathan.payoff_lottery1 + leviathan.payoff_lottery2

        if leviathan.quiz_payoff_bool == True:
            leviathan.payoff_quiz = leviathan.test_score * Constants.quiz_points
            leviathan.payoff += leviathan.payoff_quiz

class Player(BasePlayer):

    ### Setting up roles ###
    def role(self):
        if self.id_in_group == 1:
            return 'Gambler'
        if self.id_in_group == 2:
            return 'Leviathan'

    ### Setting up probability test ###
    lev_instr = models.IntegerField(
        initial = 0,
        widget = widgets.SliderInput(attrs={'min':str(-10),
                                            'max':str(10)})
    )

    control1 = models.IntegerField()
    control2 = models.IntegerField()
    control3 = models.IntegerField()
    control4 = models.IntegerField()
    control5 = models.IntegerField()
    control6 = models.IntegerField()
    control7 = models.IntegerField() # How many got more
    control8 = models.IntegerField() # How many got less
    control9 = models.IntegerField() # How many got the same
    control10 = models.BooleanField() # Was the orange players score above average
    control11 = models.BooleanField() # The Orange player got a better score than the blue player
    control12 = models.BooleanField() # The Orange player got the second-worst score among all players

    # control1 = models.IntegerField(initial=10)
    # control2 = models.IntegerField(initial=7)
    # control3 = models.IntegerField(initial=7)
    # control4 = models.IntegerField(initial=0)
    # control5 = models.IntegerField(initial=10)
    # control6 = models.IntegerField(initial=0)
    # control7 = models.IntegerField(initial=10) # How many got more
    # control8 = models.IntegerField(initial=14) # How many got less
    # control9 = models.IntegerField(initial=5) # How many got the same
    # control10 = models.BooleanField(initial=True) # Was the orange players score above average
    # control11 = models.BooleanField(initial=False) # The Orange player got a better score than the blue player
    # control12 = models.BooleanField(initial=False) # The Orange player got the second-worst score among all players

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

    lottery1 = models.CharField()
    lottery2 = models.CharField()

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
    # submitted_answer11 = models.CharField(initial = "20%", widget=widgets.RadioSelect())
    # submitted_answer12 = models.CharField(initial = "12.8%", widget=widgets.RadioSelect())
    # submitted_answer13 = models.CharField(initial = "1/4", widget=widgets.RadioSelect())
    # submitted_answer14 = models.CharField(initial = "About 15%", widget=widgets.RadioSelect())
    # submitted_answer15 = models.CharField(initial = "65%", widget=widgets.RadioSelect())
    # submitted_answer16 = models.CharField(initial = "17.25 points", widget=widgets.RadioSelect())
    # submitted_answer17 = models.CharField(initial = "25%", widget=widgets.RadioSelect())
    # submitted_answer18 = models.CharField(initial = "1/10000", widget=widgets.RadioSelect())
    # submitted_answer19 = models.CharField(initial = "20/50", widget=widgets.RadioSelect())
    # submitted_answer20 = models.CharField(initial = "100%", widget=widgets.RadioSelect())


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
        self.submitted_answer19 = "19/60" if random.random() > 0.5 else "1/2"
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

    def get_partner_score(self):
        self.partner_test_score = self.get_others_in_group()[0].test_score

    score_guess = models.IntegerField()


    gam_gamble_free1 = models.CurrencyField(initial=0,
                                            choices=currency_range(0, 10, c(1)))
    gam_gamble_free2 = models.CurrencyField(initial=0,
                                            choices=currency_range(0, 10, c(1)))

    lev_gamble1_own = models.CurrencyField(initial=0,
                                            choices=currency_range(0, 10, c(1))) #Represents the hypothetical unrestricted gambling choice of the leviathan
    lev_gamble2_own = models.CurrencyField(initial=0,
                                            choices=currency_range(0, 10, c(1)))

    lev_gamble1_evaluation = models.BooleanField()
    lev_gamble2_evaluation = models.BooleanField()

    quiz_payoff_bool = models.BooleanField() # Boolean true if player recieves payoff from quiz
    restricted_choice = models.BooleanField(initial=True) # Boolean true if payoff is determined by restricted choice (for gamblers)
    leviathan_gamble_bool = models.BooleanField(initial=False) # Boolean true if leviathan recieves payoff from gamble

    outcome_happiness = models.CharField(widget=widgets.RadioSelectHorizontal())
    restriction_happiness = models.CharField(widget=widgets.RadioSelectHorizontal())

    payoff_lottery1 = models.CurrencyField()
    payoff_lottery2 = models.CurrencyField()
    payoff_quiz = models.CurrencyField(initial=0)

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
