from django.shortcuts import render, redirect
from MedicioApp.models import Contact, Appoint, Member, ImageModel
from MedicioApp.forms import AppointmentForm, ImageUploadForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'],
                                 password=request.POST['password'],
                                 ).exists():
            members = Member.objects.filter(username=request.POST['username'],
                                            password=request.POST['password'], )
            return render(request, 'index.html', {'members': members})
        else:
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


def edit(request, id):
    appointment = Appoint.objects.get(id=id)
    return render(request, 'edit.html', {'x': appointment})


def update(request, id):
    if request.method == 'POST':
        appointment = Appoint.objects.get(id=id)
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('/show')

        else:
            return render(request, 'edit.html')

    else:
        return render(request, 'edit.html')


def register(request):
    if request.method == "POST":
        members = Member(name=request.POST['name'],
                         username=request.POST['username'],
                         password=request.POST['password'],
                         )
        members.save()
        return redirect('/login')

    else:
        return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/showimage')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})


def show_image(request):
    images = ImageModel.objects.all()
    return render(request, 'show_image.html', {'images': images})


def imagedelete(request, id):
    image = ImageModel.objects.get(id=id)
    image.delete()
    return redirect('/showimage')
