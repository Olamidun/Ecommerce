from django.shortcuts import redirect, render
from users.forms import StoreCustomerForm
from django.contrib import messages
# Create your views here.


def register(request):
    if request.method == "POST":
        form = StoreCustomerForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password('password')
            first_name = form.cleaned_data.get('first_name')
            messages.success(request, f'{first_name} you have signed up successfully!')
            return redirect('users:login')
        else:
            messages.error(request, 'Oops! Invalid details, kindly fill in the form again!')
            return redirect('users:register')
    else:
        form = StoreCustomerForm()
        context = {'form': form}
    return render(request, 'users/register.html', context)
