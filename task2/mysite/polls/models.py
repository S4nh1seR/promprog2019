from django.db import models
from django.forms import ModelForm

class Question(models.Model):
    question_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']
