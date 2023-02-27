from django.shortcuts import render,redirect,HttpResponse
from student.models import StdBio


# Create your views here.
def home(request):
    std = StdBio.objects.all()
    
    return render(request,"home.html",{'std':std})

    #return HttpResponse("This is first Home page")
def stdadd(request):
    if request.method == 'POST':
        roll = request.POST.get('roll')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        std = StdBio(roll = roll, name = name, email = email, phone = phone, address=address)
        std.save()
        return redirect("/home")   
    return render(request,"addstd.html",{ })

def deletestd(request,id):
    s=StdBio.objects.get(pk=id)
    s.delete()
    return redirect("/home")


def updatestd(request,id):
    su=StdBio.objects.get(pk=id)
    return render(request,"updatestd.html",{'su':su})

def doupdatestd(request):
     if request.method == 'POST':
        id = request.POST.get('id')
        roll = request.POST.get("roll")
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
     
        su=StdBio.objects.get(pk=id)
     
        su.name = name
        su.roll = roll
        su.email = email
        su.phone = phone
        su.address = address
        su.save()
        return redirect("/home")
     return render(request,"updatestd.html",{ }) 
