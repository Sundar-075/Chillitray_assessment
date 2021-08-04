from django.http.request import HttpRequest
from django.http.response import HttpResponse, JsonResponse
from requests.sessions import session
from .models import Tasks, User
from django.shortcuts import redirect, render
from .serializers import TaskSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.paginator import Paginator
import requests
from django.contrib.auth.decorators import login_required
import hashlib
# Create your views here.


class UserSignup(APIView):
    serializer_class = UserSerializer

    def get(self, request, format=None):
        username = self.request.GET.get('username')
        password = self.request.GET.get('password')

        if username != "" and username != None and password != "" and password != None:
            serializer = self.serializer_class(data={
                'username': username, 'password': password})
            if serializer.is_valid():

                username = serializer.data.get('username')
                password = serializer.data.get('password')
                result = hashlib.sha256(password.encode())
                password = result.hexdigest()

                user = User(username=username, password=password)
                user.save()

                return Response({'Ok': 'user successfully created'}, status=status.HTTP_200_OK)

            if 'username' in serializer.errors:
                return Response({"invalid_username": 'Please follow the naming conventions', }, status=status.HTTP_406_NOT_ACCEPTABLE)

            if 'password' in serializer.errors:
                return Response({'invalid_password': 'Please change the password'}, status=status.HTTP_406_NOT_ACCEPTABLE)

        return Response({'Bad request': 'Please fill the details'}, status=status.HTTP_400_BAD_REQUEST)


class TaskAddView(APIView):

    serializer_class = TaskSerializer

    def post(self, request, format=None):

        uid = request.POST.get('uid')
        title = request.POST.get('task_title')
        description = request.POST.get('task_description')
        pic = request.FILES.get('task_pic')
        user = User.objects.get(uid=uid)
        # print(pic)
        serializer = self.serializer_class(
            data={'uid': user.pk, 'task_title': title, 'task_description': description, 'task_pic': pic if pic != "" else None})

        if serializer.is_valid():
            serializer.save()

            return Response({'Ok': 'user successfully created'}, status=status.HTTP_200_OK)

        if serializer.errors:

            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'Bad request': "No data"}, status=status.HTTP_400_BAD_REQUEST)


class TaskGetView(APIView):

    def get(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        uid = request.GET.get('uid')
        tasks = Tasks.objects.filter(uid=uid).values(
            'task_title', 'task_description', 'task_pic', 'create_time_stamp')

        tasks_paginator = Paginator(tasks, 5)

        page_no = request.GET.get('page')

        page = tasks_paginator.get_page(page_no)
        # print(page.object_list)

        # return Response(TaskSerializer(page).data, status=status.HTTP_200_OK)
        total_pages = tasks_paginator.num_pages
        # has_previous = True if page.has_previous == True else False

        return Response({'page': page.object_list, 'total': total_pages, 'page_no': page.number}, status=status.HTTP_200_OK)


def Login(request, format=None):
    # if request.session.exists(request.session.session_key):
    #     response = redirect("/")
    #     return response
    return render(request, "Login.html", context={})


def Signup(request, format=None):
    # if request.session.exists(request.session.session_key):
    #     response = redirect("/")
    #     return response

    return render(request, "Signup.html", context={})


# @login_required
def index(request, format=None):
    if request.session.exists(request.session.session_key):
        return render(request, "index.html")
    else:
        response = redirect("login/")

        return response


def signup_code(request, format=None):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username != None and password != None and username != "" and password != "":
            data = requests.get("http://127.0.0.1:8000/signup/", params={
                'username': username, 'password': password}, headers={'Accept': '*/*'}).json()

            # print(data.json())

            if 'invalid_username' or 'invalid_password' in data:
                return render(request, "Signup.html", context=data)

            response = redirect('login')

            return response

        return render(request, "Signup.html", context={"Missing_data": "Provide username and password"})


def Signin(request, format=None):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username != None and username != "" and password != None and password != "":
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                user = None
            if user is not None:
                if user.password == hashlib.sha256(password.encode()).hexdigest():
                    # print(user.uid)
                    request.session['user_id'] = user.uid
                    # print(request.session['userId'])
                    response = redirect("/")
                    return response
                return render(request, "Login.html", context={"Fail": "Password is Wrong"})

            return render(request, "Login.html", context={"Username_fail": "There is no user with that username"})

        return render(request, "Login.html", context={"Missing_data": "Provide username and password"})


def Taskaddfun(request, format=None):
    if request.method == "POST":
        title = request.POST.get('task_title')
        description = request.POST.get('task_description')
        pic = request.FILES.get('task_pic')

        # print("pic", pic)

        if title != None:
            uid = request.session.get('userid')
            data = requests.post("http://127.0.0.1:8000/task-create/", data={
                                 'uid': uid, "task_title": title, "task_description": description}, files={'task_pic': pic})

            # print(data)
            response = redirect('/')

            return response


def GetPages(request, format=None):

    if request.method == "GET":
        page_no = request.GET.get('page')
        uid = request.session.get('user_id')

        page = requests.get("http://127.0.0.1:8000/get-task",
                            params={'page': page_no, 'uid': uid}).json()

        # print(page)
        # for i in page:
        #     print(i)
        return render(request, "Pages.html", page)


def logout(request, format=None):
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return redirect('login')
