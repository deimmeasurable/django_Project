from django.db import models

# Create your models here.
from natives.models import Native


class Project(models.Model):
    natives = models.ForeignKey(Native, on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.TextField(
        default="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Image_created_with_a_mobile_phone.png/1200px-Image_created_with_a_mobile_phone.png"
    )
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self
