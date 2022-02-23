from django.test import TestCase
from django.core import mail
from api.tasks import send_report
from django.contrib.auth.models import User


class ReportTest(TestCase):
    def setUp(self):
        User.objects.create_user(username='test', email='test@test.com', password='test123')
        send_report()

    def test_send_email(self):
        self.assertEqual(len(mail.outbox), 1)
