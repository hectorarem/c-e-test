from io import BytesIO
from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client
from .models import File

c = Client()


class FileTestCase(TestCase):
    api_auth = '/api/v1/auth/'
    api = '/api/v1/file/file/'
    user_login = {"username": "man", "password": "zaqwsxcde123/*-+"}

    def setUp(self):
        User.objects.create_user(username="man", email='man@gmail.com', password='zaqwsxcde123/*-+')


    def login(self):
        """login"""
        response = c.post(f'{self.api_auth}login', self.user_login)
        return response.json()

    def test_file_list(self):
        login = self.login()
        if login['access']:
            access = login['access']
            bearer = f"Bearer {access}"
            list = c.get(self.api, HTTP_AUTHORIZATION=bearer)
            self.assertEqual(list.status_code, 200)

    def test_file_CRD(self):
        """Check create, read and delete file. Test if can upload same file. Test change filename """

        login = self.login()
        if login['access']:
            access = login['access']
            user_id = login['user']['id']
            bearer = f"Bearer {access}"

            # Create
            img = BytesIO(b'mybinarydata')
            img.name = 'myimage.jpg'
            data = {
                "uploaded_by": user_id,
                "file": img,
            }
            new_file = c.post(self.api, data=data, HTTP_AUTHORIZATION=bearer)
            self.assertEqual(new_file.status_code, 201)

            # confirm create
            self.assertEqual(File.objects.count(), 1)

            last_file = File.objects.last()

            # Read
            read_file = c.get(f'{self.api}{last_file.pk}/', HTTP_AUTHORIZATION=bearer)
            self.assertEqual(read_file.status_code, 200)

            # Update filename
            name_update = c.post(
                '/api/v1/file/change/filename/',
                data={"id": last_file.pk, "name": 'NewName', "ext": last_file.file_extension},
                HTTP_AUTHORIZATION=bearer
            )
            self.assertEqual(name_update.status_code, 200)

            # Check if name change
            updated_file = File.objects.get(pk=last_file.pk)
            self.assertNotEqual(last_file.file.name, updated_file.file.name)

            # Delete
            delete_file = c.delete(f'{self.api}{last_file.pk}/', HTTP_AUTHORIZATION=bearer)
            self.assertEqual(delete_file.status_code, 204)
            # confirm delete
            self.assertEqual(File.objects.count(), 0)

