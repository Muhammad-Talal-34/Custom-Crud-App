from django.shortcuts import render , redirect , get_object_or_404
from UserAuth.models import *
from django.contrib.auth import authenticate ,login , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import CustomUser


def LandingPage(request):
    return render(request , 'LandingPage.html')

@login_required(login_url='login')
def Dashboard(request):
    return render(request , 'Base.html')

def RegisterUser(request):
    if request.method=='POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('first_name')
        email = request.POST.get('email')
        country_name = request.POST.get('country_name')
        city = request.POST.get('city')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
       

        if password == confirm_password:
            CustomUser.objects.create_user(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                country_name=country_name,
                city = city,
                address = address,
                phone_number = phone_number,
                password  = password,
                
            )
            return redirect('login')
    
    return render(request,'Auth/RegisterUser.html')

def LoginUser (request):
    if request.method == 'POST':
        username_field = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request , username = username_field , password = password)


        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request , 'Auth/Login.html',{'error_message': "invalid details ⚠⚠⚠⚠⚠⚠ "})
    return render(request, 'Auth/login.html')

def LogoutUser (request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def UserProfile(request):

    return render(request ,'Auth/Profile.html')



# Security check specifically for Admin
def is_admin(user):
    return user.is_authenticated and user.role == 'admin'

@login_required(login_url='/login/')
@user_passes_test(is_admin)
def manage_users(request):
    # Fetch all users EXCEPT the currently logged-in admin
    users = CustomUser.objects.exclude(id=request.user.id)
    return render(request, 'Auth/manage_users.html', {'users': users})

@login_required(login_url='/login/')
@user_passes_test(is_admin)
def change_role(request, user_id):
    if request.method == 'POST':
        target_user = get_object_or_404(CustomUser, id=user_id)
        new_role = request.POST.get('role')
        
        # Verify the role is valid before saving
        valid_roles = ['admin', 'manager', 'user']
        if new_role in valid_roles:
            target_user.role = new_role
            target_user.save()
            messages.success(request, f"Role updated for {target_user.username}")
            
    return redirect('manageusers')

@login_required(login_url='/login/')
@user_passes_test(is_admin)
def delete_user(request, user_id):
    if request.method == 'POST':
        target_user = get_object_or_404(CustomUser, id=user_id)
        target_user.delete()
        messages.success(request, "User deleted successfully.")
    return redirect('manage_users')