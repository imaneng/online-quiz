from django.db import models
from django.db.models.fields import CharField

class MyUser (models.Model):
    name = models.CharField(max_length=100,verbose_name='نام شرکت کننده')
    email = models.EmailField(unique=True,verbose_name='ایمیل شرکت کننده')
    phone_number = models.CharField(max_length=11,blank=False, verbose_name='تلفن شرکت کننده')


    def __str__(self) -> str:
        return self.name


class Question(models.Model):
    CATEGORY_CHOICES = [
        ('A','فرهنگی'),
        ('B','اجتماعی'),
        ('C','سیاسی'),
        ('D','اقتصادی'),
        ('E','ورزشی')
    
    ]
    s_question = models.CharField(max_length=500, verbose_name='سواfilterل')
    category = models.CharField(max_length=5, verbose_name='گروه سوالات', choices=CATEGORY_CHOICES)


    def __str__(self) -> str:
        return self.s_question


class Answer(models.Model):
    ANSWER_CHOICES = [
        ('A','A'),
        ('B','B'),
        ('C','C'),
        ('D','D')
    ]

    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    option_a = models.CharField(max_length=500,blank=False,null=False,verbose_name='Option A')
    option_b = models.CharField(max_length=500,blank=False,null=False,verbose_name='Option B')
    option_c = models.CharField(max_length=500,blank=False,null=False,verbose_name='Option C')
    option_d = models.CharField(max_length=500,blank=False,null=False,verbose_name='Option D')
    correct_answer = models.CharField(max_length=2,blank=False,null=False,choices= ANSWER_CHOICES)


    def __str__(self) -> str:
        return self.question.s_question



class UserAnswer(models.Model):
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    question_no = models.CharField(max_length=500,null=True)
    answer = models.CharField(max_length=1, null=True, blank=True)


    def __str__(self) -> str:
        return self.user.name