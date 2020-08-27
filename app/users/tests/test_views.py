from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from users.forms import UserRegistrationForm
import json

class TestUsersViews(TestCase):
    def setUp(self):
        self.user_1 = User.objects.create(username='user_1',
                                        first_name='Mike',
                                        email='abc@email.com',                                 
        )


    def test_register_view_GET(self):
        response = self.client.get(reverse('register'))
        # print(response.context)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/registration.html')
        self.failUnless(isinstance(response.context['form'],
                                    UserRegistrationForm
        ))

    def test_login_view_GET(self):
        response = self.client.get(reverse('login'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')
    
    def test_register_user_POST(self):
        response = self.client.post(reverse('register'), 
                                data={'username': 'user_3',
                                    'email': 'abc@eamil.com',
        })
        
        print(dir(response))
        # print(response.json)
        # print(response)

        self.assertEquals(response.status_code, 200)
        self.assertEquals(self.user.username, 'user_3')
