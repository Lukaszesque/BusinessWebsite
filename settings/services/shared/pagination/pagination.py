from settings.models import ClassOfBusiness
from django.core.paginator import Paginator

class pagination:
    
    def get_page_obj(request, objects_to_paginate):
        paginator = Paginator(objects_to_paginate, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        print(page_obj);
        return page_obj
