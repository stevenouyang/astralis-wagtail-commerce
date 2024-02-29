import os
from django.utils.text import slugify

def category_image_upload_path(instance, filename, field_name=None):
    TITLE = "title"
    TYPE = "category"

    _, file_extension = os.path.splitext(filename)
    title = instance.title
    title = "-".join(e for e in title.split())
    upload_path = os.path.join("media", TYPE, title)
    if not os.path.exists(upload_path):
        image_number = 1
    else:
        existing_numbers = [
            int(filename.split("-")[-1].rsplit("_", 1)[0].split(".")[0])
            for filename in os.listdir(upload_path)
            if filename.startswith(f"{title}-image-") and filename.endswith(".jpg")
        ]
        image_number = max(existing_numbers) + 1 if existing_numbers else 1
    final_filename = f"{title}-image-{str(image_number).zfill(2)}{file_extension}"

    print(final_filename)
    return os.path.join(TYPE, title, final_filename)

def product_gallery_image_upload_path(instance, filename):
    TYPE = "product_gallery"
    
    product_name = slugify(instance.product.title)
    user_name = slugify(instance.product.user.username)
    upload_path = os.path.join("media", TYPE,user_name, product_name)
    
    if not os.path.exists(upload_path):
        image_number = 1
    else:
        existing_numbers = [
            int(file.split("-")[-1].rsplit("_", 1)[0].split(".")[0])
            for file in os.listdir(upload_path)
            if file.startswith(f"{product_name}-image-") and file.endswith(".jpg")
        ]
        image_number = max(existing_numbers) + 1 if existing_numbers else 1

    final_filename = f"{product_name}-image-{str(image_number).zfill(2)}{os.path.splitext(filename)[1]}"

    print(final_filename)
    return os.path.join(TYPE, user_name, product_name, final_filename)

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)