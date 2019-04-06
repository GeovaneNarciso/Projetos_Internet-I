from django.db import models


class Question:
    def __init__(self, id, question_text, pub_date):
        self.id = id
        self.question_text = question_text
        self.pub_date = pub_date
