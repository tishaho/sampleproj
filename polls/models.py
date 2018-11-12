from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=100)            #max_length is required, CharField is varchar in database
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return 'Question: {}'.format(self.question_text)


class Choice(models.Model):                                     #classes should be separated with a new line for readability
    question = models.ForeignKey(Question,
                on_delete=models.CASCADE,                       #on_delete is constant
                related_name='choices')
    choice_text = models.CharField(max_length=200)              #CharField is character character field
    votes = models.IntegerField(default=0)                      #default parameter is optional, can put it in any parameter
