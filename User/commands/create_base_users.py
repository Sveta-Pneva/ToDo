from django.contrib.auth.hashers import make_password
from django.core.management.base import BaseCommand

from User.models import CustomUser


class Command(BaseCommand):
    help = "Создание базовых пользователей"

    def handle(self, *args, **options):
        CustomUser.objects.all().delete()


        CustomUser.objects.create(
            username="admin",
            email="admin@totonotes.ru",
            password=make_password("masteradmin"),
            is_superuser=True,
            is_staff=True,
        )


        CustomUser.objects.create(username="user001", firstname="001", surname="u", email="user001@totonotes.ru")
        CustomUser.objects.create(username="user002", firstname="002", surname="u", email="user002@totonotes.ru")
        CustomUser.objects.create(username="user003", firstname="003", surname="u", email="user003@totonotes.ru")
        CustomUser.objects.create(username="user004", firstname="004", surname="u", email="user004@totonotes.ru")
        CustomUser.objects.create(username="user005", firstname="005", surname="u", email="user005@totonotes.ru")


        self.stdout.write(f"Пользователи созданы")