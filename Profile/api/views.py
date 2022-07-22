
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import SignUpForm,ProfileForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from .serializers import ProfileSerializers, UserSerializers
from .models import Profile


# Create your views here.
@api_view(['GET'])
def getUsers(request):
    profile = Profile.objects.all()
    serializers = ProfileSerializers(profile,many=True)
    return Response(serializers.data)
@api_view(['GET','POST'])
def signin(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = request.data["username"] #form.cleaned_data.get('username')
            password = request.data["password"] #form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                
                return redirect("view-profile")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request,"signin.html", {"login_form":form})
def registerview(request):
    form= SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  
            # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')

            # login user after signing up
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            # redirect user to home page
            return redirect('view-profile')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def logoutview(request):
    logout(request)
    return redirect("signin")
@api_view(['GET'])
def viewProfile(request):
   
    return  render(request,"profileview.html",)

def editProfile(request):
    profile=request.user.profile
    form= ProfileForm(instance=profile)
    if request.method=='POST':
        form=ProfileForm(request.POST,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('view-profile')
    return render(request,'index.html',{'form':form}) 