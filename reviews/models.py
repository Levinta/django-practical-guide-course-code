from django.db import models

# Create your models here.


class Review(models.Model):
    """Review model.""
    """
    user_name = models.CharField(max_length=100)
    review_text = models.CharField(max_length=2000)
    rating = models.IntegerField()

    def __str__(self):
        """Return user name."""
        return f"{self.user_name} rated {self.rating} stars"
