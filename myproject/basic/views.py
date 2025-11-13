from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.db import connection
import json
from django.views.decorators.csrf import csrf_exempt
from basic.models import Student
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

#to test database connection 
def health(request):
    try:
        with connection.cursor() as c:
            c.execute("SELECT 1")
        return JsonResponse({"status":"ok","db":"connected"})
    except Exception as e:
        return JsonResponse({"status":"error","db":str(e)})

@csrf_exempt
def addStudent(request):
    print(request.method)
    if request.method=="POST":
        data=json.loads(request.body)
        student=Student.objects.create(
            name=data.get('name'),
            age=data.get("age"),
            email=data.get("email")
            )
        return JsonResponse({"status":"success","id":student.id},status=200)
    return JsonResponse({"error":"use post method"},status=400)

