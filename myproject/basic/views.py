from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.db import connection
import json
from django.views.decorators.csrf import csrf_exempt
from basic.models import Student,Users
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
    
    elif request.method=="GET":
        result=list(Student.objects.values())
        print(result)
        return JsonResponse({"status":"ok","data":result},status=200)
    

    elif request.method=="PUT":
        data=json.loads(request.body)
        ref_id=data.get("id") #getting id
        new_email=data.get("email") #getting email
        existing_student=Student.objects.get(id=ref_id) #fetched the object as per the id
        # print(existing_student)

        existing_student.email=new_email #updating with new email
        existing_student.save()
        updated_data=Student.objects.filter(id=ref_id).values().first()
        return JsonResponse({"status":"data update successfully","upload_data":"upload data"},status=200)
    elif request.method=="DELETE":
        data=json.loads(request.body)
        ref_id=data.get("id") #getting id
        get_delting_daata=Student.objects.filter(id=ref_id).values().first()
        to_be_delete=Student.objects.get(id=ref_id)
        to_be_delete.delete()

        return JsonResponse({"status":"success","message":"student record deletd successfully","deleted data":get_delting_daata},status=200)
    return JsonResponse({"error":"use post method"},status=400)


def job1(request):
    return JsonResponse({"message":"u have successfully applied for job1"},status=200)
def job2(request):
    return JsonResponse({"message":"u have successfully applied for job2"},status=200)


@csrf_exempt
def signUp(request):
    if request.method=="POST":
        data=json.loads(request.body)
        print(data)
        user=Users.objects.create(
            username=data.get("username"),
            email=data.get("email"),
            password=data.get("password")
            )
        return JsonResponse({"status":"success"},status=200)


