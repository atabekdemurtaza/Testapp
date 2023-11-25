from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from .models import CustomUser


@shared_task
def send_welcome_email(user_id):
    user = CustomUser.objects.get(pk=user_id)
    subject = 'Welcome to Book List'
    message = render_to_string('welcome_email_template.txt', {'user': user})
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])
