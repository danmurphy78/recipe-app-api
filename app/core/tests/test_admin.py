from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
import logging


class AdminSiteTests(TestCase):

    def setuUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@google.com',
            password='test123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test@google.com',
            password='test123',
            name='Test user full name'
        )

    def test_users_listed(self):
        """Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        logging.basicConfig(level=logging.DEBUG)
        logging.debug('--- - - -- - -- - -')
        logging.debug(res)
        logging.debug('--- - - -- - -- - -')
        logging.debug(dir(res))
        logging.debug('--- - - -- - -- - -')

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)
