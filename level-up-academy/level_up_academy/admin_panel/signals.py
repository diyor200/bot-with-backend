from django.db.models.signals import post_save
from django.dispatch import receiver
from django.apps import apps
import requests
import json

from .models import Homework, Test

import os

@receiver(post_save, sender=Homework)
def handle_new_instance(sender, instance: Homework, created, **kwargs):
    if created:
        print("New instance created:", instance.image_url)
        url = os.environ.get("BOT_HOST")+"/test"

        payload = json.dumps({
            "teacher": f"{instance.owner.name}",
            "image_url": f"{instance.image_url}",
            "text": f"{instance.caption}"
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)


@receiver(post_save, sender=Test)
def handle_new_instance(sender, instance: Test, created, **kwargs):
    print(instance.unit)
    print(instance.book)
    print(instance.total)