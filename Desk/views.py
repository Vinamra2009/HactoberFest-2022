from django.shortcuts import render, redirect
# from django.views import Views
# from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm

# Create your views here.#csc
def index(request):
    return render(request, 'Desk/index.html')
def add_a_book(request):
    return render(request, 'Desk/add_a_book.html')


def aboutus(request):
    return render(request, 'Desk/about_us.html')

def loginPage(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
    context = {'page': page}
    return render(request, "Desk/login_register.html", context)


def logoutPage(request):
    logout(request)
    return redirect("index")


def registerPage(request):
    page = 'register'
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            user = authenticate(request, username=user.username, password=request.POST['password1'])
            print(user)

            if user is not None:
                login(request, user)
                return redirect("index")

    context = {"form": form, "page": page}
    return render(request, "Desk/login_register.html", context)
