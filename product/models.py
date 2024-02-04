# from django.db import models
#
#
# class BaseModel(models.Model):
#     status = models.BooleanField(default=0)
#     created_at = models.DateTimeField(auto_now=True)
#     updated_at = models.DateTimeField(auto_now_add=True)
#
#
# class Category(BaseModel):
#     title = models.CharField(max_length=255)
#     slug = models.SlugField(max_length=255)
#
#
# class Size(BaseModel):
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     title = models.CharField(max_length=255)
#     slug = models.SlugField(max_length=255)
#
#
# class Color(BaseModel):
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     title = models.CharField(max_length=255)
#     slug = models.SlugField(max_length=255)
#
#
# class Product(BaseModel):
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     title = models.CharField(max_length=255)
#     text = models.TextField()
#
#
# class ProductImage(BaseModel):
#     product = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True)
#     image = models.ImageField(upload_to='product_images/')
#
#
# class Price(BaseModel):
#     size = models.ForeignKey(Size, on_delete=models.CASCADE)
#     color = models.ForeignKey(Color, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     price = models.FloatField()
