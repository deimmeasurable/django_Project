from django.db import models


# Create your models here.
class Cohort(models.Model):
    number = models.IntegerField(default=0, unique=True)
    name = models.CharField(max_length=42)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


GENDER = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('others', 'Others')
)


class Native(models.Model):
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    gender = models.TextField(max_length=10, choices=GENDER, default='others')
    number = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=42)
    last_name = models.CharField(max_length=42)
    date_of_birth = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True)
    # cohort = models.ForeignKey(Post, on_delete=models.CASCADE)


def __str__(self) -> str:
    return self
