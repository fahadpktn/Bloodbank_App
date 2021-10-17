from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import JsonResponse
from .models import donors
from django.contrib import messages
from django.contrib.auth.models import User, auth


# Create your views here.
def Home(request):
    user=request.session.get('username')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            request.session['id'] = user.id
            request.session['username']=user.username

            
            return JsonResponse({'success': True},safe=False)
        else:
            
            return JsonResponse({'success': False},safe=False)
    elif(user):
        return redirect('/display')
    else:
        return render(request, "login.html",{'user':user})




def Signup(request):
    user=request.session.get('username')
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if (password1 == password2):
            if User.objects.filter(username=username):
                messages.info(request, "username already in use")
                return redirect('/signup')
            elif User.objects.filter(email=email):
                messages.info(request, "Email already in use")
                return redirect('/signup')
            else:
                users = User.objects.create_user(
                    first_name=first_name, last_name=last_name, username=username, email=email, password=password1)
                users.save()
                return redirect('/')
        else:
            messages.info(request, "Password not matching")
        return redirect('/signup') 
    elif(user):
        return redirect('/display')
    else:
        return render(request, "signup.html",{'user':user})


def Logout(request):
    try:
        request.session.flush()
    except:
        pass    
    return redirect("/")



def Display(request):
    user=request.session.get('username') 
    if(user):
        data = donors.objects.all() 
        return render(request, "display.html", {'data': data,'user': user})
    else:
        return redirect("/")    


def AddDonor(request):
    user=request.session.get('username') 
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        group = request.POST['group']
        Age = request.POST['Age']
        donor = donors(name=name, phone=phone, blood=group, age=Age)
        donor.save()
        return redirect('/display')
    elif(user):
        user=request.session.get('username')
        return render(request, "add-donor.html",{'user':user})
    else:
        return redirect("/")     


 
