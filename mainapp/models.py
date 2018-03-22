from django.db import models

# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField(verbose_name="Название", max_length=100, unique=True)
    desciption = models.TextField(verbose_name="Описание", blank=True)
    image = models.ImageField(verbose_name="Изображение", upload_to="product_images", blank=True)


class Product(models.Model):
    name = models.CharField(verbose_name="Название", max_length=100, unique=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name="Изображение", upload_to="product_images", blank=True)
    short_desc = models.CharField(verbose_name="Кратко", max_length=200, blank=True)
    description = models.TextField(verbose_name="Описание", blank=True)
    price = models.DecimalField(verbose_name="Стоимость", max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name="Количество", default=0)

    def __str__(self):
        return "{} ({})".format(self.name, self.category.name)
