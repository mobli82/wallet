from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User

from users.views import logout
import mock
import json

class UsersViewsTest(TestCase):
    def setUp(self):
        self.user_1 = User.objects.create(username='user_1',
                                        email='abc@email.com',
                                        password='testing321',                                
        )
        self.user_1.save()
        self.login = self.client.login(username='user_1', password='testing321')

    def tearDown(self):
        del self.user_1

    def test_register_view_GET(self):
        response = self.client.get(reverse('register'))
        # print(response.context)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/registration.html')
    
    def test_register_user_POST(self):
        data_registration={'username': 'user_3',
                            'email': 'abc@eamil.com',
                            'password1': 'testing321',
                            'password2': 'testing321',
        }
        
        form_mock = mock.MagicMock(return_value = True)

        resp = self.client.get('/register/')
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Registration')

        if form_mock.return_value:
            req = self.client.post(f'/register/', data=data_registration)
            
            user = User.objects.get(username='user_3')

            self.assertEqual(req.status_code, 302)
            self.assertEqual(user.username, 'user_3')

    @mock.patch('users.views.render')
    def test_logout_view_GET(self, render):
        response = self.client.get(f'/logout/')

        request = mock.MagicMock()
        render.request = True
        
        logout(request)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/logout.html')

    def test_login_view_GET(self):
        response = self.client.get(reverse('login'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')
    
    def test_profile(self):
        request = mock.MagicMock(method='POST')

        user = User.objects.create_user('Mark', email='mark@company.com', password='tester1234')
        login = self.client.login(username='Mark', password='tester1234')

        form_mock_user = mock.MagicMock(return_value = True)
        form_mock_profile = mock.MagicMock(return_value = True)
        if request.method == 'POST':
            if form_mock_profile.return_value and form_mock_user.return_value:
                req = self.client.post('/profile/', {'username': 'jan'})
                
                self.assertEqual(req.status_code, 200)
                
                response = self.client.get('/profile/')
                self.assertEqual(response.status_code, 200)
