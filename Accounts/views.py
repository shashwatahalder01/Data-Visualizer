from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model, authenticate
from django.contrib import auth
from Dashboard.views import dashboard
from .forms import sign , log
from django.contrib import messages 
from django import forms
from Gdriveapi.views import connectDrive,fileDownload, insertintoDb

User=get_user_model()


def signup(requests):
    form=sign(requests.POST or None)
    if requests.method == 'POST':
        
        if form.is_valid():
        # # print(form.cleaned_data)
        # # print(form.cleaned_data.get("username"))
        # # print(form.cleaned_data.get("email"))
        # # print(form.cleaned_data.get("password"))
            username=form.cleaned_data.get("username").lower()
            email=form.cleaned_data.get("email").lower()
            password=form.cleaned_data.get("password")

            user = User.objects.create_user(username=username,email=email,password=password)
            user.save()
            return redirect('/') 
        
        else:
            html={'title':'Signup' , 'form':form}
            link='accounts/signup.html'
            return render(requests,link,html)
                       
    else:
        html={'title':'Signup' , 'form':form}
        link='accounts/signup.html'
        return render(requests,link,html)

    

def login(requests):
    if requests.user.is_authenticated:
        return redirect('dashboard/')
    else:
        form=log(requests.POST or None)    
        if requests.method == 'POST':
            if form.is_valid():
                username=form.cleaned_data.get("username").lower()
                password=form.cleaned_data.get("password")
                user=authenticate(requests,username=username,password=password)
                if user is not None:
                    auth.login(requests,user)
                    # session = connectDrive()
                    # fileDownload(session)
                    # insertintoDb()
                    return redirect('dashboard/')
                    # html={'title':'Dashboard' }
                    # link='dashboard/dashboard.html'
                    # return render(requests,link,html)
                else:
                    html={'title':'Login' , 'form':form}
                    link='accounts/login.html'
                    return render(requests,link,html)
                
            else:
                html={'title':'Login' , 'form':form}
                link='accounts/login.html'
                return render(requests,link,html) 
            
        else:
            html={'title':'Login' , 'form':form}
            link='accounts/login.html'
            return render(requests,link,html)



def logout(requests):
    auth.logout(requests)
    return redirect('/')