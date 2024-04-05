from django.core.management.base import BaseCommand, CommandError
from StorySphere.models import ForumTopic, User  # Import your ForumTopic and User models

class Command(BaseCommand):
    help = 'Deletes all topics created by the specified user'

    def add_arguments(self, parser):
        parser.add_argument('user_id', type=int, help='User ID to delete topics')

    def handle(self, *args, **options):
        user_id = options['user_id']
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise CommandError(f'User with ID {user_id} does not exist')

        # Delete topics created by the specified user
        ForumTopic.objects.filter(author=user).delete()

        self.stdout.write(self.style.SUCCESS('Successfully deleted topics'))
