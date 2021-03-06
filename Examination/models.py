from django.db import models
from django.urls import reverse
from Teacher.models import Teacher
from datetime import date, timedelta

# Create your models here.

class Paper(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField()
    multiple_choice_question_total_score = models.FloatField(default=0)
    essay_question_total_score = models.FloatField(default=0)
    publish_date = models.DateField(auto_now=True)
    expire_date = models.DateField(default=date.today() + timedelta(days=30))  # default expire date is 30 days from now on
    is_published = models.BooleanField(default=False)
    paper_maker = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True) 

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('examination:paper_detail', args=[self.id])
    
    def save(self, *args, **kwargs):
        multiple_choice_questions = self.multiple_choice_question_set.all()
        self.multiple_choice_question_total_score = 0
        for question in multiple_choice_questions:
            self.multiple_choice_question_total_score += question.point

        essay_questions = self.essay_question_set.all()
        self.essay_question_total_score = 0
        for question in essay_questions:
            self.essay_question_total_score += question.point

        super().save(*args, **kwargs)  # Call the "real" save() method.
    
    class Meta:
        db_table = 'paper'
        verbose_name = '试卷'
        verbose_name_plural = '试卷'


class Multiple_Choice_Question(models.Model):
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=1000)
    option_A = models.CharField(max_length=1000)
    option_B = models.CharField(max_length=1000)
    option_C = models.CharField(max_length=1000)
    option_D = models.CharField(max_length=1000)
    point = models.FloatField()

    OPTIONS = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'))
    right_answer = models.CharField(max_length=1, choices=OPTIONS, default=None)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the "real" save() method.
        self.paper.save()
    
    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)  # Call the "real" delete() method.
        self.paper.save()

    class Meta:
        db_table = 'multiple_choice_question'
        verbose_name = '选择题'
        verbose_name_plural = '选择题'


class Essay_Question(models.Model):
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE, null=True)
    title = models.TextField()
    right_answer = models.TextField()
    point = models.FloatField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the "real" save() method.
        self.paper.save()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)  # Call the "real" delete() method.
        self.paper.save()

    class Meta:
        db_table = 'essay_question'
        verbose_name = '问答题'
        verbose_name_plural = '问答题'


