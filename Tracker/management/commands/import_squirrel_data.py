import datetime
import csv

from django.core.management.base import BaseCommand

from Tracker.models import Squirrel

class Command(BaseCommand):
    help = 'import squirrel data'

    def add_arguments(self,parser):
        parser.add_argument('path')
        
    def handle(self,*args,**options):

        def str_to_bool(str):
            if str.lower() == 'true':
                return True
            else:
                return False

        path = options['path'] 

        with open(path) as fp:
            reader = csv.DictReader(fp)
            datas = list(reader)

        for data in datas:
            s = Squirrel(
                    longitude = float(data['X']),
                    latitude = float(data['Y']),
                    unique_squirrel_id = data['Unique Squirrel ID'],
                    shift = data['Shift'],
                    date = datetime.date(int(data['Date'][4:]),int(data['Date'][:2]),int(data['Date'][2:4])),
                    age = data['Age'],
                    primary_fur_color = data['Primary Fur Color'],
                    location = data['Location'],
                    specific_location = data['Specific Location'],
                    running = str_to_bool(data['Running']),
                    chasing = str_to_bool(data['Chasing']),
                    climbing = str_to_bool(data['Climbing']),
                    eating = str_to_bool(data['Eating']),
                    foraging = str_to_bool(data['Foraging']),
                    other_activities = data['Other Activities'],
                    kuks = str_to_bool(data['Kuks']),
                    quaas = str_to_bool(data['Quaas']),
                    moans = str_to_bool(data['Moans']),
                    tail_flags = str_to_bool(data['Tail flags']),
                    tail_twitches = str_to_bool(data['Tail twitches']),
                    approaches = str_to_bool(data['Approaches']),
                    indifferent = str_to_bool(data['Indifferent']),
                    runs_from = str_to_bool(data['Runs from']),
                    )
            s.save()

