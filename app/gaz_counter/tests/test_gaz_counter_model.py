from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase
# from django.core.validators import 

from .exceptions import RelatedObjectDoesNotExist
from gaz_counter.models import GazCounterModel
from decimal import Decimal
import mock

class GazCounterModelTest(TestCase):
    def setUp(self):
        self.gaz_model = GazCounterModel(id=1,
                                        value='100', 
                                        date='2020-09-03T08:10:53.660Z',
                                        unit_price=Decimal(1.30),
                                        monthly_usage=20,
                                        monthly_cost=Decimal(26.00),
        )
    
    def tearDown(self):
        del self.gaz_model
    
    def test_str_method(self):
        self.assertEqual(str(self.gaz_model.value), '100')
        self.assertEqual(str(self.gaz_model.date), '2020-09-03T08:10:53.660Z')
        self.assertEqual(str(float(Decimal(self.gaz_model.unit_price))), '1.3')
        self.assertEqual(str(self.gaz_model.value), '100')
        self.assertEqual(str(self.gaz_model.monthly_usage), '20')
        self.assertEqual(str(self.gaz_model.monthly_cost), '26')
    
    @mock.patch('gaz_counter.models.reverse')
    def test_absolute_url(self, reverse):
        reverse.return_value = 'gaz-detail/2'

        self.assertEqual('gaz-detail/2', self.gaz_model.get_absolute_url())
    
    def test_shoul_rise_RelatedObjectDoesNotExist_error(self):
        with self.assertRaises(ObjectDoesNotExist):
            self.gaz_obj = GazCounterModel.objects.create(value=22)