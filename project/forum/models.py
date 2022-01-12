from django.db import models


class Question(models.Model):
    question_title = models.CharField('Вопрос', max_length=200)
    question_text = models.TextField('Описание вопроса')
    question_pub_date = models.DateTimeField('Дата публикации вопроса')


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField('Ответ')
    answer_pub_date = models.DateTimeField('Дата публикации ответа')

# Create your models here.
