from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404

from django.shortcuts import render
from product.models import FlightTicket

def flight_tickets_view(request):
    tickets = FlightTicket.objects.all()
    context = {'tickets': tickets}
    return render(request, 'wdproject.urls/flight_tickets.html', context)

def flight_ticket_detail(request, pk):
    ticket = get_object_or_404(FlightTicket, pk=pk)
    context = {'ticket': ticket}
    return render(request, 'wdproject.urls/flight_ticket_detail.html', context)


# from product.models import Book, Category, Publisher

# def رrequest):
#     books = Book.objects.all()
#     content = {
#         'books': books
#     }
#     templates = loader.get_template('product/books.html')
#     return HttpResponse(templates.render(content, request))


# def book_detail_view(request, pk):
#     book = Book.objects.get(pk=pk)
#     content = {
#         'book': book
#     }
#     templates = loader.get_template('product/book_detail.html')
#     return HttpResponse(templates.render(content, request))


# def category_view(request, pk):
#     category = Category.objects.get(pk=pk)
#     content = {
#         'category': category
#     }
#     templates = loader.get_template('product/category.html')
#     return HttpResponse(templates.render(content, request))


# def publisher_view(request, pk):
#     publisher = Publisher.objects.get(pk=pk)
#     print(publisher.books)
#     content = {
#         'publisher': publisher
#     }
#     templates = loader.get_template('product/publisher.html')
#     return HttpResponse(templates.render(content, request))

