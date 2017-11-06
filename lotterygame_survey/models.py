from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import csv

author = 'Felix Sebastian Dossing'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'patsurvey'
    players_per_group = None
    num_rounds = 1

    number_of_surveys = 3

    with open('lotterygame_survey/disgust_questions.csv') as q:
        disgust = list(csv.DictReader(q))

    with open('lotterygame_survey/paternalism_questions.csv') as q:
        paternalism = list(csv.DictReader(q))

    with open('lotterygame_survey/personality.csv') as q:
        personality = list(csv.DictReader(q))

    with open('lotterygame_survey/ideology.csv') as q:
        ideology = list(csv.DictReader(q))

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    disgust1 = models.CharField(help_text=Constants.disgust[0]['question'])
    disgust2 = models.CharField(help_text=Constants.disgust[1]['question'])
    disgust3 = models.CharField(help_text=Constants.disgust[2]['question'])
    disgust4 = models.CharField(help_text=Constants.disgust[3]['question'])
    disgust5 = models.CharField(help_text=Constants.disgust[4]['question'])
    disgust6 = models.CharField(help_text=Constants.disgust[5]['question'])
    disgust7 = models.CharField(help_text=Constants.disgust[6]['question'])
    disgust8 = models.CharField(help_text=Constants.disgust[7]['question'])
    disgust9 = models.CharField(help_text=Constants.disgust[8]['question'])
    disgust10 = models.CharField(help_text=Constants.disgust[9]['question'])
    disgust11 = models.CharField(help_text=Constants.disgust[10]['question'])
    disgust12 = models.CharField(help_text=Constants.disgust[11]['question'])
    disgust13 = models.CharField(help_text=Constants.disgust[12]['question'])
    disgust14 = models.CharField(help_text=Constants.disgust[13]['question'])

    disgust15 = models.CharField(help_text=Constants.disgust[14]['question'])
    disgust16 = models.CharField(help_text=Constants.disgust[15]['question'])
    disgust17 = models.CharField(help_text=Constants.disgust[16]['question'])
    disgust18 = models.CharField(help_text=Constants.disgust[17]['question'])
    disgust19 = models.CharField(help_text=Constants.disgust[18]['question'])
    disgust20 = models.CharField(help_text=Constants.disgust[19]['question'])
    disgust21 = models.CharField(help_text=Constants.disgust[20]['question'])
    disgust22 = models.CharField(help_text=Constants.disgust[21]['question'])
    disgust23 = models.CharField(help_text=Constants.disgust[22]['question'])
    disgust24 = models.CharField(help_text=Constants.disgust[23]['question'])
    disgust25 = models.CharField(help_text=Constants.disgust[24]['question'])
    disgust26 = models.CharField(help_text=Constants.disgust[25]['question'])
    disgust27 = models.CharField(help_text=Constants.disgust[26]['question'])

    boxes_opened = models.IntegerField()

    paternalism_question1 = models.CharField(help_text=Constants.paternalism[0]['question'])
    paternalism_question2 = models.CharField(help_text=Constants.paternalism[1]['question'])
    paternalism_question3 = models.CharField(help_text=Constants.paternalism[2]['question'])
    paternalism_question4 = models.CharField(help_text=Constants.paternalism[3]['question'])
    paternalism_question5 = models.CharField(help_text=Constants.paternalism[4]['question'])
    paternalism_question6 = models.CharField(help_text=Constants.paternalism[5]['question'])
    paternalism_question7 = models.CharField(help_text=Constants.paternalism[6]['question'])
    paternalism_question8 = models.CharField(help_text=Constants.paternalism[7]['question'])
    paternalism_question9 = models.CharField(help_text=Constants.paternalism[8]['question'])

    paternalism_question10 = models.CharField(widget=widgets.RadioSelect())

    personality1 = models.CharField(help_text=Constants.personality[0]['question'])
    personality2 = models.CharField(help_text=Constants.personality[1]['question'])
    personality3 = models.CharField(help_text=Constants.personality[2]['question'])
    personality4 = models.CharField(help_text=Constants.personality[3]['question'])
    personality5 = models.CharField(help_text=Constants.personality[4]['question'])
    personality6 = models.CharField(help_text=Constants.personality[5]['question'])
    personality7 = models.CharField(help_text=Constants.personality[6]['question'])
    personality8 = models.CharField(help_text=Constants.personality[7]['question'])
    personality9 = models.CharField(help_text=Constants.personality[8]['question'])
    personality10 = models.CharField(help_text=Constants.personality[9]['question'])

    pol_scale_pos = models.CharField(verbose_name=Constants.ideology[0]['introduction'],
                                     widget=widgets.RadioSelect())
    income_equity = models.CharField(verbose_name=Constants.ideology[1]['introduction'],
                                     widget=widgets.RadioSelect())
    private_vs_state = models.CharField(verbose_name=Constants.ideology[2]['introduction'],
                                     widget=widgets.RadioSelect())
    government_responsibility = models.CharField(verbose_name=Constants.ideology[3]['introduction'],
                                     widget=widgets.RadioSelect())
    competition = models.CharField(verbose_name=Constants.ideology[4]['introduction'],
                                     widget=widgets.RadioSelect())
    hard_work = models.CharField(verbose_name=Constants.ideology[5]['introduction'],
                                     widget=widgets.RadioSelect())
    wealth = models.CharField(verbose_name=Constants.ideology[6]['introduction'],
                                     widget=widgets.RadioSelect())

    #Ideology
    #Belief in science
    #Democracy


    vote2015 = models.CharField(widget=widgets.RadioSelect())
    votenow = models.CharField(widget=widgets.RadioSelect())

    gender = models.CharField(widget=widgets.RadioSelect())
    height = models.IntegerField(min=0, max=300)
    weight = models.IntegerField(min=0, max=300)
    birthyear = models.CharField()
    smoker = models.CharField(widget=widgets.RadioSelect())
    zipcode = models.IntegerField(min=0, max=9999)
