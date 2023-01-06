
from django.urls import path
from books.views import bookshome , aboutus, contactus, books2 , books3 

urlpatterns = [
   
    path('home', bookshome, name="bookshome"),
    path('page2', books2, name="test"),
    path('page3', books3, name="test"),
    path('about', aboutus, name="aboutus"),
    path('contact', contactus, name="contactus"),
]
