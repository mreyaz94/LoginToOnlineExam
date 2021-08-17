from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from webapp.forms import SignUpForm
from django.http import HttpResponseRedirect

# Create your views here.
def home_page_view(request):
    return render(request,'webapp/home.html')

@login_required
def java_exam_view(request):
    return render(request,'webapp/javaexam.html')

@login_required
def python_exam_view(request):
    return render(request,'webapp/pythonexam.html')

@login_required
def aptitude_exam_view(request):
    return render(request,'webapp/aptitudeexam.html')

def logout_view(request):
    return render(request,'webapp/logout.html')

def sign_up_view(request):
    form=SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        # if form.is_valid():
        #     form.save()
        user = form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'webapp/signup.html', {'form':form})