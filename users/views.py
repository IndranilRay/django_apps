from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


def register(request):
    # print('======inside function============')
    if request.method == 'POST':
        # print("request method received")
        form = UserRegisterForm(request.POST)
        # print("Is form valid {}".format(form.is_valid()))
        if form.is_valid():
            # print('it is a valid form')
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    print("request method is {}".format(request.method))
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')

