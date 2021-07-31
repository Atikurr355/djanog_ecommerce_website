from django.db import models
from .category import Category

class Product(models.Model):
    name = models.CharField(max_length=70)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    desc = models.CharField(max_length=200, default="")
    image = models.ImageField(upload_to="product_image/")
    slug = models.CharField(max_length=70)

    def __str__(self):
        return self.name


    @staticmethod
    def get_all_products():
        return Product.objects.all()


    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category= category_id)
        else:
            return Product.get_all_products()

