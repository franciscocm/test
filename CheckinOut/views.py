from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from ClientManager.models import clients, catalog, backlog
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

# Create your views here.

def select(request):
    print("Estou no def select")
    
    selector = request.GET['selector']
    nif = request.GET['nif']

    if nif == '':
        print("Entrei raise http404")
        raise Http404
    else:
        print("entrei else")
        #client = get_object_or_404(clients, nif=nif)

        books = catalog.objects.only("book")
        try:
            print("entrei try")
            client = clients.objects.get(nif=nif)
        except clients.DoesNotExist:
            print("entrei excepcao")
            messages.info(request, 'NIF not found! Please register client!')
            return clientregister(request)
            #return render(request,'clientregister.html', {'nif':nif})
            #raise Http404
        
        context = {
                    'client': client,
                    'books' : books
                }
        print('NIF: ',nif)

        if selector == 'checkoutbook':
            print("selector check out book")
            return render(request,'checkoutbook.html',context)
            #return checkoutbook(request, nif)
        elif selector == 'checkinbook':
            print("selector check in book")
            return render(request,'checkinbook.html',context)
        elif selector == 'clientbacklog':
            print("selector client back log")
            return render(request,'clientbacklog.html', context)
        elif selector == 'clientregister':
            print('selector client register')
            return clientregister(request)
            #return render(request,'/clientregister.html')
        else:
            print("else")
            return render(request,'clientmanager.html')







def checkoutbook(request):
    print("Estou no def check out book")

    if request.method=='POST':
        nif = request.POST['nif']
        book = request.POST['book']
        days = request.POST['days']
        #date_beg = request.POST['date_beg']
        book_id = catalog.objects.values_list('id', flat=True).get(book=book)
        book_price = catalog.objects.values_list('price', flat=True).get(book=book)
        value = days * book_price

        upload = backlog(user_id=nif, book_id=book_id, book=book, price=book_price, date_end='1990-01-01', days=days, value=value)
        upload.save()
        return render(request,'clientmanager.html')

    else:
        books = catalog.objects.only("book")
        try:
            print("entrei try")
            client = clients.objects.get(nif=nif)
        except clients.DoesNotExist:
            print("entrei excepcao")
            messages.info(request, 'NIF not found! Please register client!')
            return clientregister(request)
        
        context = {
                    'client': client,
                    'books' : books
                }

        return render(request,'checkoutbook.html', context)


def checkinbook(request):
    print("Estou no def Check In Book")

    if request.method=='POST':
        nif = request.POST['nif']
        book = request.POST['book']
        date_end = request.POST['date_end']
        book_id = catalog.objects.values_list('id', flat=True).get(book=book)
        #book_price = catalog.objects.values_list('price', flat=True).get(book=book)

        backlog.objects.filter(user_id=nif,book_id=book_id).update(date_end=date_end)

        return render(request,'clientmanager.html')
    else:
        return render(request,'checkinbook.html')


def clientbacklog(request):
    print("Estou no def client Backlog")
    return render(request,'clientbacklog.html')


def clientregister(request):
    print("estou no def client register")
    if request.method=='POST':
        nif = request.POST['nif']
        name = request.POST['name']
        email = request.POST['email']
        date_birth = request.POST['date_birth']

        upload = clients(name=name, nif=nif, date_birth=date_birth, mail=email)
        upload.save()
        return render(request,'clientmanager.html')

    else:
        return render(request,'clientregister.html')