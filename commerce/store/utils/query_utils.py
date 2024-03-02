from ..models import ProductGallery, Product, Category


# utility: get first and second image (replacing default image method)
def get_first_and_second_images(products):
    for product in products:
        
        image_1 = ProductGallery.objects.filter(product=product).first()
        product.image_1 = image_1

        image_2 = ProductGallery.objects.filter(product=product).all()[1] if len(ProductGallery.objects.filter(product=product).all()) > 1 else None
        product.image_2 = image_2

    return products