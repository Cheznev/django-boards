# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 13:24:47 2019

@author: Chibuzo"""

from django.test import TestCase
from ..forms import SignUpForm

class SignUpFormTest(TestCase):
    
    def test_form_has_fields(self):
        form = SignUpForm()
        expected = ['username', 'email', 'password1', 'password2',]
        actual = list(form.fields)
        self.assertSequenceEqual(expected, actual)