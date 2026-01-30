from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserRegisterForm, StudentForm
from .format_data import clean_questionaire_data, get_right_answers




from collections import OrderedDict
# Create your views here.


import requests



def home(request):

    return render(request,'home.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request,'User account was created!')
            login(request,user)
            
            return redirect('edit-account')

        
    return render(request,'account/signup.html',{'form':form})


@login_required(login_url='loginPage')
def editAccount(request):
    profile = request.user.student
    form = StudentForm(instance=profile)

    if request.method == "POST":
        form = StudentForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()

        return redirect('home')

    context = {'form':form}
    return render(request,'account/profile.html', context)




def dashboard(request):
    return render(request,'dashboard/dashboard.html')


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'Username does not exist')
            print("email")


        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Username or Password is incorrect')
    return render(request,'account/login.html')



def logoutUser(request):
    logout(request)
    return redirect('home')



@login_required(login_url='loginPage')
def exam(request):

    return render(request, 'exam/exam.html')



@login_required(login_url='loginPage')
def exam_site(request):
    # if request.session.get('exam_taken'):
    #     return redirect('home')  # or show "you already took the test"
    # request.session['exam_started'] = True
    
    test = requests.get("https://opentdb.com/api.php?amount=5&type=multiple")


    questionaire = clean_questionaire_data(test.json()['results'])

    correct_answers = get_right_answers(test.json()['results'])

    request.session['correct_answers'] = correct_answers

    context = {'data':questionaire}
    return render(request, 'exam/exam-site.html', context)


def exam_result(request):
    if request.method == "POST":
        correct_answersData = request.session.get('correct_answers')
        # request.session['exam_taken'] = True
        # request.session.pop('exam_started', None)
        result = {}

        print(correct_answersData)
        for key, value in request.POST.items():
            if "question_" in key:
                question_index = key.split("_")[1]
                if correct_answersData[question_index] == value:
                    result[question_index] = "correct"
                else:
                    result[question_index] = "wrong"


        sorted_result = OrderedDict(sorted(result.items()))



        return render(request, 'exam/exam-result.html', {'answers': sorted_result})

    return redirect('exam-site') 

