from django.db import models

# Create your models here.

# class CategoryChoices(models.TextChoices):

#     BIRTHDAY_CAKE = 'Birthday Cake','Birthday Cake'

#     WEDDING_CAKE = 'Wedding Cake','Wedding Cake'

# class WeightChoices(models.TextChoices):

#     HALF_KG = '1/2 kg','1/2 kg'

#     ONE_KG = '1 kg','1 kg'

#     TWO_KG = '2 kg','2 kg'

# class ShapeChoices(models.TextChoices):

#     RECTANGLE = 'Rectangle','Rectangle'

#     ROUND = 'Round','Round'

class Category(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):

        return self.name

    class Meta:

        verbose_name = 'Category'

        verbose_name_plural = 'Category'

class Weight(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):

        return self.name

    class Meta:

        verbose_name = 'Weights'

        verbose_name_plural = 'Weights'

class Shape(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):

        return self.name

    class Meta:

        verbose_name = 'Shapes'

        verbose_name_plural = 'Shapes'

class Cake(models.Model):

    name = models.CharField(max_length=20)

    description = models.TextField()

    photo = models.ImageField(upload_to='cake-images')

    category = models.ForeignKey('Category',on_delete=models.CASCADE) # used to decide what happe ns to the cake model when the created category is deleted

    # on_delete = models.CASCADE to delete the whole cake record

    # on_delete = models.SET_NULLL to set null to the category section of that cake model
    
    weight = models.ForeignKey('Weight',on_delete=models.CASCADE)

    shape = models.ForeignKey('Shape',on_delete=models.CASCADE)

    price = models.FloatField()

    def __str__(self):

        return self.name

    class Meta:

        verbose_name = 'Cake'

        verbose_name_plural = 'Cake'