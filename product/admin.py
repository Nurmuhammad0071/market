from django.contrib import admin
from django.forms import ModelForm

from .models import Category, Size, Color, Product, ProductImage, Price, Discount, Currency, Comment


# Inlines
class CategoryInline(admin.TabularInline):  # or admin.StackedInline for a different layout
    model = Category
    extra = 1


class SizeInline(admin.TabularInline):  # or admin.StackedInline for a different layout
    model = Size


class ColorInline(admin.TabularInline):  # or admin.StackedInline for a different layout
    model = Color
    extra = 1


class PriseInline(admin.TabularInline):  # or admin.StackedInline for a different layout
    model = Price
    extra = 1


class ImageInline(admin.TabularInline):  # or admin.StackedInline for a different layout
    model = ProductImage
    extra = 1


class DiscountInline(admin.TabularInline):  # or admin.StackedInline for a different layout
    model = Discount
    extra = 1


class CurrencyInline(admin.TabularInline):  # or admin.StackedInline for a different layout
    model = Currency
    extra = 1


# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['title']
    inlines = [SizeInline, ColorInline]
    readonly_fields = ['slug']
    # inlines = []


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ['title']
    # prepopulated_fields = {'slug': ('title',)}
    list_filter = ['created_at', 'updated_at']
    # search_fields = ['title']
    # inlines = []
    readonly_fields = ['slug']


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['title']
    readonly_fields = ['slug']
    # inlines = []


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'slug', 'text']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['title']
    inlines = [PriseInline]
    readonly_fields = ['slug']
    # inlines = []


@admin.register(ProductImage)
class PrImageAdmin(admin.ModelAdmin):
    list_display = ['prise_id']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['prise_id']


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ['product', 'size', 'color', 'count', 'price', 'discount_price']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['count']
    inlines = [ImageInline]


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['title']
    readonly_fields = ['slug']


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['title']
    readonly_fields = ['slug']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['product_id', 'name', 'email', 'text']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['name']
    # inlines = []
