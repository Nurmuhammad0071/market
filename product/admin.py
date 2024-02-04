from django.contrib import admin
from django.forms import ModelForm

from .models import Category, Size, Color, Product, ProductImage, Price


# Inlines
class CategoryInline(admin.TabularInline):  # or admin.StackedInline for a different layout
    model = Category
    extra = 1


class SizeInline(admin.TabularInline):  # or admin.StackedInline for a different layout
    model = Size


class ColorInline(admin.TabularInline):  # or admin.StackedInline for a different layout
    model = Color
    extra = 1


class ColorInline(admin.TabularInline):  # or admin.StackedInline for a different layout
    model = Color
    extra = 1


# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['created_at', 'updated_at']
    search_fields = ['title']
    inlines = [SizeInline, ColorInline]

    # inlines = []


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['created_at', 'updated_at']
    search_fields = ['title']
    # inlines = []


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['created_at', 'updated_at']
    search_fields = ['title']

    # inlines = []


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'slug', 'text']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['created_at', 'updated_at']
    search_fields = ['title']

    # inlines = []


@admin.register(ProductImage)
class PrImageAdmin(admin.ModelAdmin):
    list_display = ['product']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['product']


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ['product']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['count']

