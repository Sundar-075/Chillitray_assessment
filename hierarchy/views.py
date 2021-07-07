from django.db import connection
from django.http.response import HttpResponse
from rest_framework.response import Response
from hierarchy.serializers import TableSerializer
from hierarchy.models import Table
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
import requests
# Create your views here.


class TableView(generics.ListAPIView):

    serializer_class = TableSerializer
    queryset = Table.objects.all()


def get_view():
    serializer_data = Table.objects.all()
    data = []
    for single in serializer_data:
        data.append(TableSerializer(single).data)
    value, root, connections = dict(), [], dict()
    for one in data:
        connections[one['si_no']] = []
        value[one['si_no']] = one['title']
        if one['parent_id'] is None:
            root.append(one['si_no'])
        else:
            connections[one['parent_id']].append(one['si_no'])
    # print(value, root, connections)
    visited = []

    def dfs(i, value, connections, visited, mul):

        if i in visited:
            return ""
        visited.append(i)
        res = "&emsp;"*mul+"-"+value[i]+"<br/><br/>"
        if connections[i] != []:
            for j in connections[i]:
                res += dfs(j, value, connections, visited, mul+1)
        # print(i, res)
        return res

    data = []
    for i in value.keys():
        if i not in visited:
            if i in root and connections[i] == []:
                data.append("-"+value[i]+"<br/><br/>")
            else:
                res = dfs(i, value, connections, visited, 0)
                data.append(res)

    # print(data)

    return data


class AddView(APIView):

    serializer_class = TableSerializer

    def post(self, request, format=None):

        if request.method == "POST":

            serializer = self.serializer_class(data=request.data)

            if serializer.is_valid():
                title = serializer.data.get('title')
                parent = serializer.data.get('parent_id')
                table = Table(title=title, parent_id=parent)
                table.save()

                return Response({}, status=status.HTTP_200_OK)

        return Response({'Bad request': "Invalid data or method"}, status=status.HTTP_400_BAD_REQUEST)


def index(request, format=None):
    return render(request, "hier.html", {'pres': False})


def show(request, format=None):
    if request.method == "POST":
        data = get_view()
        # print(data)
        # return render(request, "hier.html", {'data': data, 'pres': True})
        res = "".join(data)
        return HttpResponse("<p> "+res+"</p>")
