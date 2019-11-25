import datetime

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

        f = open(path)
        for line in f:
            data = line.strip().split(',')
            Squirrel.objects.get_or_create(
                    longitude = float(data[0]),
                    latitude = float(data[1]),
                    unique_squirrel_id = data[2],
                    shift = data[4],
                    date = datetime.date(int(data[5][4:]),int(data[5][:2]),int(data[5][2:4])),
                    age = data[7],
                    primary_fur_color = data[8],
                    location = data[12],
                    specific_location = data[14],
                    running = str_to_bool(data[15]),
                    chasing = str_to_bool(data[16]),
                    climbing = str_to_bool(data[17]),
                    eating = str_to_bool(data[18]),
                    foraging = str_to_bool(data[19]),
                    other_activities = data[20],
                    kuks = str_to_bool(data[21]),
                    quaas = str_to_bool(data[22]),
                    moans = str_to_bool(data[23]),
                    tail_flags = str_to_bool(data[24]),
                    tail_twitches = str_to_bool(data[25]),
                    approaches = str_to_bool(data[26]),
                    indifferent = str_to_bool(data[27]),
                    runs_from = str_to_bool(data[28]),
                    )
        f.close()
