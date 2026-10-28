from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework.response import Response

from . models import Cake,Category,Weight,Shape

from . serializers import CakeSerializer,CategorySerializer,WeightSerializer,ShapeSerializer

from rest_framework.authentication import BasicAuthentication,TokenAuthentication

from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly

from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

from authentication.permissions import IsAdmin,IsUser

from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.

class CakeListCreateView(APIView):

    serializer_class = CakeSerializer

    authentication_classes=[JWTAuthentication]

    # permission_classes=[IsAuthenticated]

    def get_permissions(self): # MO

        permissions = []

        if self.request.method == 'POST':

            permissions = [IsAdmin]

        return [permission() for permission in permissions]

    def get(self,request,*args,**kwargs):

        cakes = Cake.objects.all()

        # data = {'cakes':cakes} we can't do this because Cake.objects.all() returns complex datatype. it has to be converted to python native type, for that we use serializer.

        serializer = self.serializer_class(cakes,many=True) # many=True cuz in default serializer only converts one set of record
        
        return Response(serializer.data,status=200) # return serializer.data

    def post(self,request,*args,**kwargs):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(): # checks if all values recieved from frontend are valid (eg: make sure we did'nt recieves pdf instead of jpg)

            serializer.save() # save everything to db (no need of orm queries)

            data = {'msg':'cake created successfully'}

            return Response(data,status=201)
        
        return Response(serializer.errors,status=400) # returns the errors from recieved values from frontend (only works if if statement didnt work)

class CakeRetrieveUpdateDestroyView(APIView):

    serializer_class = CakeSerializer

    def get(self,request,*args,**kwargs):

        id = kwargs.get('id')

        cake = Cake.objects.get(id=id)

        serializer = self.serializer_class(cake)

        return Response(serializer.data,status=200)

    def patch(self,request,*args,**kwargs):

        id = kwargs.get('id')
        
        cake = Cake.objects.get(id=id)

        serializer = self.serializer_class(instance=cake,data=request.data,partial=True)

        if serializer.is_valid():

            serializer.save()

            data = {'msg':'cake updated successfully'}

            return Response(data,status=200)

        return Response(serializer.errors,status=400)

    def delete(self,request,*args,**kwargs):

        id = kwargs.get('id')
                
        cake = Cake.objects.get(id=id)

        cake.delete()

        data = {'msg':'cake is deleted successfully'}

        return Response(data,status=200)


class CategoryCreateListView(ListCreateAPIView):

    queryset = Category.objects.all()

    serializer_class = CategorySerializer # this includes both get and post

class CategoryRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):

    queryset = Category.objects.all()

    serializer_class = CategorySerializer

class ShapeCreateListView(ListCreateAPIView):

    queryset = Shape.objects.all()

    serializer_class = ShapeSerializer # this includes both get and post

class ShapeRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):

    queryset = Shape.objects.all()

    serializer_class = ShapeSerializer

class WeightCreateListView(ListCreateAPIView):

    queryset = Weight.objects.all()

    serializer_class = WeightSerializer # this includes both get and post

class WeightRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):

    queryset = Weight.objects.all()

    serializer_class = WeightSerializer