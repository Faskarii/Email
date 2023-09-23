from celery import shared_task
from time import sleep
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_mail_task():
    sleep(5)
    send_mail('Celery Task Done!',
              'Mission Done!',
              settings.EMAIL_HOST_USER,
              [settings.RECIPIENT_ADDRESS])