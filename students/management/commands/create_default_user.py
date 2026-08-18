from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        username = "Lakshya"
        password = "lakshya9070"

        user, created = User.objects.get_or_create(
            username=username
        )

        if created:
            user.set_password(password)
            user.is_staff = True
            user.is_superuser = True
            user.save()

            self.stdout.write(
                self.style.SUCCESS("Default user created successfully!")
            )

        else:
            self.stdout.write(
                self.style.SUCCESS("User already exists!")
            )