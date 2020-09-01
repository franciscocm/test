from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from .models import clients, backlog, catalog

from CheckinOut.views import checkinbook, checkoutbook, clientbacklog, clientregister 

# Create your views here.

def clientmanager(request):
  print("estou no def clientmanager")

  if request.method=='POST':
    print("estou no POST")
    selector = request.POST['selector']
    nif = request.POST['nif']
    if nif == '':
        print("Entrei raise http404")
        return redirect('/')
        #raise Http404
    else:
      print("entrei else")
      books = catalog.objects.only("book")

      try:
        print("entrei try")
        client = clients.objects.get(nif=nif)
      
      except clients.DoesNotExist:
        print("entrei excepcao")
        messages.info(request, 'NIF not found! Please register client!')
        return render(request,'clientregister.html', {'nif':nif})
        #raise Http404
      
      context = {
                'client': client,
                'books' : books
                }

      if selector == 'checkoutbook':
        print("selector check out book")
        return render(request,'checkoutbook.html',context)

      elif selector == 'checkinbook':
        print("selector check in book")
        #books_by_nif = catalog.objects.only('book').filter(id=nif)
        #backlogs = backlog.objects.all()
        backlog_by_nif = backlog.objects.all().filter(user_id=nif)
        if not backlog_by_nif: # empty query
          messages.info(request, 'Costumer has no rented books!')
          return render(request,'clientmanager.html')
        else:
          print('else')
        contextII = {
          'client'          : client,
          'context'         : context,
          'backlog_by_nif'  : backlog_by_nif,
          #'books_by_nif'    : books_by_nif
          #'backlogs'        : backlogs,
        }
        return render(request,'checkinbook.html',contextII)

      elif selector == 'clientbacklog':
        print("selector client back log")
        #books_all = catalog.objects.all()
        books_by_nif = catalog.objects.only('book').filter(id=nif)
        backlogs = backlog.objects.all()
        backlog_by_nif = backlog.objects.all().filter(user_id=nif)
        contextI = {
          'client'          : client,
          'context'         : context,
          'backlogs'        : backlogs,
          'backlog_by_nif'  : backlog_by_nif,
          'books_by_nif'    : books_by_nif
          #'books_all'       : books_all,
        }
        return render(request,'clientbacklog.html', contextI)

      elif selector == 'clientregister':
        print('selector client register')
        messages.info(request, 'NIF already in the system!')
        return redirect('/')
        #return clientregister(request)
        #return render(request,'clientregister.html', context)

      else:
        print("else")
        return render(request,'clientmanager.html')
  else:
    print("estou no Else if do POST")
    return render(request,'clientmanager.html')