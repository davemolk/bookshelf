from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


from autoslug import AutoSlugField


class Book(models.Model):
    title = models.CharField("Book Title", max_length=255)
    slug = AutoSlugField("Book Slug",
        unique=True, always_update=False, populate_from="title")
    author = models.CharField(max_length=255, blank=True)
    notes = models.TextField("Description", blank=True)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={"slug": self.slug})