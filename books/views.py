from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
# Create your views here.

def bookshome(request):

    booksinfo = [
		{"id":1, "name":"book1", "description":"book1_description"},
		{"id":2, "name":"book2", "description":"book2_description"},
		{"id":3, "name":"book3", "description":"book3_description"}
    ]
    return render(request,"books/home.html",context={"booksinfo" : booksinfo})

def aboutus(request):
    return render(request,"books/aboutus.html")

def contactus(request):
    return render(request,"books/contactus.html")



def books2(request):

    return HttpResponse("<h1> Books page 2</h1>")


def books3(request):

    return HttpResponse("<h1> Books page 3 </h1>")

