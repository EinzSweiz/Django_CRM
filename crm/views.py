from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from crm.forms import UserCreateForm, RecordCreateForm
from crm.models import Records
from django.http import HttpResponseNotFound
from django.core.exceptions import ValidationError
def get_home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have been logged in')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Username and password are required')
        # Return to the same page with error messages
        return render(request, 'crm/home.html', {'records': Records.objects.all()})
    
    records = Records.objects.all()
    return render(request, 'crm/home.html', {'records': records})

def delete_record(request, record_id):
    if request.user.is_authenticated:
        record = Records.objects.get(pk=record_id)
        record.delete()
        messages.success(request, 'Record have been successfully deleted')
        return redirect('home')
    else:
         messages.success(request, "You need to be logged in to delete the Record")
         return redirect('home')

def add_records(request):
    form = RecordCreateForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            add_record = form.save()
            messages.success(request, 'Your record added successfully')
            return redirect('home')
        else:
            messages.error(request, 'There was an error in the form submission.')
    return render(request, 'crm/record_add.html', {'form':form})

def login_user(request):
    pass


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('home')


def register_user(request):
	if request.method == 'POST':
		form = UserCreateForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = UserCreateForm()
		return render(request, 'crm/register.html', {'form':form})

	return render(request, 'crm/register.html', {'form':form})

def show_record(request, record_id):
    record = Records.objects.get(pk=record_id)
    if record:
        return render(request, 'crm/record.html', {'record': record})
    else:
         return HttpResponseNotFound('Unfortunately the page is not found')
    


def update_record(request, record_id):
    record = get_object_or_404(Records, pk=record_id)
    form = RecordCreateForm(request.POST or None, instance=record)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Everything passed successfully')
            return redirect('home')
        else:
            messages.error(request, 'Something went wrong, please try again')
    else:
        return render(request, 'crm/update_record.html', {'form': form})