from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.
def sample(request):
    return HttpResponse("hello world")

def sample1(request):
    return HttpResponse("welcome to django")

def sampleInfo(request):
   # data={"name":"sumanth","age":25,"city":"hyd"}
   data={"result":[5,6,7,8]}
   return JsonResponse(data)

def dynamicResponce(request):
    name=request.GET.get("name","kiran")
    city=request.GET.get("city","hyd")
    return HttpResponse(f"hello {name} from {city}")


def math(request):
    # Get values from query string or use defaults
    a = int(request.GET.get("a", 10))
    b = int(request.GET.get("b", 5))
    operation = request.GET.get("operation", "add")

    # Perform the requested operation
    if operation == "add":
        result = a + b
    elif operation == "sub":
        result = a - b
    elif operation == "mul":
        result = a * b
    elif operation == "div":
        result = a / b if b != 0 else "undefined (division by zero)"
    else:
        return HttpResponse("Invalid operation. Use add, sub, mul, or div.")

    return HttpResponse(f"Operation: {operation}, Result: {result}")