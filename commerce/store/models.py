from django.db import models
from django.utils import timezone
from django.conf import settings
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from autoslug import AutoSlugField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from store.utils.fileupload import category_image_upload_path, product_gallery_image_upload_path, user_directory_path

# Create your models here.
# utility: soft delete
class NonDeleted(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)
 
class SoftDelete(models.Model):
    is_deleted = models.BooleanField(default=False)
    deleted_date = models.DateTimeField(null=True, blank=True)
    everything = models.Manager()
    objects = NonDeleted()
 
    def toggle_soft_delete(self):
        if self.is_deleted and not self.deleted_date:
            self.deleted_date = timezone.now()
        elif not self.is_deleted:
            self.deleted_date = None

    def save(self, *args, **kwargs):
        self.toggle_soft_delete()
        super().save(*args, **kwargs)
 
    def soft_deleted(self):
        self.is_deleted = True
        self.toggle_soft_delete()
        self.save()
 
    def restore(self):
        self.is_deleted = False
        self.toggle_soft_delete()
        self.save()
 
    class Meta:
        abstract = True
        

# model: category
class Category(SoftDelete):
    title       = models.CharField(max_length=100, unique=True)
    slug        = AutoSlugField(populate_from='title')
    image       = models.ImageField(upload_to=category_image_upload_path, blank=True, null=True)
    image_300x300 = ImageSpecField(
        source="image",
        processors=[ResizeToFill(300, 300)],
        format="WebP",
        options={"quality": 80},
    )
    
    panels = [
        FieldPanel("title"),
        FieldPanel("image"),
    ]
    
    class Meta:
        verbose_name_plural = "Categories"
        
    def delete(self):
        self.deteled=True
        self.save()
        
    def __str__(self):
        return self.title

    # def get_url(self):
    #     return reverse("core:category-product-list", kwargs={"category_slug": self.slug})