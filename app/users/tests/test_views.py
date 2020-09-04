from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User


from users.forms import UserCreationForm, UserUpdateForm, UserRegistrationForm
import mock

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

class UserCreationTest(TestCase):

    def setUp(self):
        self.user_1 = User.objects.create(username='u1', first_name='Nick')
        self.user_2 = User.objects.create(username='u2', first_name='Jim')

        self.user_1.refresh_from_db()
        self.user_2.refresh_from_db()
    
    def tearDown(self):
        del self.user_1
        del self.user_2

    def test_check_create_user(self):
        user_1_first_name = 'Nick' 
        user_2_first_name = 'Jim'

        self.assertTrue(isinstance(self.user_1, User))
        self.assertTrue(isinstance(self.user_2, User))

        self.assertEqual(user_1_first_name, self.user_1.first_name)
        self.assertEqual(user_2_first_name, self.user_2.first_name)

class UsersViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username = 'user_1',
            email = 'abc@company.com',
            )
        self.template_name = 'users/profile.html'

        self.user.refresh_from_db()

    def tearDown(self):
        del self.template_name
        del self.user
    
    def test_created_message(self):
        response = self.client.get('/register/')
        self.assertContains(response, 'Registration')
    
    @mock.patch('users.views.messages')
    def test_message_after_create_user(self, messages):
        test_message = 'Account has been created'
        messages.data_return = 'Account has been created'
        message_return = messages.data_return
        
        self.assertEquals(test_message, message_return)
    
    def test_valid_form(self):
        data = {'username': self.user.username,
                'email': self.user.email,
                'password1': 'testing321',
                'password2': 'testing321',
        }
        form = UserRegistrationForm(data=data)

        self.assertTrue(form.is_valid())
