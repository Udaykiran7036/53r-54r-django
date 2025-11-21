from django.http import JsonResponse
import re,json
from .models import Users

class basicMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
       # print(request,"hello")
        if(request.path=="/student/"):
           print(request.method,"method")
           print(request.path)
        response=self.get_response(request)
        return response


# class signupMiddleware:
#     def __init__(self,get_response):
#         self.get_response=get_response
#     def __call__(self,request):
#         data=json.loads(request.body)
#         username=data.get("username")
#         email=data.get("email")
#         dob=data.get("dob")
#         password=data.get("pswd") #uday123 firoiuq39re38f
#         #check eusername rules with regex
#         #check email rules with regex
#         #check dob rules with regex
#         #check password rules with regex


class sscMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
            if(request.path in ["/job1/","/job2/"]):
                ssc_result=request.GET.get("ssc")
                print(ssc_result,"hello")
                if(ssc_result !='True'):
                    return JsonResponse({"error":"u should qualify atleast ssc for applying this job"},status=400)   
            return self.get_response(request)



class MedicalMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
            if(request.path == "/job1/"):
                medical_fit_result=request.GET.get("medically_fit",False)
                if(medical_fit_result !='True'):
                    return JsonResponse({"error":"u not medically fit to apply for this job role"},status=400)
            return self.get_response(request)
        

class AgeMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
            if(request.path in ["/job1/","/job2/"]):
                Age_checker=int(request.GET.get("age",17))
                if(Age_checker >25 and Age_checker <18):
                    return JsonResponse({"error":"age must be in 18 and 25"},status=400)
                return self.get_response(request)
            




class UsernameMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        if (request.path == "/signup/"):
              data=json.loads(request.body)
              username=data.get("username","")
              #checks user name is empty or not 
              if not username:
                   return JsonResponse({"error":"username is required"},status=400)
              #checks length
              if len(username)<3 or len(username)>20:
                   return JsonResponse({"error":"username should contains 3 to 20 characters"},status=400)
              #checks starting and ending
              if username[0] in "._" or username[-1] in "._":
                   return JsonResponse({"error":"username should not starts or emds with . or _"},status=400)
              #checks allowed characters
              if not re.match(r"^[a-zA-Z0-9._]+$",username):
                   return JsonResponse({"error":"username should contains only letters,numbers,dot,underscore"},status=400)
              #checks .. and __
              if ".." in username or "__" in username:
                   return JsonResponse({"error":"cannot have .. or __"},status=400)
        return self.get_response(request)
    


class EmailMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
          if (request.path == "/signup/"):
               data=json.loads(request.body)
               email=data.get("email","")
               #checks email empty or not
               if not email:
                    return JsonResponse({"erroe":"email should not empty"},status=400)
               #checks basic email format
               if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",email):
                    return JsonResponse({"error":"invalid email format"},status=400)
               #checks email is duplicate or not
               if Users.objects.filter(email=email).exists():
                    return JsonResponse({"error":"duplicate email"},status=400)
          return self.get_response(request)  # means: "OK, I am done. Send the request to the next middleware or the view."

class PasswordMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
          if (request.path == "/signup/"):
               data=json.loads(request.body)
               password=data.get("password","")
               #checks password empty or not
               if not password:
                    return JsonResponse({"error":"password should not empty"},status=400)
               #checks passsword At least 1 uppercase,At least 1 lowercase, At least 1 number,At least 1 special character ,Minimum 8 characters
               if not re.match(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z0-9@$!%*?&]{8,}$",password):
                    return JsonResponse({"error":"password At least 1 uppercase,At least 1 lowercase, At least 1 number,At least 1 special character ,Minimum 8 characters"},status=400)
          return self.get_response(request)
               

