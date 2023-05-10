from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from APP_TODO.models import Task
from APP_TODO.serializer import ToDoSerializer,ToDoSerializer2
# Create your views here.

class ToDoTaskAPI(APIView):

    # get all tasks
    def get(self,request):
        
        quri = Task.objects.all()
        serializer = ToDoSerializer(quri,many = True)
        return Response(serializer.data,status=200)
    
    # add new tasks
    def post(self,request):
        data=request.data
        serialiser = ToDoSerializer(data=data)
        try:
            if serialiser.is_valid():
                serialiser.save()
                return Response({
                    "msg":"the task added"
                })  
            return Response(serialiser.errors)
        except Exception as e:
            print(e)
            return Response({"msg":"exception"})
        
class TaskAPI(APIView):

    # get a single task
    def get(self,request,id):
        
        quri = Task.objects.get(id=id)
        serializer = ToDoSerializer(quri)
        return Response(serializer.data,status=200)
    
    # update a single task
    def put(self,request,id):
        data = request.data
        try:
            quri = Task.objects.get(id=id)
        except Task.DoesNotExist:
            return Response({"msg":"the reques does not exist"})
        serializer = ToDoSerializer2(quri,data,partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"The Task is Updated"})
        else:
            return Response({"msg":"The task can't be updated!!"})

    # delete a single task   
    def delete(self,request,id):
        try:
            task = Task.objects.get(id=id)
            task.delete()
            return Response({"msg":"The task is deleted"})
        except Exception as e:
            return Response({"msg":"The task is not able to delete"})


        
        