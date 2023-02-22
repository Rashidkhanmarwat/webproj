from django.shortcuts import render, HttpResponse
from student.models import StdBio

# Create your views here.
def home(request):
    
    return render(request,"home.html",{})

    #return HttpResponse("This is first Home page")
def stdadd(request):
    if request.method == 'POST':
        roll = request.POST.get('roll')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        std = StdBio(rollno = roll, name = name, email = email, phone = phone, address=address)
        std.save()
    return render(request,"addstd.html",{ })