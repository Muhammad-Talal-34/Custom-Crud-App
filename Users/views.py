# from django.shortcuts import render ,redirect
# from Users.forms import CustomRegistrationForm


# def Home(request):
#     return render(request,'base.html')


# def RegisterUser(request):  
#     if request.method =='POST':
#         form = CustomRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = CustomRegistrationForm()

#     return render(request,'UsersTemplate/RegisterUser.html', {'form':form})

# def UserProfile(request):
#     return render(request , 'UsersTemplate/Profile.html')

# def Users_view(request):
#      users_list = User.objects.all()
#      context = {'users' :users_list}

#      return render(request,'UsersTemplate/users.html',context)
# def AddUser(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         age = request.POST.get('age')
#         image = request.FILES.get('image')


#         User.objects.create(
#             u_name = name,
#             u_email = email,
#             u_age = age,
#             u_image = image,
          
#         ) 
       
        
#         return redirect('/users/')
#     return render(request,'UsersTemplate/addUser.html')


# def UpdateUser(request, id):
#    user = User.objects.get(id=id)
#    if request.method == 'POST':
#       name = request.POST.get('name')
#       age = request.POST.get('age')
#       email = request.POST.get('email')
#       image =request.FILES.get('image')

#       user.u_name = name
#       user.u_email = email

#       user.u_age = age
#       if image:
#          user.u_image = image
#       user.save()
#       return redirect('users')
#    return render(request, 'UsersTemplate/UpdateUser.html', context={'user': user})   

# def  DeleteUser(request,id) :
#     user = User.objects.get(id=id)
#     user.delete()
#     return redirect('users')