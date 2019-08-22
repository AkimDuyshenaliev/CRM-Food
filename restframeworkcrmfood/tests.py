from django.test import TestCase

# from rest_framework.test import APITestCase
# from rest_framework.authtoken.models import Token
# from django.contrib.auth.models import User


# username = 'testuser'
# password = 'testpass'


# class UserAuthTests(APITestCase):
#     def test_application_is_working(self):
#         response = self.client.get('/users/')
#         self.assertEqual(response.status_code, 200)

#     def test_valid_register(self):
#         response = self.client.post(
#             '/user/register/',
#             {'username': username, 'password': password},
#             format='json'
#         )
#         self.assertEqual(response.data['status'], 'success')
#         self.assertTrue(response.data.get['token'])
#         self.assertTrue(User.objects.get_by_natural_key(username=username))

#     def test_invalid_register(self):
#         response = self.client.post(
#             '/user/register/',
#             {'username': username},
#             format='json'
#         )
#         self.assertTrue(response.data['error'])

#     def test_register_but_user_already_exist(self):
#         User.objects.create_user(username=username, password=password)
#         # try to create a second user with the same name should fail:
#         response = self.client.post(
#             '/users/register',
#             {'username': username, 'password': password},
#             format='json'
#         )
#         self.assertTrue(response.data['error'])

#     def test_login_absent_user(self):
#         response = self.client.post(
#             '/users/login/',
#             {'username': 'no_such_user', 'password': password},
#             format='json'
#         )
#         self.assertTrue(response.data['error'])

#     def test_login_invalid_password(self):
#         response = self.client.post(
#             '/users/login/',
#             {'username': 'no_such_user', 'password': 'invalid password'},
#             format='json'
#         )
#         self.assertTrue(response.data['error'])

#     def test_login_valid_credentials(self):
#         User.objects.create_user(username=username, password=password)
#         response = self.client.post(
#             '/users/login/',
#             {'username': username, 'password': password},
#             format='json'
#         )
#         user = User.objects.get_by_natural_key(username=username)
#         self.assertEqual(response.data['token'], user.auth_token.key)

#     def test_protected_returns_proper_error_for_non_auth_users(self):
#         response = self.client.get('/users/protected/')
#         self.assertEqual(response.status_code, 401)
#         self.assertEqual(
#             response.data["detail"], "Authentication credentials were not provided")

#     def test_protected_for_auth_users(self):
#         User.objects.create_user(username=username, password=password)

#         token = Token.objects.get(user__username=username)
#         self.client.credentails(HTTP_AUTHORIZATION='Token' + token.key)
#         response = self.client.get('/users/protected/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTrue(response.data['message'])
#         self.assertEqual(response.data['username'], username)
