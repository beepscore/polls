import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return (now - datetime.timedelta(days=1)) <= self.pub_date <= now

    # assign attribute admin_order_field to method was_published_recently
    # http://blog.lerner.co.il/python-attributes/
    was_published_recently.admin_order_field = 'pub_date'
    # change displayed value from words 'True' or 'False' to
    # symbols green circle with checkmark or red circle with -
    was_published_recently.boolean = True
    # column heading
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
