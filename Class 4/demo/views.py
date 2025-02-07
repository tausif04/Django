from django.shortcuts import render

def data(request):
    # name="Ritu"
    # return render(request,'data.html',{'name':name})
    person ={"Firstname":"Tausif","Lastname":"Bin Mozid","Age":22}
    return render(request,'data.html',{'person':person})

def loop(request):
    # names = ['Ritu','Tausif','Neha','Suman']
    # return render(request,'loop.html',{'names':names})
    data=[('Ritu',20),('Tausif',22),('Neha',25),('Suman',27)]
    temperature=40
    number=44
    return render(request,'loop.html',{'data':data , 'tempt':temperature , 'number':number})


def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def report(request):
    return render(request,'reports.html')