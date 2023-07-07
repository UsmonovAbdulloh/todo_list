from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TodoModel
from rest_framework.permissions import IsAuthenticated
from .serializers import TodoModelSerializer
from rest_framework import generics
from .permissions import IsOwnerPermission

# Create your views here.
#class CreateTodoView(APIView):
#    def post(self,request,*args,**kwargs):
#        try:
#            task = request.data['task']
#        except KeyError:
#            return Response({'message':'Please send task'},400)
#        t = TodoModel()
#        t.task = task
#        t.save()
#
#        return Response({'message':'Object created successfully'},201)
#
#class DetailTodo(APIView):
#    def get(self,request,*args,**kwargs):
#        data = get_object_or_404(TodoModel,pk=kwargs['todomodel_id'])
#        return Response({'id':data.id,'task':data.task,'created_at':data.created_at})
#
#class ListItems(APIView):
#    def get(self,request):#
#        result = []
#        all_data = TodoModel.objects.all()
#        for todo in all_data:
#            result.append({'id':todo.pk,'task':todo.task,'created_at':todo.created_at,'updated_at':todo.updated_at,'status':todo.status})
#        return Response(result)

#class UpdateStatus(APIView):
#    def patch(self,request,*args,**kwargs):
#        todo = get_object_or_404(TodoModel,pk=kwargs['todomodel_id'])
#        if not todo.status:
#            todo.status = True
#            todo.updated_at = datetime.now()
#            todo.save()
#        return Response({'message':'success'})
#
#class DeleteTodomodel(APIView):
#    def delete(self,request,*args,**kwargs):
#        todo = get_object_or_404(TodoModel,pk=kwargs['todomodel_id'])
#        todo.delete()
#        return Response({'message':'deleted'})
#
#class UpdateTodomodel(APIView):
#    def patch(self,request,*args,**kwargs):
#        todo = get_object_or_404(TodoModel,pk=kwargs['todomodel_id'])
#        if 'task' in request.data:
#            todo.task = request.data['task']
#            todo.save()
#        return Response({'message': 'success'})

class GetStatusView(APIView):
    def get(self,request,*args,**kwargs):
        status = True if kwargs['status']=='true' else False
        all_todos = TodoModel.objects.filter(status=status)

        result = []
        for todo in all_todos:
            result.append({
                'id':todo.id,
                'task':todo.task,
                'status':todo.status,
                'created_at':todo.created_at,
                'updated_at':todo.updated_at
            })
        return Response(result)
        return Response(data)

class DetailUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoModelSerializer
    permission_classes = (IsOwnerPermission,)

class AllCreateTodoView(generics.ListCreateAPIView):
    queryset = TodoModel
    serializer_class = TodoModelSerializer
    permission_classes = (IsOwnerPermission,)
