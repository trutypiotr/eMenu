from datetime import timedelta
from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.db.models import Q
from django.template.loader import render_to_string
from django.utils import timezone
from django.utils.html import strip_tags
from . import models


def get_dishes():
    yesterday = timezone.now() - timedelta(days=1)
    return models.Dish.objects.filter(Q(addition_date=yesterday) | (Q(update_date=yesterday)))


@shared_task
def send_report():
    receivers = []
    for user in User.objects.all():
        receivers.append(user.email)

    html_message = render_to_string('report.html', {'dishes': get_dishes()})
    plain_message = strip_tags(html_message)
    send_mail('Raport', plain_message, 'report@emenu.pl', receivers, html_message=html_message)
