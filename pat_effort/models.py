from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import itertools, csv, random
author = 'Felix Sebastian Doessing'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'egame1'
    players_per_group = 2
    num_rounds = 4

    number_of_choices = 4
    point_conversion = 0.25
    worktime_minutes = 10

    with open ('pat_effort/commit_choices.csv') as csvfile:
        commitChoices = list(csv.DictReader(csvfile))
    with open ('pat_effort/paternalee_choices.csv') as csvfile:
        paternaleeChoices = list(csv.DictReader(csvfile))

class Subsession(BaseSubsession):

    num_players = models.IntegerField()

    def creating_session(self):

        self.num_players = len(self.get_players())

        if self.round_number == 1:
            for i in range(0,self.num_players):
                self.get_players()[i].player_id = str(i+1)
        else:
            for i in range(0,self.num_players):
                self.get_players()[i].player_id = self.get_players()[i].in_round(1).player_id

        self.group_randomly(fixed_id_in_group = True)

        ## Make sure partner is always new
        if self.num_players >= 8:
            if self.round_number == 1:
                self.session.vars['group_matrix1'] = self.get_group_matrix()
            elif self.round_number > 1:
                done = False
                while done == False:
                    count = 0
                    for i in range(1, self.round_number):
                        for j in self.session.vars['group_matrix{}'.format(str(i))]:
                            for h in self.get_group_matrix():
                                ## Man kan ikke bare sammenligne disse lister...
                                if j[0].player_id == h[0].player_id and j[1].player_id == h[1].player_id:
                                    count = 1
                    if count > 0:
                        self.group_randomly(fixed_id_in_group = True)
                    else:
                        done = True
                        self.session.vars['group_matrix{}'.format(str(i+1))] = self.get_group_matrix()

        ## Set partner_id
        for p in self.get_players():
            p.partner_id = p.get_others_in_group()[0].player_id


class Group(BaseGroup):

    def handleImplementation(self):
        for p in self.get_players():

            p.random1 = random.randint(1,2)
            p.random2 = random.randint(1,4)
            p.random_prob = random.random()

            p.partner_choice = p.get_others_in_group()[0].decisionForPartner

            p.commit_decision1 = p.commit_decision1 * 0.01
            p.commit_decision2 = p.commit_decision2 * 0.01
            p.commit_decision3 = p.commit_decision3 * 0.01
            p.commit_decision4 = p.commit_decision4 * 0.01
            p.paternalee_decision1 = p.paternalee_decision1 * 0.01
            p.paternalee_decision2 = p.paternalee_decision2 * 0.01
            p.paternalee_decision3 = p.paternalee_decision3 * 0.01
            p.paternalee_decision4 = p.paternalee_decision4 * 0.01

            if p.random1 == 1:
                if p.random2 == 1:
                    p.choice11_implemented = True
                    if p.random_prob <= p.commit_decision1:
                        p.button_present = False
                elif p.random2 == 2:
                    p.choice12_implemented = True
                    if p.random_prob <= p.commit_decision2:
                        p.button_present = False
                elif p.random2 == 3:
                    p.choice13_implemented = True
                    if p.random_prob <= p.commit_decision3:
                        p.button_present = False
                elif p.random2 == 4:
                    p.choice14_implemented = True
                    if p.random_prob <= p.commit_decision4:
                        p.button_present = False
            else:
                if p.random2 == 1:
                    p.choice21_implemented = True
                    if p.random_prob <= p.paternalee_decision1:
                        p.partner_given_choice = True
                        if p.get_others_in_group()[0].decisionForPartner == True:
                            p.button_present = False
                elif p.random2 == 2:
                    p.choice22_implemented = True
                    if p.random_prob <= p.paternalee_decision2:
                        p.partner_given_choice = True
                        if p.get_others_in_group()[0].decisionForPartner == True:
                            p.button_present = False
                elif p.random2 == 3:
                    p.choice23_implemented = True
                    if p.random_prob <= p.paternalee_decision3:
                        p.partner_given_choice = True
                        if p.get_others_in_group()[0].decisionForPartner == True:
                            p.button_present = False
                elif p.random2 == 4:
                    p.choice24_implemented = True
                    if p.random_prob <= p.paternalee_decision4:
                        p.partner_given_choice = True
                        if p.get_others_in_group()[0].decisionForPartner == True:
                            p.button_present = False

            ## Set costs
            if p.choice11_implemented == True:
                for i in Constants.commitChoices[:9]:
                    if i['pct'] == str(int(p.commit_decision1*100)):
                        p.choice_cost = int(i['cost'])
            elif p.choice12_implemented == True:
                for i in Constants.commitChoices[9:18]:
                    if i['pct'] == str(int(p.commit_decision2*100)):
                        p.choice_cost = int(i['cost'])
            elif p.choice13_implemented == True:
                for i in Constants.commitChoices[18:27]:
                    if i['pct'] == str(int(p.commit_decision3*100)):
                        p.choice_cost = int(i['cost'])
            elif p.choice14_implemented == True:
                for i in Constants.commitChoices[27:36]:
                    if i['pct'] == str(int(p.commit_decision4*100)):
                        p.choice_cost = int(i['cost'])
            elif p.choice21_implemented == True:
                for i in Constants.paternaleeChoices[:9]:
                    if i['pct'] == str(int(p.paternalee_decision1*100)):
                        p.choice_cost = int(i['cost'])
            elif p.choice22_implemented == True:
                for i in Constants.paternaleeChoices[9:18]:
                    if i['pct'] == str(int(p.paternalee_decision2*100)):
                        p.choice_cost = int(i['cost'])
            elif p.choice23_implemented == True:
                for i in Constants.paternaleeChoices[18:27]:
                    if i['pct'] == str(int(p.paternalee_decision3*100)):
                        p.choice_cost = int(i['cost'])
            elif p.choice24_implemented == True:
                for i in Constants.paternaleeChoices[27:36]:
                    if i['pct'] == str(int(p.paternalee_decision4*100)):
                        p.choice_cost = int(i['cost'])

    def calculatePayoffs(self):
        for p in self.get_players():
            p.payoff = p.tasksCompleted - p.choice_cost
            p.accumulated_payoff = sum([q.payoff for q in p.in_all_rounds()])



class Player(BasePlayer):

    partner_id = models.CharField()
    player_id = models.CharField()

    choice_cost = models.IntegerField(initial=0)

    accumulated_payoff = models.IntegerField(initial=0)

    random1 = models.IntegerField()
    random2 = models.IntegerField()
    random_prob = models.FloatField()

    partner_choice = models.BooleanField() ##The choice that the partner made
    partner_given_choice = models.BooleanField(initial=False)

    choice11_implemented = models.BooleanField(initial=False)
    choice12_implemented = models.BooleanField(initial=False)
    choice13_implemented = models.BooleanField(initial=False)
    choice14_implemented = models.BooleanField(initial=False)
    choice21_implemented = models.BooleanField(initial=False)
    choice22_implemented = models.BooleanField(initial=False)
    choice23_implemented = models.BooleanField(initial=False)
    choice24_implemented = models.BooleanField(initial=False)

    button_present = models.BooleanField(initial=True)

    tasksCompleted_trial = models.IntegerField()
    tasksCompleted = models.IntegerField()

    commit_decision1 = models.FloatField(
        choices=[10,20,30,40,50,60,70,80,90],
        widget=widgets.RadioSelectHorizontal
    )
    commit_decision2 = models.FloatField(
        choices=[10,20,30,40,50,60,70,80,90],
        widget=widgets.RadioSelectHorizontal
    )
    commit_decision3 = models.FloatField(
        choices=[10,20,30,40,50,60,70,80,90],
        widget=widgets.RadioSelectHorizontal
    )
    commit_decision4 = models.FloatField(
        choices=[10,20,30,40,50,60,70,80,90],
        widget=widgets.RadioSelectHorizontal
    )

    paternalee_decision1 = models.FloatField(
        choices=[10,20,30,40,50,60,70,80,90],
        widget=widgets.RadioSelectHorizontal
    )
    paternalee_decision2 = models.FloatField(
        choices=[10,20,30,40,50,60,70,80,90],
        widget=widgets.RadioSelectHorizontal
    )
    paternalee_decision3 = models.FloatField(
        choices=[10,20,30,40,50,60,70,80,90],
        widget=widgets.RadioSelectHorizontal
    )
    paternalee_decision4 = models.FloatField(
        choices=[10,20,30,40,50,60,70,80,90],
        widget=widgets.RadioSelectHorizontal
    )

    decisionForPartner = models.BooleanField()

    partner_belief = models.IntegerField(
        choices=[0,10,20,30,40,50,60,70,80,90,100],
        widget=widgets.RadioSelectHorizontal
    )

    def role(self):
        if self.round_number % 2 != 0: #is uneven
            if self.id_in_group == 1:
                return 'commit_first'
            elif self.id_in_group == 2:
                return 'paternalee_first'
        else:
            if self.id_in_group == 1:
                return 'paternalee_first'
            elif self.id_in_group == 2:
                return 'commit_first'
