import os
from django.db import models
from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey
from django.utils import timezone
from django.conf import settings
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from autoslug import AutoSlugField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from store.utils.fileupload import category_image_upload_path, product_gallery_image_upload_path, user_directory_path
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager
from userauth.models import User
from store.utils.choice import STATUS_CHOICE, STATUS, RATING

CATEGORY_DEFALT_IMAGE = os.path.join(settings.MEDIA_ROOT, "placeholder/category.png")
VENDOR_COVER_DEFAULT_IMAGE = os.path.join(settings.MEDIA_ROOT, "vendor-header-bg.png")

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
    
#model: vendor
class Vendor(models.Model):
    user                = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title               = models.CharField(max_length=40, unique=True)
    slug                = AutoSlugField(populate_from='title', blank=True, null=True)
    image               = models.ImageField(upload_to=user_directory_path, default=CATEGORY_DEFALT_IMAGE)
    cover_image         = models.ImageField(upload_to=user_directory_path, default=VENDOR_COVER_DEFAULT_IMAGE)
    description         = models.TextField(null=True, blank=True, default="Everyone has to face these problems.  When facing such problems, Understanding clearly what kind of existence the 69 is is the key to solving all problems.")
    address             = models.CharField(max_length=100, default="Jalan no 69")
    contact             = models.CharField(max_length=100, default="+62818181818")
    chat_resp_time      = models.CharField(max_length=100, default="100")
    shipping_on_time    = models.CharField(max_length=100, default="100")
    authentic_rating    = models.CharField(max_length=100, default="100")
    days_return         = models.CharField(max_length=100, default="100")
    image_300x300       = ImageSpecField(
                            source="image",
                            processors=[ResizeToFill(300, 300)],
                            format="WebP",
                            options={"quality": 80},
                        )
    image_50x50         = ImageSpecField(
                            source="image",
                            processors=[ResizeToFill(50, 50)],
                            format="WebP",
                            options={"quality": 80},
                        )
    cover_image_1920x476 = ImageSpecField(
                            source="cover_image",
                            processors=[ResizeToFill(1920, 476)],
                            format="WebP",
                            options={"quality": 80},
                        )
    date                = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    panels = [
        FieldPanel("user"),
        FieldPanel("title"),
        FieldPanel("image"),
        FieldPanel("cover_image"),
        FieldPanel("description"),
        FieldPanel("address"),
        FieldPanel("contact"),
        FieldPanel("chat_resp_time"),
        FieldPanel("shipping_on_time"),
        FieldPanel("authentic_rating"),
        FieldPanel("days_return"),
    ]
    
    class Meta:
        verbose_name_plural = "Vendors"
    
        
    def delete(self):
        self.deteled=True
        self.save()
        
    def __str__(self):
        return self.title
    
    # def get_url(self):
    #     return reverse("core:vendor-detail", kwargs={"slug": self.slug})

# model: Product
class Product(ClusterableModel):
    user                = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    vendor              = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True, related_name="product")
    slug                = AutoSlugField(populate_from='title', blank=True, null=True)
    title               = models.CharField(max_length=100, default="The largest nuts in the world")
    category            = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name="product")
    tag                 = TaggableManager(blank=True)
    description         = models.TextField(max_length=255, null=True, blank=True, default="The so-called Largest nuts, the key is how the Largest nuts needs to be written. So, So, With these questions, let's examine the Largest nuts.")
    description_long    = models.TextField(max_length=1069, null=True, blank=True, default="The so-called Largest nuts, the key is how the Largest nuts needs to be written. So, So, With these questions, let's examine the Largest nuts.")
    price               = models.DecimalField(max_digits=15, decimal_places=2, default="69000.00")
    old_price           = models.DecimalField(max_digits=15, decimal_places=2, default="69069.00")
    product_status      = models.CharField(choices=STATUS, max_length=100, blank=True, null=True, default="IN_REVIEW")
    status              = models.BooleanField(default=True)
    stock               = models.PositiveIntegerField(default=100)
    in_stock            = models.BooleanField(default=True)
    is_featured         = models.BooleanField(default=True)
    sku                 = models.CharField(max_length=20, blank=True, null=True)
    date_created        = models.DateTimeField(auto_now_add=True)
    date_updated        = models.DateTimeField(null=True, blank=True)
    is_deleted          = models.BooleanField(default=False)
    deleted_date        = models.DateTimeField(null=True, blank=True)
    
    panels = [
        FieldPanel("user"),
        FieldPanel("title"),
        FieldPanel("category"),
        FieldPanel("tag"),
        FieldPanel("description"),
        FieldPanel("description_long"),
        FieldPanel("price"),
        FieldPanel("old_price"),
        FieldPanel("product_status"),
        FieldPanel("status"),
        FieldPanel("stock"),
        FieldPanel("in_stock"),
        FieldPanel("is_featured"),
        FieldPanel("sku"),
        FieldPanel("is_deleted"),
        FieldPanel("deleted_date"),
        InlinePanel("product_gallery", label="Product Gallery"),
        InlinePanel("product_spec", label="Product Spec"),
    ]

    class Meta:
        verbose_name_plural = "Products"

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
        
    def __str__(self):
        return self.title
    
    # def get_url(self):
    #     return reverse("core:product-details", kwargs={"product_slug":self.slug, "vendor_slug":self.vendor.slug})
    
    def get_percentage(self):
        percentage = int(100-((self.price/self.old_price) * 100))
        return percentage
    
# content: product specification
class SpecTable(models.Model):
    name = models.CharField(max_length=50, unique=True)
    order = models.IntegerField(blank=True, null=True, default=0)

    panels = [
        FieldPanel("name"),
        FieldPanel("order"),
    ]

    def __str__(self):
        return self.name

# content: product specification PK
class ProductSpecification(models.Model):
    product = ParentalKey(Product, related_name="product_spec", blank=True, null=True)
    table = models.ForeignKey(SpecTable, on_delete=models.CASCADE)
    value = models.CharField(max_length=200, blank=True, null=True)

# content: product gallery
class ProductGallery(models.Model):
    product         = ParentalKey(
                    Product, related_name="product_gallery", blank=True, null=True
                    )
    image           = models.ImageField(upload_to=product_gallery_image_upload_path, null=True, default=None)
    image_110x110   = ImageSpecField(
                    source="image",
                    processors=[ResizeToFill(110, 110)],
                    format="WebP",
                    options={"quality": 85},
                )
    image_182x182   = ImageSpecField(
                    source="image",
                    processors=[ResizeToFill(182, 182)],
                    format="WebP",
                    options={"quality": 85},
                )
    image_800x800   = ImageSpecField(
                    source="image",
                    processors=[ResizeToFill(800, 800)],
                    format="WebP",
                    options={"quality": 85},
                )

    
                
    def __str__(self):
        return self.product.title
    
    

    class Meta:
        verbose_name = "product gallery"
        verbose_name_plural = "product gallery"