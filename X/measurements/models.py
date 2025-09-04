from django.db import models
class UserMeasurement(models.Model):
    height = models.FloatField(help_text="User height in centimeters")
    weight = models.FloatField(help_text="User weight in kilograms")
    size = models.CharField(max_length=10, help_text="Suitable size")

    def __str__(self):
        return f"{self.height} cm, {self.weight} kg - Size: {self.size}"