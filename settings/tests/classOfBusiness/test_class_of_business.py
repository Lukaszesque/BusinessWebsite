from msilib.schema import Class
from urllib.request import Request
from django.test import TestCase
from django.test.client import RequestFactory
from settings.models import ClassOfBusiness
from settings.services.shared.pagination.pagination import pagination

class PaginationTestCase(TestCase):
    
    def setUp(self):

        i = 1
        while i < 12:
            ClassOfBusiness.objects.create(classOfBusiness_text="Class of business")
            i += 1

    def test_assert_correct_number_of_pages(self):
        rf = RequestFactory()
        page_obj = pagination.get_page_obj(rf.get('test'), ClassOfBusiness.objects.all().order_by('id'))
        self.assertEqual(str(page_obj), "<Page 1 of 2>")
