from django.shortcuts import render
from django.http import HttpResponse
from service.models import Service

from .forms import UsersForm


def index(request):
    servicesData=Service.objects.all()
    #sending the data from the table to the website using data dictionaries.
    data={'servicesData':servicesData}
    return render(request, "index.html",data)


def about(request):
    return render(request, "about.html")


def blog(request):
    return render(request, "blog.html")


def shop(request):
    return render(request, "shop.html")


def test(request):
    data = {
        "Name": "Yash Chauhan",
        "Course": "Btech ",
        "Year": "3rd year",
        "description": "He is a good software developer and Website developer",
        "skills": ["PHP", "java", "Python "],
        "clist":
          [
            {'name':'pradeep','phone':9269698122},
            {'name':'testing','phone':909696981225}
          ]
    }
    return render(request, "testing.html", data)

def form (request):
   finalans=0
   try:
    n1=int(request.POST.get('num1'))
    n2=int(request.POST.get('num2'))
    finalans=n1+n2
   except:
    pass 
    return render(request,"userform.html",{'output':finalans})
   

def submitform(request):
  try:
     if request.method=='POST':
        n1=int(request.POST.get('num1'))
        n2=int(request.POST.get('num2'))
        finalans=n1+n2
        data={
        'n1':n1,
        'n2':n2,
        'output':finalans
        }
        return HttpResponse(finalans)
  except:
     pass


def calculate(request):
   data={}
   try:
      if(request.method=="POST"):
         number1=eval(request.POST.get('num1'))
         number2=eval(request.POST.get('num2'))
         data={'add':number1+number2,
               'sub':number1-number2,
               'mul':number1*number2,
               'div':number1/number2,
               }
         return render(request,"calculator.html",data)
   except:
      pass  
   return render(request,"calculate.html",data)


def evenodd(request):
   try:
      if(request.method=="POST"):
         
         if((request.POST.get('number'))==''): #if space is encountered in input return an error key
            return render(request,"evenodd.html",{'error':True})
         elif(eval(request.POST.get('number'))%2==0):
            return render(request,"evenodd.html",{'answer':'even'}) #if the input is even then return the answer key as the value of even 
         else:
            return render(request,"evenodd.html",{'answer':'odd'}) #if the input is odd then return the answer key as the value of odd
   except:
      return render(request,"evenodd.html",{'answer':'invalid input please input numbers '})
   return render(request,"evenodd.html",{'answer':'',})


def marksheet(request):
     data={}
     if(request.method=='POST'):
         s1=eval(request.POST.get('sub1'))
         s2=eval(request.POST.get('sub2'))
         s3=eval(request.POST.get('sub3'))
         s4=eval(request.POST.get('sub4'))
         s5=eval(request.POST.get('sub5'))
         total=s1+s2+s3+s4+s5
         per=(total)*100/500
         data={'total':total,
               'percentage':per,
               }       
         return render(request,'marksheet.html',data)
     return render(request,'marksheet.html',data)
