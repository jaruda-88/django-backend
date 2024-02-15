from django.db import models
from server_project.settings import AUTH_USER_MODEL


class Category(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return f"{self.name}"
    

ARTICLE_TYPES = [
    ("UN", "Unspecified"),
    ("TU", "Tutorial"),
    ("RS", "Research"),
    ("RW", "Review"),
]


class Article(models.Model):
    title = models.CharField(max_length=256)
    author = models.ForeignKey(to=AUTH_USER_MODEL, on_delete=models.CASCADE)
    type = models.CharField(max_length=2, choices=ARTICLE_TYPES, default="UN")
    categories = models.ManyToManyField(to=Category, blank=True, related_name="categories")
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author}: {self.title} ({self.create_at.date()})"