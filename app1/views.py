from django.shortcuts import render,redirect

from django.http import HttpResponse
from django.contrib import messages

from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import UserRegisterForm, Articleform
from .decorators import unauthenticated_user, allowed_users,admin_only

from .models import Profile,Articles
def home(request):
    return render(request, 'base.html')
def register_user(request):
  
	form = UserRegisterForm()
	if request.method == "POST":
		roles = request.POST.get('roles')
		email = request.POST.get('email')
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			# user = form.save(commit=False)
			# user.username = user.username.lower()
			# user.is_active = False
			# user.save()
			# user.groups.add(group)
			user = form.save()
			username = form.cleaned_data.get('username')

			group, created = Group.objects.get_or_create(name=roles)
			user.groups.add(group)

			Profile.objects.create(
				user=user,
				username=user.username,
				email=user.email,
				
			)

			return redirect('login')

			messages.success(request, "User was created successfully")
	context = {'form':form}
	return render(request, 'Signup.html', context)









"""
crud operation
where only the admin and developer can delete or add or update the tables
others only have the rights to view the table

"""
@allowed_users(allowed_roles=['admin','Developer','HR','Manager','Reviewer'])
@login_required(login_url='login')
def get_articles(request):
	data= Articles.objects.all()
	print(data)
	context={'data':data}
	return render(request, 'articles.html', context)





@allowed_users(allowed_roles=['admin','Developer'])
@login_required(login_url='login')
def article_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = Articleform()
        else:
            article = Articles.objects.get(pk=id)
            form = Articleform(instance=article)
        return render(request, "article_form.html", {'forms': form})
    else:
        if id == 0:
            form = Articleform(request.POST)
        else:
            article = Articles.objects.get(pk=id)
            form = Articleform(request.POST,instance= article)
        if form.is_valid():
            form.save()
        return redirect('/')


@allowed_users(allowed_roles=['admin','Developer'])
@login_required(login_url='login')
def article_delete(request,id):
    article = Articles.objects.get(pk=id)
    article.delete()
    return redirect('/')





