from django.db import models

# Create your models here.

class Rating(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=1000)
    edu = models.CharField(max_length=1000)
    expertise = models.CharField(max_length=1000)
    religion = models.CharField(max_length=1000)
    race = models.CharField(max_length=1000)
    marriage = models.CharField(max_length=1000)
    grow_city = models.CharField(max_length=1000)
    grow_town = models.CharField(max_length=1000)
    fill_time = models.DateField()
    fill_city = models.CharField(max_length=1000)
    fill_town = models.CharField(max_length=1000)
    whatIsWisdom = models.CharField(max_length=1000)
    is_wisdom1 = models.IntegerField()
    most_wisdom = models.CharField(max_length=1000)
    most_wisdom_year = models.IntegerField()
    most_wisdom_old = models.IntegerField()
    most_wisdom_period = models.IntegerField()
    special = models.CharField(max_length=1000)
    wisdom_perform = models.IntegerField()
    think = models.CharField(max_length=1000)
    idea = models.IntegerField()
    postiveEffect = models.IntegerField()
    who_postiveEffect = models.IntegerField()
    what_postiveEffect = models.IntegerField()
    think_period = models.IntegerField()
    is_wisdom2 = models.IntegerField()
    why_wisdom = models.CharField(max_length=1000)
    realize = models.IntegerField()
    why_realize = models.CharField(max_length=1000)
    IP_addr = models.CharField(max_length=16)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.age) + ' ' + self.gender + self.expertise

class Option(models.Model):
    name = models.CharField(max_length=1000) #Think_element, behavior_element, wisdom_difficulty, wisdom_conquer, recall_element, postiveEffect_element
    content = models.CharField(max_length=1000)
    which = models.ForeignKey(Rating, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name + ' ' + self.content
