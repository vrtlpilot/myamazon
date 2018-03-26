from django.core.management.base import BaseCommand
from authapp.models import ShopUser
from catalogapp.managment.commands.import_from_json import import_json
from os import path, getcwd


class Command(BaseCommand):

    def handle(self, *args, **options):

        file_name = "import/promo.json"
        if path.isfile(path.join(getcwd(), file_name)):
            with open(path.join(getcwd(), file_name)) as json_file:
                result = import_json(json_data=json_file.read())
                print("Импортировано объектов - {}".format(result))

        ShopUser.objects.create_superuser(
            username='django',
            password='geekbrains',
            email='django@geekbrains.com',
            age='20'
        )