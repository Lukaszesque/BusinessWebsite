from msilib.schema import Class
from urllib.request import Request
from django.test import TestCase
from django.test.client import RequestFactory
from settings.models import ClassOfBusiness
from settings.services.shared.pagination.pagination import pagination

class PaginationTestCase(TestCase):
    
    def setup(self):

        i = 1
        while i < 12:
            ClassOfBusiness.objects.create(a="a", classOfBusiness_text="Class of business" % i)
            i += 1
            print(i)

    def test_assert_correct_number_of_pages(self):
        rf = RequestFactory()
        page_obj = pagination.get_page_obj(rf.get('test'), ClassOfBusiness.objects.all())
        self.assertEqual(page_obj, "<Page 1 of 2>")
