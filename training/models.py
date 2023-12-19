from django.db import models


class Training(models.Model):
    """
    A model of the training for the user
    """

    Training_name = models.CharField(max_length=20, null=True, blank=True)
    Distance = models.DecimalField(max_digits=4, decimal_places=2)
    # todo Time
    Average_speed = models.DecimalField(max_digits=2, decimal_places=2)
    # todo Training_type
    Base_score = models.IntegerField(null=True, blank=True)
    Date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Training_name
