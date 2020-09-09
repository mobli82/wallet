from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from gaz_counter.models import GazCounterModel
from gaz_counter.views import (GazCounterListView,
                               GazCounterDetailView,
                               GazCounterCreateView,
                               GazCounterDeleteView,
                               GazCounterUpdateView,
)
import mock
from unittest_data_provider import data_provider
from decimal import Decimal


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

class GazCounterDetailView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='Mike')
        self.record = GazCounterModel.objects.create(
                                                        id=1,
                                                        value=100, 
                                                        date='2020-09-03T08:10:53.660Z',
                                                        unit_price=Decimal(1.30),
                                                        monthly_usage=20,
                                                        monthly_cost=Decimal(26.00),
                                                        owner=self.user
        )
        self.detail_view = GazCounterDetailView()
        self.template_name = 'gaz_counter/gaz_counter_detail.html'
    
    def tearDown(self):
        del self.detail_view
        del self.template_name
    
    def test_template_name(self):
        resp = self.client.get('/gaz-detail/1/')

        self.assertEqual(resp.status_code, 302)
        # self.assertTemplateUsed(resp, self.template_name)