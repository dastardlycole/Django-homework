import imp
from urllib import response
from django.test import TestCase
from django.urls import reverse, resolve
from .views import *

# Create your tests here.

class CompanyTests(TestCase):
    def test_home_view(self):
        res = resolve(reverse('home'))
        self.assertEqual(res.func,home)
        response = self.client.get('/home/')
        self.assertTemplateUsed(response,'home.html')  

    def test_about_view(self):
        res = resolve('/about/')     
        self.assertEqual(res.func,about_us)
        response = self.client.get('/about/')
        self.assertContains(response, "This is our about page")

    def test_contact_view(self):
        res = resolve(reverse('contact'))
        self.assertEqual(res.url_name,'contact')
        response = self.client.get(reverse('contact'))
        self.assertTemplateUsed(response, 'contact.html')