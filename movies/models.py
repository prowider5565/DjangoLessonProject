from django.db import models


class Movie(models.Model):
    """
    Model representing a movie.
    """
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='movies/images/', blank=True, null=True)
    video = models.FileField(upload_to='movies/videos/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    release_date = models.DateField()
    rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "movies"