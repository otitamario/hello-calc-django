from django.shortcuts import render,HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse('Hello World')

def sum(request,a,b):
    op=a+b
    return HttpResponse('<h1>The sum of  {0} and {1} is {2}</h1>'.format(a,b,op))

def sub(request,a,b):
    op=a-b
    return HttpResponse('<h1>The difference of  {0} and {1} is {2}</h1>'.format(a,b,op))

def mult(request,a,b):
    op=a*b
    return HttpResponse('<h1>The multiplication of  {0} and {1} is {2}</h1>'.format(a,b,op))

def div(request,a,b):
    if b!=0:
        op=a/b
        return HttpResponse('<h1>The division of  {0} by {1} is {2}</h1>'.format(a,b,op))
    else:
        return HttpResponse('<h1>Cannot divide the numbers because the divisor is 0</h1>')