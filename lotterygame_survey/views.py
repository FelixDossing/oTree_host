from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants



class Risk_instructions(Page):
    pass

class Risk_main(Page):
    form_model = models.Player
    form_fields = ['boxes_opened']

class Disgust_survey1(Page):
    form_model = models.Player
    form_fields = ['disgust{}'.format(i) for i in range(1,15)]

class Disgust_survey2(Page):
    form_model = models.Player
    form_fields = ['disgust{}'.format(i) for i in range(15,28)]

class Paternalism_questions1(Page):
    form_model = models.Player
    form_fields = ['paternalism_question{}'.format(i) for i in range(1,6)]

class Paternalism_questions2(Page):
    form_model = models.Player
    form_fields = ['paternalism_question{}'.format(i) for i in range(6,8)]

class Paternalism_questions3(Page):
    form_model = models.Player
    form_fields = ['paternalism_question{}'.format(i) for i in range(8,10)]

class Paternalism_questions4(Page):
    form_model = models.Player
    form_fields = ['paternalism_question10']

    def paternalism_question10_choices(self):
        return [
            "We should keep the current system, which requires people to sign up if they want to be an organ donor",
            "We should implement a new system, where those who don't want to be an organ donor should resign",
            "Everyone should be an organ donor without the possibility to resign"
        ]
class Ideology(Page):
    form_model = models.Player
    form_fields = ['pol_scale_pos', 'income_equity', 'private_vs_state', 'government_responsibility',
                   'competition', 'hard_work', 'wealth']

    def pol_scale_pos_choices(self):
        scale = ['{}'.format(i) for i in range(2,10)]
        scale.insert(0,Constants.ideology[0]['1'])
        scale.append(Constants.ideology[0]['10'])
        return scale

    def income_equity_choices(self):
        scale = ['{}'.format(i) for i in range(2,10)]
        scale.insert(0,Constants.ideology[1]['1'])
        scale.append(Constants.ideology[1]['10'])
        return scale

    def private_vs_state_choices(self):
        scale = ['{}'.format(i) for i in range(2,10)]
        scale.insert(0,Constants.ideology[2]['1'])
        scale.append(Constants.ideology[2]['10'])
        return scale

    def government_responsibility_choices(self):
        scale = ['{}'.format(i) for i in range(2,10)]
        scale.insert(0,Constants.ideology[3]['1'])
        scale.append(Constants.ideology[3]['10'])
        return scale

    def competition_choices(self):
        scale = ['{}'.format(i) for i in range(2,10)]
        scale.insert(0,Constants.ideology[4]['1'])
        scale.append(Constants.ideology[4]['10'])
        return scale

    def hard_work_choices(self):
        scale = ['{}'.format(i) for i in range(2,10)]
        scale.insert(0,Constants.ideology[5]['1'])
        scale.append(Constants.ideology[5]['10'])
        return scale

    def wealth_choices(self):
        scale = ['{}'.format(i) for i in range(2,10)]
        scale.insert(0,Constants.ideology[6]['1'])
        scale.append(Constants.ideology[6]['10'])
        return scale

    #Højre Venstre
    #Kan markedet allokere ressourcer effektivt
    #33 helping the poor
    #34 work vs luck

class Voting(Page):
    form_model = models.Player
    form_fields = ['vote2015', 'votenow']

    def vote2015_choices(self):
        return [
            "Socialdemokratiet (A)",
            "Radikale Venstre (B)",
            "Det Konservative Folkeparti (C)",
            "SF - Socialistisk Folkeparti (F)",
            "Liberal Alliance (I)",
            "Kristendemokraterne (K)",
            "Dansk Folkeparti (O)",
            "Venstre - Danmarks liberale parti (V)",
            "Enhedslisten - De Rød-Grønne (Ø)",
            "Alternativet (Å)"
            "I chose not to vote",
            "I am not allowed to vote in the Danish general election"
        ]

    def votenow_choices(self):
        return [
            "Socialdemokratiet (A)",
            "Radikale Venstre (B)",
            "Det Konservative Folkeparti (C)",
            "SF - Socialistisk Folkeparti (F)",
            "Liberal Alliance (I)",
            "Kristendemokraterne (K)",
            "Dansk Folkeparti (O)",
            "Venstre - Danmarks liberale parti (V)",
            "Enhedslisten - De Rød-Grønne (Ø)",
            "Alternativet (Å)"
            "I chose not to vote",
            "I am not allowed to vote in the Danish general election"
        ]

class Personality(Page):
    form_model = models.Player
    form_fields = ['personality{}'.format(i) for i in range(1,11)]


class Demographics(Page):
    form_model = models.Player
    form_fields = ['gender','height','weight','birthyear','smoker']

    def gender_choices(self):
        return [
            "Female",
            "Male",
            "Other"
        ]
    def birthyear_choices(self):
        return ["{}".format(i) for i in range(1900,2010)]
    def smoker_choices(self):
        return [
            "are a smoker",
            "are a smoker, but have tried to quit",
            "have been a smoker, but have quit",
            "have never been a smoker"
        ]


    #36 - difficulty handling money, impulsivity and so on



#To be in survey: CR-test, "type-questions"
# Social dominance orientation
# Political orientation Two-dimensional


class Results(Page):
    pass
page_sequence = [
    # Risk_instructions,
    # Risk_main,
    # Disgust_survey1,
    # Disgust_survey2,
    # Paternalism_questions1,
    # Paternalism_questions2,
    # Paternalism_questions3,
    # Paternalism_questions4,
    Ideology,
    # Results,
    # Personality,
    # Voting,
    Demographics
]
