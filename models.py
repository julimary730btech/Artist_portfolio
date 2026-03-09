from django.db import models

class Artwork(models.Model):
    CATEGORY_CHOICES = (
        ('Mehendi', 'Mehendi'),
        ('Painting', 'Painting'),
        ('Drawing', 'Drawing'),
    )

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='artworks/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()

    def __str__(self):
        return self.title


class Booking(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    event_type = models.CharField(max_length=100)
    date = models.DateField()
    message = models.TextField()

    def __str__(self):
        return self.name