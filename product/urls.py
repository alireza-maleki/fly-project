from django.urls import path

# from product.views import books_view, book_detail_view, category_view, publisher_view

# urlpatterns = [
#     path('books/', books_view),
#     path('books/<int:pk>/', book_detail_view),
#     path('category/<int:pk>/', category_view),
#     path('publisher/<int:pk>/', publisher_view),
# ]


from product.views import flight_tickets_list, flight_ticket_detail

urlpatterns = [
    path('flight-tickets/', flight_tickets_list, name='flight-tickets-list'),
    path('flight-tickets/<int:pk>/', flight_ticket_detail, name='flight-ticket-detail'),
]