from django.core.management.base import BaseCommand
import yaml
import json

class Command(BaseCommand):
    help = 'Generate SDG Metadata'

    def handle(self, *args, **kwargs):
        # Example: Generate metadata
        metadata = {
            'project_name': 'Your Project Name',
            'sdg_goals': ['Goal 1', 'Goal 2'],
            'status': 'Active'
        }

        # Write to a YAML file
        with open('sdg_metadata.yml', 'w') as yaml_file:
            yaml.dump(metadata, yaml_file)

        # Alternatively, write to a JSON file
        with open('sdg_metadata.json', 'w') as json_file:
            json.dump(metadata, json_file, indent=4)

        self.stdout.write(self.style.SUCCESS('Successfully generated SDG metadata'))