from django.contrib import admin
from . models import Category

# Register your models here.
admin.site.register(Category)





#EXAMPLE
#class ImageInline(admin.StackedInline):
#    model = Image

#class ProductInline(admin.StackedInline):
#    model = Product

#@admin.register(ImageAlbum)
#class ImageAlbumAdmin(admin.ModelAdmin):
#    inlines = [
#        ProductInline,
#        ImageInline,
#    ]

#admin.site.register(Image)
#admin.site.register(Product)

