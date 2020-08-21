from django.db.models import F, Value, CharField
from django.db.models.functions import Concat
from django.http import JsonResponse

from company.logic import get_branch_facade_image_url_prefix
from company.models import Branch


def all_branches(request):
    """
    Main view for branches.
    """

    url_prefix = get_branch_facade_image_url_prefix()
    qs = Branch.objects
    qs = qs.annotate(url=Concat(Value(url_prefix), F('facade_image'),
                                output_field=CharField()))
    qs = qs.values('name', 'url', 'longitude', 'latitude')
    books = list(qs)
    return JsonResponse(books, safe=False)
