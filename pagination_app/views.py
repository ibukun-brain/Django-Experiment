from django.http import JsonResponse
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Book

# Create your views here.
def booklist(request):
    books = Book.objects.all()
    paginator = Paginator(books, 3) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # print(books.number)
    print(page_number)

    # if request.is_ajax():
        # return JsonResponse({'page_no': page_number})

    context = {
        'books' : page_obj,
    }

    return render(request, 'pagination_app/index.html', context)
    
    