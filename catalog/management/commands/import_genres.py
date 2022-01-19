from django.core.management.base import BaseCommand, CommandError
from catalog.models import Genre


class Command(BaseCommand):
    help = 'Imports Genres found in genres.txt'

    def handle(self, *args, **options):
        try:
            with open('genres.txt', 'r') as genres_f:
                for genre_name in genres_f.readlines():
                    g1 = Genre.objects.create(name=genre_name.strip('\n'))
                    self.stdout.write(self.style.SUCCESS(f"Genre '{g1.name}' added."))

        except Exception as e:
            self.stdout.write(self.style.ERROR(e))
            raise CommandError('An error occurred. Please fix and try again.')

        self.stdout.write(self.style.SUCCESS('Successfully imported genres'))
