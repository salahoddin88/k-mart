from django.shortcuts import render
from cms.models import Slider
from product.models import ProductCategory, Product, ProductTag
from cms.models import WebsiteSetting


def home_page(request):
    """ Home page of k-mart E-com  """
    navigation_categories = ProductCategory.objects.filter(status=True)
    website_setting = WebsiteSetting.objects.all().last()
    sliders = Slider.objects.filter(status=True)
    product_categories = ProductCategory.objects.filter(status=True, show_on_homepage=True)
    fashion_products_one = Product.objects.filter(status=True)[0:2]
    fashion_products_two = Product.objects.filter(status=True)[2:4]
    product_tags = ProductTag.objects.filter(status=True)[0:2]
    context = {
        'navigation_categories' : navigation_categories,
        'website_setting' : website_setting,
        'sliders' : sliders,
        'product_categories' : product_categories,
        'fashion_products_one' : fashion_products_one,
        'fashion_products_two' : fashion_products_two,
        'product_tags' : product_tags
    }
    return render(request, 'home.html', context)


def product_listing(request, category_id):
    navigation_categories = ProductCategory.objects.filter(status=True)
    product_category = ProductCategory.objects.get(id=category_id)
    print(product_category)
    return render(request, 'test.html', {'navigation_categories': navigation_categories})


