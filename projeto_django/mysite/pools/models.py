from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=255)
    closed = models.BooleanField(default=False)
    pub_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    choice_text = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, related_name='choices', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text
