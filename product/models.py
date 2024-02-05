from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Category(BaseModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.title


class Size(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sizes')
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.title


class Color(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='colors')
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.title


class Product(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)  # Bu sana buyicha unique qilingan
    text = models.TextField()

    def __str__(self):
        return self.title


class ProductImage(BaseModel):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True, related_name='image')
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f"Image for Product: {self.product.title}"


class Price(BaseModel):
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name='prices_by_size')
    color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name='prices_by_color')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='prices')
    product_img = models.ManyToManyField(ProductImage)
    count = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Option for Product: {self.product.title}"
