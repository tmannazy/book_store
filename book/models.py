from django.db import models


# Create your models here.

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
