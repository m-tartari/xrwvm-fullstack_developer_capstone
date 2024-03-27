from django.db import models
# from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    """
    Represents a car make.

    Attributes:
        name (str): The name of the car make.
        description (str): The description of the car make.
    """

    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class CarModel(models.Model):
    """
    Represents a car model.

    Attributes:
        car_make (CarMake): The car make associated with the car model.
        name (str): The name of the car model.
        type (str): The type of the car model (e.g., Sedan, SUV, Wagon).
        year (int): The year of the car model.
    """

    car_make = models.ForeignKey(
        CarMake, on_delete=models.CASCADE)  # Many-to-One relationship
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(
        default=2023,
        validators=[MaxValueValidator(2023),
                    MinValueValidator(2015)])

    def __str__(self):
        return self.name
