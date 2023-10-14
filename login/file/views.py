from django.shortcuts import render

# Create your views here.
def view2(request):
    return render(request,'signup.html')
def view1(request):
    if(request.method=="POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')
    return render(request, 'home.html',{'un':username,'pw':password})