from django.shortcuts import render
from myceleryproject.celery import add 
from .tasks import sub
from celery.result import AsyncResult

def index(request):
    # result = add.delay(10,20)
    # using apply_async which is same as delay
    result = add.apply_async(args=[10,20])
    # result2 = sub.delay(20,10)
    print("result :",result)
    # print("result2 :",result2)
    
    return render(request,'index.html',{'result':result})

def result(request,task_id):
    result = AsyncResult(task_id)  
    return render(request,'results.html',{'result':result})

def about(request):
    print("result :")
    return render(request,'about.html')

def contact(request):
    print("result :")
    return render(request,'contact.html')
