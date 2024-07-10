from django.shortcuts import render, redirect
from MedicioApp.models import Contact, Appoint


# Create your views here.
def index(request):
    return render(request, 'index.html')

def inner(request):
    return render(request, 'inner-page.html')

def about(request):
    return render(request, 'about.html')

def doctors(request):
    return render(request, 'doctors.html')

def departments(request):
    return render(request, 'departments.html')

def contact(request):
    if request.method == 'POST':
        all = Contact(name=request.POST['name'],
                      email=request.POST['email'],
                      phone=request.POST['phone'],
                      message=request.POST['message'],
                      )
        all.save()
        return redirect('/contact')

    else:
        return render(request, 'contact.html')

def appointments(request):
    if request.method == 'POST':
        appoint = Appoint(name=request.POST['name'],
                      email=request.POST['email'],
                      phone=request.POST['phone'],
                      date=request.POST['date'],
                      department=request.POST['department'],
                      doctor=request.POST['doctor'],
                      message=request.POST['message'],
                      )

        appoint.save()
        return redirect('/appointments')

    else:
        return render(request, 'appointments.html')

def show(request):
    information = Appoint.objects.all()
    return render(request, 'show.html', {'data': information})

def delete(request, id):
    myappointment = Appoint.objects.get(id=id)
    myappointment.delete()
    return redirect('/show')
