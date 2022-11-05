from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.

operation_type = str
x = int
y = int
result = int
slack = str('femi')

def index(request):
    return render(request, 'index.html')

def answer(request):
    result = ""
    x = int(request.POST['num1'])
    y = int(request.POST['num2'])
    operation_type = request.POST['operation_type']
    
    #Opereations
    if operation_type == '+':
        result = x + y
    elif operation_type == '-':
        result = x - y
    elif operation_type == '*':
        result = x * y 
    else:
        print("You have netered an invalid operation {}".format(operation_type))
        
    return JsonResponse({'slackUsername' : slack, 'result': result, 'operation_type': operation_type})
        