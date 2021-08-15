from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.


class Book(models.Model):
    # id = models.BigAutoField(primary_key=True, auto_created=True) this will be added in every models by django3.2
    # id = models.AutoField() this will be added in every models by django in old versions
    title = models.CharField(max_length=200, unique=True)
    rating = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(null=True, max_length=100, db_index=True)
    is_bestselling = models.BooleanField(default=False)
    published_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)  # Harry Potter 1 => harry-potter-1

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        # print(f"Make URL for:{self.id}")
        return reverse("book_detail", args=[self.slug])

    def __str__(self):
        return f"{self.title}  ({self.rating})"



