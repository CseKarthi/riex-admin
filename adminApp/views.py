from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from .models import Institution
import uuid

# Create your views here.

def admin(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    if request.method=="POST":
        user=User.objects.filter(username=request.POST['username'])
        if not user.exists():
            messages.info(request,"Account not found!.")
            return redirect("login")
        elif user.exists():
            user=authenticate(username=request.POST['username'],password=request.POST['password'])
            login(request,user,backend='django.contrib.auth.backends.ModelBackend')
            return redirect('dashboard')
        else:
            messages.error(request,"Invalid Username or Password")
            return redirect("login")
    return render(request,'login.html')


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect("login")
    data={
        "title":"Super Admin Dashboard",
        "user":request.user,
    }
    return render(request,'dashboard.html',context=data)

def logout_user(request):
    logout(request)
    return redirect("login")


def updateProfile(request):
    if not request.user.is_authenticated:
        return redirect("login")
    if request.method=="POST":
       request_file = request.FILES['pro_img'] if 'pro_img' in request.FILES else None
       filepath=''
       if request_file:
           fs=FileSystemStorage(location='user_profile',base_url='user_profile')
           file = fs.save(request_file.name, request_file)
           filepath=fs.url(file)
       user=User.objects.get(id=request.user.id)
       user.first_name=request.POST['firstName']
       user.email=request.POST['email']
       if filepath!='':
            user.img='/'+filepath
       user.save()

       messages.success(request,"Profile Updated Successfully")
       return redirect('updateProfile') 

    data={
        "title":"Super Admin - Update Profile",
        "user":request.user,
    }
    return render(request,'userProfile.html',context=data)

def newInstitution(request):
    if not request.user.is_authenticated:
        return redirect("login")
    if request.method=='POST':
        request_file = request.FILES['ins_logo'] if 'ins_logo' in request.FILES else None
        filepath=''
        if request_file:
           fs=FileSystemStorage(location='user_profile',base_url='user_profile')
           file = fs.save(request_file.name, request_file)
           filepath=fs.url(file)
        user=User(first_name=request.POST['insName'],email=request.POST['emailId'],username=request.POST['username'],
                  password=request.POST['password'],user_role=4,img=filepath)
        user.save()
        usr=User.objects.filter(email=request.POST['emailId'])
        if usr.exists():
            uId=User.objects.get(email=request.POST['emailId'])
            ins=Institution(authId=uId.id,insGUID=uuid.uuid4(),insName=request.POST['insName'],addr1=request.POST['addr'],
                            city=request.POST['city'],state=request.POST['state'],pinCode=request.POST['pincode'],
                            country=request.POST['country'],phone=request.POST['phone'],contactPerson=request.POST['personName'])
            ins.save()
            messages.success(request,"Institution Created Successfully")
            return redirect('newInstitution') 
        else:
            messages.error(request,"Something went wrong. Try Again!...")
            return redirect('newInstitution') 

    data={
        "title":"Super Admin - Create New Institution",
        "user":request.user,
    }
    return render(request,'new_institution.html',context=data)

def institution(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    institutions=Institution.objects.all()
    data={
        "title":"Super Admin - Create New Institution",
        "user":request.user,
        "institutions":institutions
    }
    return render(request,'institution.html',context=data)


