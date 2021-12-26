import json
from django.http.response import HttpResponse, JsonResponse
import random
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render



def show_question (request):
    if request.method == "GET" :
        qs = Question.objects.all()
        qs2 = Answer.objects.all()
        temp1 = []
        temp11 = []
          

        temp2=[]
        for k in qs:
            if k.category == "C":
                temp1.append(
                 
                {
                    "سوال" : k.s_question,
                    "گروه سوال" : k.category,
                    
                }
              )
            if k.category == "E":
                temp11.append(
                 
                {
                    "سوال" : k.s_question,
                    "گروه سوال" : k.category,
                    
                }
              )
            
        for l in qs2 :
        
            temp2.append(
                {
                    
                    "option_a" : l.option_a,
                    "option_b" : l.option_b,
                    "option_c" : l.option_c,
                    "option_d" : l.option_d
                }
            )
        a_z1 = list(zip (temp1,temp2))
        a_z2 = list(zip(temp11,temp2))
        t=[]
        t1=[]
        
        t.append(random.sample(a_z1,4))
        t1.append(random.sample(a_z2,4))
        #return JsonResponse({"status" : "successful" , "data" : (t,t1)})
        context = {'data' : (a_z1)}
        return render(request, 'index.html', context)

    else :
        return JsonResponse ({"status" : "eror" , "mesage" : "faghat GET"}, status = 403)

@csrf_exempt
def get_answer (request):
    if request.method == "POST":
        data = json.loads(request.body)
        question_no = data.get("question_no","")
        answer = data.get("answer", "")
        id = int(data.get("id", ""))

        UserAnswer.objects.create(answer=answer,question_no=question_no,user_id=id)
        return JsonResponse({"status" : "successful" , "mesage" : "java shoma sabt shod"}, status = 201)
    else:
        return JsonResponse({"status": "error", "msg": "faghat post mojazeh"}, status=403)
@csrf_exempt
def get_user (request):
    if request.method == "POST":
        data = json.loads(request.body)
        print(data)
        name = data.get("name", "")
        email = data.get("email", "")
        phone_number = data.get("phone_number","")
        MyUser.objects.create(name=name,email=email,phone_number=phone_number)
        return JsonResponse({"status":"successful","mesage":"sabt shod",}, status =201)
    else:
        return JsonResponse({"status": "error", "msg": "faghat post mojazeh"}, status=403)


def show_score(request):
    if request.method == "GET":
        data = UserAnswer.objects.get(user_id = 2)
        data1 = Answer.objects.get(id=2)
        if data.answer == data1.correct_answer:
            return HttpResponse('ok')
        else:
            return HttpResponse("wrong answer")

def test(request):
    return render("iman")

