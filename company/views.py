from django.http import JsonResponse

from company.models import Branch


def all_branches(request):
    """
    Main view for branches.
    """
    books = Branch.objects.values('longitude', 'latitude', 'facade_image',
                                  'name')
    books = list(books)
    return JsonResponse(books,safe=False)
