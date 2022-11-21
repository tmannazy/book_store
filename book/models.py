from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator


# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    website = models.URLField()


class Book(models.Model):
    GENRE_CHOICES = (
        ("C", "Comedy",),
        ("T", "Tragedy"),
        ("TC", "Tragicomedy"),
        ("H", "Horror"),
        ("CR", "Crime"),
        ("R", "Romance"),
        ("SF", "Sci-Fi")
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(db_index=True, default="-")
    isbn = models.CharField(max_length=20)
    date_published = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    date_added = models.DateField(auto_now_add=True)
    edition = models.PositiveSmallIntegerField()
    genre = models.CharField(max_length=2, choices=GENRE_CHOICES, default="R")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name="books")
    authors = models.ManyToManyField("Author", related_name="books")


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)


class Address(models.Model):
    number = models.PositiveSmallIntegerField()
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=6,
                               validators=[MinLengthValidator(5, "code cannot be less than a length of 5"),
                                           MaxLengthValidator(6, "code cannot exceed length of 6")])
    publisher = models.OneToOneField(Publisher, on_delete=models.CASCADE)
