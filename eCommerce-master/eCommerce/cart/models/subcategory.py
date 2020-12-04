from django.db import models
from .category import Category


class Subcategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE , default="")


    @staticmethod
    def get_all_products_by_categoryid(category_name):
        if category_name:
            return Subcategory.objects.filter(category=category_name)
        else:
            return None


    def __str__(self):
        return self.name


