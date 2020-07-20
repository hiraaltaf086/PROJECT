from django.contrib.auth.models import User
from django.db import models


class ImagesManager(models.Manager):
    def get_queryset(self):
        return super(ImagesManager, self).get_queryset().order_by('-uploaded_at')


class ImageModel(models.Model):
    Image = models.ImageField(upload_to='media/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)

    HEALTHY = 0
    MILD = 1
    MODERATE = 2
    SEVERE = 3
    PROLIFERATIVE = 4

    PREDICTION_OPTIONS = (
        (HEALTHY, 'healthy'),
        (MILD, 'Mild'),
        (MODERATE, 'Moderate'),
        (SEVERE, 'Severe'),
        (PROLIFERATIVE, 'Proliferative'),

    )
    prediction = models.PositiveIntegerField(choices=PREDICTION_OPTIONS, default=None)

    # Model Manager
    objects = models.Manager()
    sorted_images = ImagesManager()
