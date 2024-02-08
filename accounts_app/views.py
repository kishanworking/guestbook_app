

# Create your views here.
from django.shortcuts import render,redirect,HttpResponse
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.views.generic import View



from django.contrib.auth.forms import UserCreationForm


class IndexPage(View):
    template_name = "home.html"
    def get(self, request):
        return render (request, 'accounts/home.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password = password)
            login(request, user)
            return redirect('home')

    else:
        form = UserCreationForm()

    context = {'form' : form }
    return render(request, 'registration/register.html', context)






# class SignupPage(View):
#     template_name = "accounts/signup.html"

#     def get(self, request):
#         return render(request, self.template_name)
    
#     def post(self, request):
#         uname = request.POST.get('username')
#         email = request.POST.get('email')
#         pass1 = request.POST.get('password')
#         pass2 = request.POST.get('confirmPassword')

#         if pass1 != pass2:
#             return HttpResponse('conform pass is different')
#         else:
#             my_user = User.objects.create_user(uname,email,pass1)
#             my_user.save()
#             return redirect('login')

# class LoginPage(View):
#     template_name = "accounts/login.html"

#     def get(self,request):
#         return render(request, self.template_name)
    
#     def post(self, request):
#         username = request.POST.get('username')
#         pass1 = request.POST.get('pass')
#         user = authenticate(request,username=username,password=pass1)
#         if user is not None:
#             login(request,user)
#             return redirect('home')
#         else:
#             return HttpResponse("username or password is incorrect")


# class LogoutPage(View):
#     def get(self, request):
#         logout(request)
#         return redirect('login')