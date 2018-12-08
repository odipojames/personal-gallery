from django.db import models

# Create your models here.

class Places(models.Model):
    location = models.CharField(max_length= 40)

    def __str__(self):
        return self.location

class Category(models.Model):
    category = models.CharField(max_length= 30)

    def __str__(self):
        return self.category

class Image(models.Model):
    name = models.CharField(max_length= 50)
    description = models.TextField()
    location = models.ForeignKey(Places)
    category = models.ForeignKey(Category)
    image = models.ImageField(upload_to='pictures/')

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    @classmethod
    def delete_image(cls,id):
        image = cls.objects.filter(id = id)
        image.delete()

    @classmethod
    def get_image(cls,id):
        image = cls.objects.filter(id = id)

        return image

    @classmethod
    def search_image(cls,search_term):
        image = cls.objects.filter(category__category__icontains= search_term)

        return image

    @classmethod
    def view_image(cls, town):
        image = cls.objects.filter(location=town)

        return image

    @classmethod
    def image_cat(cls, category):
        image = cls.objects.filter(category=category)

        return image
