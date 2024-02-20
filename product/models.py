import random

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from unidecode import unidecode
from django.utils.text import slugify


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Category(BaseModel):
    title = models.CharField(max_length=255, verbose_name=_('Category Title'))
    slug = models.SlugField(max_length=255, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.title)) + '_' + slugify(random.randint(1, 60))
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Size(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sizes')
    title = models.CharField(max_length=255, verbose_name=_('Size title'))
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.title)) + '_' + slugify(random.randint(1, 60))
        return super().save(*args, **kwargs)


class Color(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='colors')
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.title)) + '_' + slugify(random.randint(1, 60))
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Product(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)  # Bu sana buyicha unique qilingan
    text = models.TextField()
    detail = models.TextField()
    discount_id = models.ForeignKey('product.Discount', on_delete=models.CASCADE, null=True, blank=True,
                                    related_name='prices_by_discount')
    currency_ids = models.ForeignKey('product.Currency', on_delete=models.CASCADE, related_name='prices_by_currency')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.title)) + '_' + slugify(random.randint(1, 60))
        return super().save(*args, **kwargs)


class Price(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='prices')
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name='prices_by_size')
    color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name='prices_by_color')
    count = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Option for Product: {self.product.title}"


class ProductImage(BaseModel):
    prise_id = models.ForeignKey(Price, on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f"Image for Product: {self.prise_id.product.title}"


class Comment(BaseModel):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comment")
    name = models.CharField(max_length=255, null=True)
    email = models.EmailField(null=True)
    text = models.TextField()
    reating = models.PositiveIntegerField(default=0)


class Discount(BaseModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    count = models.PositiveIntegerField()
    discount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title[:10]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.title)) + '_' + slugify(random.randint(1, 60))
        return super().save(*args, **kwargs)


class Currency(BaseModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=5)

    def __str__(self):
        return self.title[:10]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.title)) + '_' + slugify(random.randint(1, 60))
        return super().save(*args, **kwargs)
