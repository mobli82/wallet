from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from django.contrib.auth.views import (
        LogoutView, 
        LoginView,
        PasswordResetView,
        PasswordResetDoneView,
        PasswordResetConfirmView,
        PasswordResetCompleteView, 
    )
from users.views import profile, register


class TestUsersUrls(SimpleTestCase):
    
    def test_register_url(self):
        url_register = reverse('register')

        # print(resolve(url_register))
        self.assertEqual(resolve(url_register).func, register)

    def test_profile_url(self):
        url_profile = reverse('profile')

        # print(resolve(url_profile))
        self.assertEqual(resolve(url_profile).func, profile)
    
    def test_logout_url(self):
        url_logout = reverse('logout')

        # print(resolve(url_logout))
        self.assertEqual(resolve(url_logout).func.view_class, 
                        LogoutView
        )

    def test_login_url(self):
        url_login = reverse('login')

        # print(resolve(url_login))
        self.assertEqual(resolve(url_login).func.view_class, 
                        LoginView
        )
    
    def test_login_url(self):
        url_login = reverse('login')

        # print(resolve(url_login))
        self.assertEqual(resolve(url_login).func.view_class, 
                        LoginView
        )
    
    def test_password_reset_url(self):
        url_password_reset = reverse('password_reset')

        # print(resolve(url_password_reset))
        self.assertEqual(resolve(url_password_reset).func.view_class, 
                        PasswordResetView
        )
    
    def test_password_reset_done_url(self):
        url_password_reset_done = reverse('password_reset_done')

        # print(resolve(url_password_reset_done))
        self.assertEqual(resolve(url_password_reset_done).func.view_class, 
                        PasswordResetDoneView
        )
    
    def test_password_reset_confirm_url(self):
        url_password_reset_confirm = reverse('password_reset_confirm', 
                                            args=['1234', 'abcd']
        )

        # print(resolve(url_password_reset_confirm))
        self.assertEqual(resolve(url_password_reset_confirm).func.view_class, 
                        PasswordResetConfirmView
        )
    
    def test_password_reset_complete_url(self):
        url_password_reset_complete = reverse('password_reset_complete')

        # print(resolve(url_password_reset_complete))
        self.assertEqual(resolve(url_password_reset_complete).func.view_class, 
                        PasswordResetCompleteView
        )