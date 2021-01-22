from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 255, db_index = True)
    slug = models.SlugField(max_length = 255, unique = True) 
    
    # Slug - an addressable unit. For example '\admin\shop\category' is a slug as it addresses that part of that domain
    # A slug is essentially saving an addressable link in the database

    class Meta:
        verbose_name_plural = 'categories'
    # Meta is to provide more information in the table. Its data abot data. Provides more information in different parts of the system.

    def __str__(self):
        return self.name
    # Double Underscore (Dunder) Methods are special methods that allow to perform different methods. 
    # The above applies the default name for data that is returned for the database. 
    

#class Image(models.Model):
#    name = models.CharField(max_length = 255)
#    decription = models.CharField(max_length = 255)
#    image = models.ImageField(upload_to = 'images/')
#    primary_image = models.BooleanField(default = False)
#    is_active = models.BooleanField(default = False)
#    width = models.FloatField(default = 100)
#    length = models.FloatField(default = 100#)
#    album = models.ForeignKey(
#        ImageAlbum, related_name = 'images', on_delete = models.CASCADE)
#    created = models.DateTimeField(auto_now_add = True)
#    updated = models.DateTimeField(auto_now = True)

#    def __str__(self):
#        return self.name

#class Product(models.Model):
#    category = models.ForeignKey (
#        Category, related_name = 'product', on_delete = models.CASCADE)
#    title = models.CharField(max_length = 255)
#    author = models.CharField(max_length = 255, default = 'unknown')
#    description = models.TextField(blank = True)
#    slug = models.SlugField(max_length = 255)
#    price = models.DecimalField(max_digits = 4, decimal_places = 2)
#    in_stock = models.BooleanField(default = True)
#    album = models.OneToOneField(
#        ImageAlbum, related_name = 'model', on_delete = models.CASCADE)
#    is_active = models.BooleanField(default = True)
#    created = models.DateTimeField(auto_now_add = True)
#    updated = models.DateTimeField(auto_now = True)

#    class Meta: 
#        verbose_name_plural = 'Products'

#    def get_absolute_url(self):
#        return reverse('store:product_detail', args = [self.slug])

#   def __str__(self):
#        return self.title
    