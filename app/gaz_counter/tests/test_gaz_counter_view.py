from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from gaz_counter.views import GazCounterListView
import mock
from unittest_data_provider import data_provider


class GazCounterListView(TestCase):
    def setUp(self):
        self.gaz_view = GazCounterListView()
        self.temp_name = 'gaz_counter/gaz_counter_create.html'

    def tearDown(self):
        del self.gaz_view
        del self.temp_name
    
    def test_list_has_table(self):
        resp = self.client.get('/')

        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Login')
        self.assertContains(resp, 'Profile')
    
    def test_has_template_name(self):
        resp = self.client.get('/gaz-create/')
        self.assertTemplateUsed(resp, self.temp_name)
    
    def test_anonymous_can_see_gaz_list(self):
        user = User.objects.create_user('Nick')

        self.client.force_login(user)
        res = self.client.get(reverse('gaz-list'))

        self.assertEqual(res.status_code, 200)

    def test_anonymous_cannot_see_gaz_list(self):
        with self.assertRaises(TypeError):
            self.client.get(reverse('gaz-list'))
    
    # @data_provider(template_data)
    # def test_templates_names(self, template_data):
    #     get_name = lambda: self.templates_names

    #     self.assertEqual(template_data[1], self.return_temp(template_data[0]))