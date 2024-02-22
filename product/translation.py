# model translation imports
from modeltranslation.translator import register, TranslationOptions
from .models import Category, Size, Color, Product


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'text')
