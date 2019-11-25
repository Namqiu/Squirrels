import csv
from django.core.management.base import BaseCommand
from Tracker.models import Squirrel

class Command(BaseCommand):
    help = 'export squirrel data'
    def add_arguments(self,parser):
        parser.add_argument('path')

    def handle(self,*args,**options):
        def write_csv(meta):
            f = open(meta['file'], 'w+')
            writer = csv.writer(f)
            writer.writerow( meta['fields'] )
            for obj in meta['class'].objects.all():
                row = [getattr(obj, field) for field in meta['fields']]
                writer.writerow(row)
            f.close()
        path = options['path']
        meta = {
            'file': path,
            'class': Squirrel,
            'fields': ('longitude','latitude','unique_squirrel_id','shift','date','age','primary_fur_color',
                       'location','specific_location','running','chasing','climbing','eating','foraging',
                       'other_activities','kuks','quaas','moans','tail_flags','tail_twitches',
                       'approaches','indifferent','runs_from')
        }   
        write_csv(meta)


