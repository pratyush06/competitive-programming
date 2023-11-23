from django.shortcuts import render
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics, permissions
from rest_framework.reverse import reverse
from rest_framework import renderers
from django.contrib.auth.models import User
from snippets.permissions import IsOwnerOrReadOnly

# Create your views here.
# function based views
@api_view(['GET', 'POST'])
#@csrf_exempt
def snippet_list(request, format=None):
    if request.method=='GET':
        # import pdb;pdb.set_trace()
        snippets= Snippet.objects.all()
        serializer=SnippetSerializer(snippets, many=True)
        # return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)
    
    elif request.method=='POST':
        # data=JSONParser().parse(request)
        # serializer=SnippetSerializer(data=data)
        serializer=SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        # return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def snippet_detail(request, pk, format=None):
    try:
        snippet=Snippet.objects.get(pk=pk)
    
    except Snippet.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serializer=SnippetSerializer(snippet)
        # return JsonResponse(serializer.data)
        return Response(serializer.data)
    
    elif request.method=='PUT':
        # data=JSONParser().parse(request)
        serializer=SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            # return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        # return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
            
    elif request.method=='DELETE':
        snippet.delete()
        # return HttpResponse(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_204_NO_CONTENT)

# class based views
    
# class SnippetList(APIView):
#     def get(self, request, fomrat=None):
#         Snippets=Snippet.objects.all()
#         serializer=SnippetSerializer(Snippets, many=True)
#         return Response(serializer.data)
    
#     def post(self, request, format=None):
#         serializer=SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    

# class SnippetDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Snippet.objects.get(pk=pk)
        
#         except Snippet.DoesNotExist:
#             raise Http404 
    
#     def get(self, request, pk, format=None):
#         snippet=self.get_object(pk)
#         serializer=SnippetSerializer(snippet)
#         return Response(serializer.data)
    
#     def put(self, request, pk, fomrat=None):
#         snippet=self.get_object(pk)
#         serializer=SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk, format=None):
#         snippet=self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# geniric class based views

class HelloView(APIView):
    permission_classes = [permissions.IsAuthenticated,]

    def get(self, request):
        content = {'message': request.user.username}
        return Response(content)

class SnippetList(generics.ListCreateAPIView):
    queryset=Snippet.objects.all()
    serializer_class=SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    # def get_queryset(self):
    #     import pdb;pdb.set_trace()
    #     return Snippet.objects.all().filter(owner=self.request.user)
        # return super().get_queryset()
    
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Snippet.objects.all()
    serializer_class=SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class UserList(generics.ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class USerDetail(generics.RetrieveAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    
class RootView(APIView):
    def get(self, request, format=None):
        return Response({
            'user':reverse('user-list', request=request, format=format),
            'snippets':reverse('snippet-list', request=request, format=format)
        })

class SnippetHighlighted(generics.GenericAPIView):
    queryset=Snippet.objects.all()
    renderer_classes=[renderers.StaticHTMLRenderer]
    
    def get(self, request, *args, **kwargs):
        Snippet=self.get_object()
        return Response(Snippet.highlighted)

## viesets and routers 
from rest_framework import viewsets
from rest_framework.decorators import action
# REST framework includes an abstraction for dealing with ViewSets, that allows the developer
# to concentrate on modeling the state and interactions of the API, and leave the URL
# construction to be handled automatically, based on common conventions.

# ViewSet classes are almost the same thing as View classes, except that they provide
# operations such as retrieve, or update, and not method handlers such as get or put.

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
#This time we've used the ModelViewSet class in order to get the complete set of default
# read and write operations.

# Notice that we've also used the @action decorator to create a custom action, named
# highlight. This decorator can be used to add any custom endpoints that don't fit
# into the standard create/update/delete style.

# Custom actions which use the @action decorator will respond to GET requests
# by default. We can use the methods argument if we wanted an action that responded to POST
# requests.

# The URLs for custom actions by default depend on the method name itself. If you want
# to change the way url should be constructed, you can include url_path as a decorator
# keyword argument.
class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet=self.get_object()
        return Response(snippet.highlighted)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        


# ## upload video to s3
# class FileItem(models.Model):
#     user                            = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
#     name                            = models.CharField(max_length=120, null=True, blank=True)
#     path                            = models.TextField(blank=True, null=True)
#     size                            = models.BigIntegerField(default=0)
#     file_type                       = models.CharField(max_length=120, null=True, blank=True)
#     timestamp                       = models.DateTimeField(auto_now_add=True)
#     updated                         = models.DateTimeField(auto_now=True)
#     uploaded                        = models.BooleanField(default=False)
#     active                          = models.BooleanField(default=True)
# import base64
# import hashlib
# import hmac
# import os
# import time
# from rest_framework import permissions, status, authentication
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .config_aws import (
#     AWS_UPLOAD_BUCKET,
#     AWS_UPLOAD_REGION,
#     AWS_UPLOAD_ACCESS_KEY_ID,
#     AWS_UPLOAD_SECRET_KEY
# )
# from .models import FileItem
# django storages librabry

# from storages.backends.s3boto3 import S3Boto3Storage

# class MediaStorage(S3Boto3Storage):
#     bucket_name = 'my-media-bucket'

# from django_backend.custom_storages import MediaStorage

# class FileUploadView(View):
#     def post(self, requests, **kwargs):
#         file_obj = requests.FILES.get('file', '')

#         # do your validation here e.g. file size/type check

#         # organize a path for the file in bucket
#         file_directory_within_bucket = 'user_upload_files/{username}'.format(username=requests.user)

#         # synthesize a full file path; note that we included the filename
#         file_path_within_bucket = os.path.join(
#             file_directory_within_bucket,
#             file_obj.name
#         )

#         media_storage = MediaStorage()
        
        
#         if not media_storage.exists(file_path_within_bucket): # avoid overwriting existing file
#             media_storage.save(file_path_within_bucket, file_obj)
#             file_url = media_storage.url(file_path_within_bucket)

#             return JsonResponse({
#                 'message': 'OK',
#                 'fileUrl': file_url,
#             })
#         else:
#             return JsonResponse({
#                 'message': 'Error: file {filename} already exists at {file_directory} in bucket {bucket_name}'.format(
#                     filename=file_obj.name,
#                     file_directory=file_directory_within_bucket,
#                     bucket_name=media_storage.bucket_name
#                 ),
#             }, status=400)








   