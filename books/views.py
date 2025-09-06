from django.http import HttpResponse, JsonResponse


books = [
    {"title": "name 1", "author": "author 1"},
    {"title": "name 2", "author": "author 2"},
    {"title": "name 3", "author": "author 3"},
]

def book_list(request):
    """
    shows the list of books HttpResponse format
    """
    result = "<br>".join([f"{b['title']} by {b['author']} " for b in books])
    return HttpResponse(result)

def book_json(request):
    """
    shows the list of books Json format
    """
    return JsonResponse(books, safe=False)
