from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.models import *
import json

# Create your views here.
# Prefix all views with `m_`.

def m_api_q_list(request):
    items = Question.objects.all()
    items_list = []
    for x in items:
        items_list.append(x.id)
    return HttpResponse(json.dumps(items_list), content_type="application/json")

def m_api_q_stat(request, id: int):
    return_t = {}
    if Question.objects.filter(id=id).exists():
        q = Question.objects.get(id=id)
        return_t["ok"] = True
        return_t["title"] = q.q_title
        return_t["content"] = q.q_content
        return_t["answers"] = []
        for x in Answer.objects.filter(a_question=q).values_list("id"):
            return_t["answers"].append(x[0])
    else:
        return_t["ok"] = False
    return HttpResponse(json.dumps(return_t), content_type="application/json",status=200 if return_t["ok"] else 404)

def m_api_a_stat(request, id: int):
    return_t = {}
    if Answer.objects.filter(id=id).exists():
        a = Answer.objects.get(id=id)
        return_t["ok"] = True
        return_t["question"] = a.a_question.id
        return_t["content"] = a.a_content
    else:
        return_t["ok"] = False
    return HttpResponse(json.dumps(return_t), content_type="application/json",status=200 if return_t["ok"] else 404)

def m_gui_ask_post(request):
    if request.method == "POST":
        ip = request.META["REMOTE_ADDR"]
        data = request.POST
        try:
            title = data["title"]
            content = data["content"]
        except KeyError:
            return render(request, "ask_error.html",{"status": "Missing Data"},status=400)
        q = Question.objects.create(q_ip=ip,q_title=title,q_content=content)
        q.save()
        return render(request, "ask_return.html",{"id": q.id})

def m_gui_ask(request):
    return render(request, "ask.html")

def m_gui_question(request, id: int):
    return_t = {}
    if Question.objects.filter(id=id).exists():
        q = Question.objects.get(id=id)
        return_t["ok"] = True
        return_t["title"] = q.q_title
        return_t["content"] = q.q_content
        return_t["answers"] = []
        for x in Answer.objects.filter(a_question=q).values_list("id"):
            return_t["answers"].append(x[0])
        return render(request, "question.html",return_t)
    else:
        return render(request, "ask_error.html",{"status": "Not Found"},status=404)

def m_gui_answer(request, id: int):
    return_t = {}
    if Answer.objects.filter(id=id).exists():
        a = Answer.objects.get(id=id)
        return_t["q_id"] = a.a_question.id
        return_t["content"] = a.a_content
        return_t["q_title"] = a.a_question.q_title
        return render(request, "answer.html",return_t)
    else:
        return render(request, "ask_error.html",{"status": "Not Found"},status=404)

def m_gui_list(request):
    items = Question.objects.all()
    return render(request, "question_list.html",{"questions": items})




