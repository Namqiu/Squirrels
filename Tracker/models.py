import re
import datetime
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

def validate_date(value):
    if value > timezone.now().date():
        raise ValidationError("Future date is invalid")
def validate_unique_squirrel_id(value):
    p = re.compile(r'\w{2,3}-[AP]M-\d{4}-\d+')
    if p.match(value) == None:
        raise ValidationError("Unique Squirrel id is invalid")
    

class Squirrel(models.Model):
    longitude = models.FloatField('Longitude') 
    latitude = models.FloatField('Latitude')
    unique_squirrel_id = models.CharField('Unique Squirrel ID',max_length=200,validators=[validate_unique_squirrel_id])
    SHIFT_CHOICES = (('AM', 'AM'),('PM', 'PM'),)
    shift = models.CharField('Shift',max_length=5,choices=SHIFT_CHOICES)
    date = models.DateField('Date', validators=[validate_date])
    age = models.CharField('Age',max_length=50,choices=(('Adult','Adult'),('Juvenile','Juvenile'),),blank=True)
    primary_fur_color = models.CharField('Primary Fur Color',max_length=50, choices=(('Gray','Gray'),('Cinnamon','Cinnamon'),('Black','Black'),),blank=True)
    location = models.CharField('Location',max_length=50,choices=(('Ground Plane','Ground Plane'),('Above Ground','Above Ground'),),blank=True)
    specific_location = models.CharField('Specific Location',max_length=200,blank=True)
    running = models.BooleanField('Running')
    chasing = models.BooleanField('Chasing')
    climbing = models.BooleanField('Climbing')
    eating = models.BooleanField('Eating')
    foraging = models.BooleanField('Foraging')
    other_activities = models.CharField('Other Activities',max_length=200,blank=True)
    kuks = models.BooleanField('Kuks')
    quaas = models.BooleanField('Quaas')
    moans = models.BooleanField('Moans')
    tail_flags = models.BooleanField('Tail flags')
    tail_twitches = models.BooleanField('Tail twitches')
    approaches = models.BooleanField('Approaches')
    indifferent = models.BooleanField('Indifferent')
    runs_from = models.BooleanField('Runs from')

    def __str__(self):
        return self.unique_squirrel_id
    
    def id_match(self):
        id_shift = self.unique_squirrel_id.split('-')[1]
        id_date = self.unique_squirrel_id.split('-')[2]
        id_date_month = int(id_date[:2])
        id_date_day = int(id_date[2:])
        if id_shift == self.shift and id_date_month == self.date.month and id_date_day == self.date.day:
            return True
        else:
            return False






# Create your models here.
