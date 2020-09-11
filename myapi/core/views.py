from django.shortcuts import render
from django.http import JsonResponse

#third party imports
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from . serializers import PostSerializer
from rest_framework import generics,mixins
from . models import Post

class PostView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self,request, *args, **kwargs):
        return self.list(request,*args,**kwargs)

    def get(self,request, *args, **kwargs):
        return self.create(request,*args,**kwargs) 

class PostCreateView(generics.CreateAPIView): 
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self,request, *args, **kwargs):
        return self.create(request,*args,**kwargs) 

class PostListCreateView(generics.ListCreateAPIView):  
    serializer_class = PostSerializer
    queryset = Post.objects.all()      
          

        


"""class TestView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request, *args, **kwargs):
        qs = Post.objects.all()
        post = qs.first()
        serializer = PostSerializer(qs,many=True)
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()    
            return Response(serializer.data)
        return Response(serializer.errors)"""