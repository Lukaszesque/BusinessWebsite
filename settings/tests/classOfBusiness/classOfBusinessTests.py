from msilib.schema import Class
from urllib.request import Request
from django.test import TestCase
from django.test.client import RequestFactory
from settings.models import ClassOfBusiness
from settings.services.shared.pagination.pagination import pagination


class PaginationTestCase:
    
    def setup(self):
        i = 1
        while i < 12:
            ClassOfBusiness.objects.create(classOfBusiness_text="Class of business" % i)
            i += 1

    def assert_correct_number_of_pages(self):
        rf = RequestFactory()
        pagination.get_page_obj(rf.get, ClassOfBusiness.objects.all)
        self.assertEqual()
