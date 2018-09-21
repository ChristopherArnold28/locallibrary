from django.shortcuts import render
from catalog.models import Author, Book, BookInstance, Genre
# Create your views here.
def index(request):
    """View function for home page of site/"""

    #Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    #available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact = 'a').count()

    #the all() is implied by default
    num_authors = Author.objects.count()

    context = {
        'num_books' : num_books,
        'num_instances':num_instances,
        'num_instsances_available':num_instances_available,
        'num_authors':num_authors
    }

    return render(request, 'index.html', context = context)


from django.views import generic

class BookListView(generic.ListView):
    model = Book
    paginate_by = 10

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10

class AuthorDetailView(generic.DetailView):
    model = Author
