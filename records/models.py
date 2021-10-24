from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


from autoslug import AutoSlugField


class Record(models.Model):
    title = models.CharField("Record Title", max_length=255)
    slug = AutoSlugField("Record Slug",
        unique=True, always_update=False, populate_from='title')
    notes = models.TextField("Notes", blank=True)
    record_url = models.URLField("URL", blank=True)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('record_detail', kwargs={'slug': self.slug})


