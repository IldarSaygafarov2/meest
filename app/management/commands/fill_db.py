from django.core.management.base import BaseCommand
from django.conf import settings
from app.models import UserRequest
import os
import json


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open(settings.BASE_DIR / 'data.json', mode='r', encoding='utf-8') as file:
            data = json.load(file)


        for item in data['rows']:
            try:
                obj = UserRequest.objects.create(
                    track_number=item[1],
                    fullname=item[2],
                    passport_series=item[3],
                    passport_number=item[4],
                    pinfl=item[5],
                    phone_number=item[6],
                    created_at=item[7],
                )
                obj.save()
            except Exception as e:
                print(e)
                print(item)