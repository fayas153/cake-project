from rest_framework import serializers

from . models import Cake,Category,Weight,Shape

class CategorySerializer(serializers.ModelSerializer):

    class Meta:

        model = Category

        fields = '__all__'

class WeightSerializer(serializers.ModelSerializer):

    class Meta:

        model = Weight

        fields = '__all__'

class ShapeSerializer(serializers.ModelSerializer):

    class Meta:

        model = Shape

        fields = '__all__'


# normal serializer

# class CakeSerializer(serializers.ModelSerializer):

#     class Meta:

#         model = Cake

#         # fields = ['id','name','photo','description'] # if you want only specific fields

#         # exclude = ['name'] # if you want all fields except name

#         fields = '__all__' # for all fields


# nested serializer

# class CakeSerializer(serializers.ModelSerializer):

#     category = CategorySerializer()

#     weight = WeightSerializer()

#     shape = ShapeSerializer()

#     class Meta:

#         model = Cake

#         fields = '__all__'

class CategoryField(serializers.PrimaryKeyRelatedField):

    def get_attribute(self, instance): # MO

        return getattr(instance,self.source_attrs[0])

    def to_representation(self, value): # MO

        return CategorySerializer(value).data

class WeightField(serializers.PrimaryKeyRelatedField):

    def get_attribute(self, instance):

        return getattr(instance,self.source_attrs[0])

    def to_representation(self, value):

        return WeightSerializer(value).data

class ShapeField(serializers.PrimaryKeyRelatedField):

    def get_attribute(self, instance):

        return getattr(instance,self.source_attrs[0])

    def to_representation(self, value):

        return ShapeSerializer(value).data

class CakeSerializer(serializers.ModelSerializer):

    category = CategoryField(queryset=Category.objects.all())

    weight = WeightField(queryset=Weight.objects.all())

    shape = ShapeField(queryset=Shape.objects.all())

    flag = serializers.SerializerMethodField() # serializer can add fields that does'nt exist in model

    def get_flag(self,obj):

        if obj.price < 1000 : 

            return 'super saver!!!'

        return None
    
    class Meta:
        
        model = Cake

        fields = '__all__'