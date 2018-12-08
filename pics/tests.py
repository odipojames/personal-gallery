from django.test import TestCase
from .models import *
# Create your tests here.
class ImageTest(TestCase):

    # creating a setup for the test
    def setUp(self):
        self.new_town = Places.objects.create(location = 'kisumo')
        self.new_category = Category.objects.create(category = 'sports')
        self.new_image = Image.objects.create(name = 'image', description = 'james jatugo', location = self.new_town, category = self.new_category)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))

    def test_delete(self):
        self.new_image.save()
        self.new_image.delete()
        self.assertTrue(len(Image.objects.all()) == 0)

    def test_get_image(self):
        self.new_image.save()
        image = Image.get_image(1)
        self.assertTrue(len(image) == 0)

    def test_search_image(self):
        self.new_image.save()
        image = Image.search_image('sports')
        self.assertTrue(len(image) > 0)

    def test_view_image(self):
        self.new_image.save()
        image = Image.view_image(self.new_town)
        self.assertTrue(len(image) > 0)

    def test_image_cat(self):
        self.new_image.save()
        image = Image.image_cat(self.new_category)
        self.assertTrue(len(image) > 0)
