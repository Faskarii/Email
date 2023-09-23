from django.shortcuts import render
from django.http import HttpResponse
from .tasks import send_mail_task
def Send(request):
    send_mail_task.delay()
    return HttpResponse('<h1>Email has been sent!</h1>')
