from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase
from gaz_counter.models import GazCounterModel
from decimal import Decimal
import mock

class GazCounterModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='Mike')
        self.gaz_model = GazCounterModel.objects.create(id=1,
                                                        value=100, 
                                                        date='2020-09-03T08:10:53.660Z',
                                                        unit_price=Decimal(1.30),
                                                        monthly_usage=20,
                                                        monthly_cost=Decimal(26.00),
                                                        owner=self.user, 
        )
    
    def tearDown(self):
        del self.gaz_model
    
    def test_str_method(self):
        self.assertEqual(str(self.gaz_model.value), '100')
        self.assertEqual(str(self.gaz_model.date), '2020-09-03T08:10:53.660Z')
        self.assertEqual(str(float(Decimal(self.gaz_model.unit_price))), '1.3')
        self.assertEqual(str(self.gaz_model.value), '100')
        self.assertEqual(str(self.gaz_model.monthly_usage), '100')
        self.assertEqual(str(self.gaz_model.monthly_cost), '130.0')
    
    @mock.patch('gaz_counter.models.__str__')
    def test_should_return_str(self, __str__):
        __str__.return_value = f'100 2020-09-03T08:10:53.660Z 1.30 100 130.0'
        self.assertEqual(f'100 2020-09-03T08:10:53.660Z {Decimal(1.30)} 100 130.0', self.gaz_model.__str__())

    @mock.patch('gaz_counter.models.reverse')
    def test_absolute_url(self, reverse):    
        reverse.return_value = 'gaz-detail/2'
        self.assertEqual('gaz-detail/2', self.gaz_model.get_absolute_url())
    
    def test_shoul_rise_ObjectDoesNotExist_error(self):
        with self.assertRaises(ObjectDoesNotExist):
            self.gaz_obj = GazCounterModel.objects.create(value=22)
    
    def test_should_raise_TypeError(self):
        with self.assertRaises(TypeError):
            self.gaz_obj = GazCounterModel.objects.create(value='22', owner=self.user)
    
    def test_should_raise_ValueError(self):
        with self.assertRaises(ValueError):
            self.gaz_obj = GazCounterModel.objects.create(value='22', owner='')