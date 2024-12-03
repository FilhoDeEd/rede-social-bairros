from django.core.management.base import BaseCommand, CommandParser
from forum.models import Forum
from user_profile.models import Neighborhood, UserProfile


class Command(BaseCommand):
    help = 'Creates default forums for each neighborhood with a "ghost" user_profile as the owner.'

    def add_arguments(self, parser: CommandParser) -> None:
        # Add an argument to limit the number of neighborhoods processed, but it's not required
        parser.add_argument(
            '--limit', 
            type=int, 
            help='Limit the number of neighborhoods to process (optional)',
        )

    def handle(self, *args, **kwargs):
        # Get the limit from the command-line argument, if provided
        limit = kwargs.get('limit')

        # Get neighborhoods, applying the limit if provided
        if limit:
            neighborhoods = Neighborhood.objects.all()[:limit]
        else:
            neighborhoods = Neighborhood.objects.all()

        # Iterate over each neighborhood
        for neighborhood in neighborhoods:
            try:
                # Create the "ghost" UserProfile (not linked to any account)
                ghost_profile = UserProfile.objects.create(        
                    neighborhood=neighborhood,  # Link to the specific neighborhood
                )

                # Create default forums for this neighborhood
                forum_titles = [
                    f"{neighborhood.name} - Notícias e Atualizações Locais",
                    f"{neighborhood.name} - Comércio Local",
                    f"{neighborhood.name} - Segurança e Emergências",
                    f"{neighborhood.name} - Transporte e Trânsito",
                    f"{neighborhood.name} - Vagas e Empregos Locais",
                ]

                # Create each forum and associate it with the ghost profile as the owner
                for title in forum_titles:
                    Forum.objects.create(
                        owner=ghost_profile,  # Assign the ghost profile as the forum owner
                        neighborhood=neighborhood,  # Link the forum to the neighborhood
                        title=title,  # Set the forum title
                        description=f"Forum about {title}",  # Set a description for the forum
                    )

                self.stdout.write(self.style.SUCCESS(f"Forums created for neighborhood {neighborhood.name}"))

            except Exception as e:
                # If an error occurs, show an error message with the neighborhood name
                self.stdout.write(self.style.ERROR(f"Error creating forums for neighborhood {neighborhood.name}: {e}"))
