from django.contrib.auth.models import User, Group
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient
from .factory import *
from .models import *


class TestDocumentRuleGet(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.url = reverse('documents-list')
        populate_test_db_users(User,Group)
        populate_test_db_docs(Document)

    def test_common_permissions(self):
        self.client.login(username='common', password='123456')
        self.response = self.client.get(self.url)
        self.assertContains(self.response, text='public document', status_code=200)

    def test_common_no_permissions(self):
        self.client.login(username='common', password='123456')
        self.response = self.client.get(self.url)
        self.assertNotContains(self.response, text='private document', status_code=200)

    def test_sergeant_permissions(self):
        self.client.login(username='sergeant', password='123456')
        self.response = self.client.get(self.url)
        self.assertContains(self.response, text='private document', status_code=200)

    def test_sergeant_no_permissions(self):
        self.client.login(username='sergeant', password='123456')
        self.response = self.client.get(self.url)
        self.assertNotContains(self.response, text='secret document', status_code=200)

    def test_general_permissions(self):
        self.client.login(username='general', password='123456')
        self.response = self.client.get(self.url)
        self.assertContains(self.response, text='secret document', status_code=200)

    def test_general_no_permissions(self):
        self.client.login(username='general', password='123456')
        self.response = self.client.get(self.url)
        self.assertNotContains(self.response, text='top-secret document', status_code=200)

    def test_get_president_permissions_public(self):
        self.client.login(username='president', password='123456')
        self.response = self.client.get(self.url)
        self.assertContains(self.response, text='public', status_code=200)

    def test_get_president_permissions_secret(self):
        self.client.login(username='president', password='123456')
        self.response = self.client.get(self.url)
        self.assertContains(self.response, text='secret', status_code=200)

    def test_get_president_permissions_top_private(self):
        self.client.login(username='president', password='123456')
        self.response = self.client.get(self.url)
        self.assertContains(self.response, text='private', status_code=200)


class TestDocumentRulePost(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.url = reverse('documents-list')
        populate_test_db_users(User,Group)

    def test_post_common_no_permissions_public(self):
        self.client.login(username='common', password='123456')
        data = {
            "title": "test doc for common",
            "date_expired": "2021-05-10",
            "status": "Active",
            "document_root": "Public",
            "text": "Test doc for president"
        }
        self.response = self.client.post(self.url, data)
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_common_no_permissions_private(self):
        self.client.login(username='common', password='123456')
        data = {
            "title": "test doc for common",
            "date_expired": "2021-05-10",
            "status": "Active",
            "document_root": "Private",
            "text": "Test doc for president"
        }
        self.response = self.client.post(self.url, data)
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_common_no_permissions_secret(self):
        self.client.login(username='common', password='123456')
        data = {
            "title": "test doc for common",
            "date_expired": "2021-05-10",
            "status": "Active",
            "document_root": "Secret",
            "text": "Test doc for common"
        }
        self.response = self.client.post(self.url, data)
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_common_no_permissions_top_secret(self):
        self.client.login(username='common', password='123456')
        data = {
            "title": "test doc for common",
            "date_expired": "2021-05-10",
            "status": "Active",
            "document_root": "Top-Secret",
            "text": "Test doc for common"
        }
        self.response = self.client.post(self.url, data)
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_sergeant_no_permissions_public(self):
        self.client.login(username='sergeant', password='123456')
        data = {
            "title": "test doc for sergeant",
            "date_expired": "2021-05-10",
            "status": "Active",
            "document_root": "Public",
            "text": "Test doc for sergeant"
        }
        self.response = self.client.post(self.url, data)
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_sergeant_no_permissions_private(self):
        self.client.login(username='sergeant', password='123456')
        data = {
            "title": "test doc for sergeant",
            "date_expired": "2021-05-10",
            "status": "Active",
            "document_root": "Private",
            "text": "Test doc for sergeant"
        }
        self.response = self.client.post(self.url, data)
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_sergeant_no_permissions_secret(self):
        self.client.login(username='sergeant', password='123456')
        data = {
            "title": "test doc for sergeant",
            "date_expired": "2021-05-10",
            "status": "Active",
            "document_root": "Secret",
            "text": "Test doc for sergeant"
        }
        self.response = self.client.post(self.url, data)
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_sergeant_no_permissions_top_secret(self):
        self.client.login(username='sergeant', password='123456')
        data = {
            "title": "test doc for sergeant",
            "date_expired": "2021-05-10",
            "status": "Active",
            "document_root": "Top-Secret",
            "text": "Test doc for sergeant"
        }
        self.response = self.client.post(self.url, data)
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_general_no_permissions_public(self):
        self.client.login(username='general', password='123456')
        data = {
            "title": "test doc for general",
            "date_expired": "2021-05-10",
            "status": "Active",
            "document_root": "Public",
            "text": "Test doc for general"
        }
        self.response = self.client.post(self.url, data)
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_general_no_permissions_private(self):
        self.client.login(username='general', password='123456')
        data = {
            "title": "test doc for general",
            "date_expired": "2021-05-10",
            "status": "Active",
            "document_root": "Private",
            "text": "Test doc for general"
        }
        self.response = self.client.post(self.url, data)
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_general_no_permissions_secret(self):
        self.client.login(username='general', password='123456')
        data = {
            "title": "test doc for general",
            "date_expired": "2021-05-10",
            "status": "Active",
            "document_root": "Secret",
            "text": "Test doc for general"
        }
        self.response = self.client.post(self.url, data)
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_general_no_permissions_top_secret(self):
        self.client.login(username='general', password='123456')
        data = {
            "title": "test doc for general",
            "date_expired": "2021-05-10",
            "status": "Active",
            "document_root": "Top-Secret",
            "text": "Test doc for general"
        }
        self.response = self.client.post(self.url, data)
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_president_permissions_public(self):
        self.client.login(username='president', password='123456')
        data = {
            "title": "test doc for president",
            "date_expired": "2021-05-10",
            "status": "Active",
            "document_root": "Public",
            "text": "Test doc for president"
        }
        self.response = self.client.post(self.url, data)
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_post_president_permissions_private(self):
        self.client.login(username='president', password='123456')
        data = {
            "title": "test doc for president",
            "date_expired": "2021-05-10",
            "status": "Active",
            "document_root": "Private",
            "text": "Test doc for president"
        }
        self.response = self.client.post(self.url, data)
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_post_president_permissions_secret(self):
        self.client.login(username='president', password='123456')
        data = {
            "title": "test doc for president",
            "date_expired": "2021-05-10",
            "status": "Active",
            "document_root": "Secret",
            "text": "Test doc for president"
        }
        self.response = self.client.post(self.url, data)
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_post_president_permissions_top_secret(self):
        self.client.login(username='president', password='123456')
        data = {
            "title": "test doc for president",
            "date_expired": "2021-05-10",
            "status": "Active",
            "document_root": "Top-Secret",
            "text": "Test doc for president"
        }
        self.response = self.client.post(self.url, data)
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
