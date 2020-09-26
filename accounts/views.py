from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout

def signup(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_lists:lists')
    else:
        form = UserCreationForm()
    return render(request,'accounts/signup.html',{'forms_are':form})

# IMPORTANT: DON'T GIVE FUNCTION NAME AS LOGIN
# DJANGO WILL GET CONFUSED WITH LOGIN FUCNTION SO YOU'LL GET ERROR
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('article_lists:lists')

    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{'forms_are':form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('article_lists:lists')