# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.utils import timezone
from django.test import TestCase
from django.urls import reverse

from .models import Nameaddress
# Create your tests here.

def create_NameAddress(name_txt, email_txt):
        """
        Create a new record (names, email) with the given `name_text` and `email_text`.
        """
        name_txt='name_txt'
        email_txt='email@yahoo.fr'
        return Nameaddress.objects.create(name_text=name_txt, email_text=email_txt)

class NameadressText(TestCase)

	def test_list_contact(self):
        """
        If no contacts exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('myapp:list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No recors are available.")
        self.assertQuerysetEqual(response.context['name_list'], [])
