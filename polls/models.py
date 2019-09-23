import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


def vote_count(id):
    """
    Return total votes for a given poll. id is poll id
    Args: int
    Return: int
    """
    sum_vote = 0
    quest = Question.objects.get(pk=id)
    choices = quest.choice_set.all()
    for choice in choices:
        sum_vote += choice.votes
    return sum_vote


def find_poll_for_text(text):
    """
    Return list of Question objects for all polls containing some text
    Arg: String
    Return: List ob Question Object
    """
    q = Question.objects.filter(question_text__contains=text)
    return list(q)
