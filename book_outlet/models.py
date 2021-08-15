from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.


class Library(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=16)

    def __str__(self):
        return f"{self.name}({self.code})"

    class Meta:
        verbose_name_plural = "Libraries"


class Address(models.Model):
    street = models.CharField(max_length=100)
    zip = models.CharField(max_length=6)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.street}, {self.city} {self.country}-{self.zip}"

    class Meta:
        verbose_name = "Author's Address"
        verbose_name_plural = "Address Entries"


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Book(models.Model):
    # id = models.BigAutoField(primary_key=True, auto_created=True) this will be added in every models by django3.2
    # id = models.AutoField() this will be added in every models by django in old versions
    title = models.CharField(max_length=200, unique=True)
    rating = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    # author = models.CharField(null=True, max_length=100, db_index=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='books')
    is_bestselling = models.BooleanField(default=False)
    issued_library = models.ManyToManyField(Library)
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




