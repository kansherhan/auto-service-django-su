import random
from lorem_text import lorem

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from services.models import Service
from spare_parts.models import SparePart


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("count", nargs="+", type=int)

    def handle(self, *args, **options):
        self.__create_super_user()

        count = abs(options["count"]) + 1
        self.__create_services(count)
        self.__create_spare_parts(count)

    @staticmethod
    def __create_super_user():
        super_user = User.objects.create_superuser(
            username="sherhan",
            email="kansherhan@gmail.com",
            password="123456",
        )

        super_user.save()

    @staticmethod
    def __create_services(count: int) -> None:
        for _ in range(1, count):
            service = Service.objects.create(
                name=f"#{_} - {lorem.words(random.randint(3, 10)).capitalize()}",
                image_url="https://picsum.photos/420/225",
                detail=lorem.paragraphs(random.randint(5, 20)),
                price=random.randint(5, 25) * 1000
            )

            service.save()

    @staticmethod
    def __create_spare_parts(count: int) -> None:
        for _ in range(1, count):
            spare_part = SparePart.objects.create(
                name=f"#{_} - {lorem.words(random.randint(3, 10)).capitalize()}",
                image_url="https://picsum.photos/420/225",
                detail=lorem.paragraphs(random.randint(5, 20)),
                price=random.randint(1, 15) * 500
            )

            spare_part.save()
