from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateform,ProfileUpdateForm
def register(request):
	if request.method=='POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username')
			messages.success(request,f'Your account has been created! You are now able to login ')
			return redirect('login')
	else:	
		form= UserRegisterForm()
	context= {'form':form}
	return render(request,'users/register.html',context)

@login_required
def profile(request):
	if request.method=='POST':
		u_form=UserUpdateform(request.POST, instance=request.user)
		p_from=ProfileUpdateForm(request.POST,
		 request.FILES,
		 instance=request.user.profile)
		if u_form.is_valid() and p_from.is_valid():
			u_form.save()
			p_from.save()
			messages.success(request,f'Your account has been updated')
			return redirect('profile')
	else:
		u_form=UserUpdateform(instance=request.user)
		p_from=ProfileUpdateForm(instance=request.user.profile)

	context= {
		'u_form':u_form,
		'p_from':p_from
	}
	return render(request, 'users/profile.html',context)