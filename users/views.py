from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
