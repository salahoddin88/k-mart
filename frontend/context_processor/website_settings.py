from cms.models import WebsiteSetting
from cart.models import Cart


def website_setting(request):
    """ Website setting, Display dynamic LOGO, TITLE and address details on frontend """
    website_setting = WebsiteSetting.objects.all().last()
    return { 'global_website_setting' : website_setting }


def cart_count(request):
    """ Display cart count on website header """
    quantity = 0
    if request.user.is_authenticated:
        """ NOTE: Optimize this query """
        carts = Cart.objects.filter(user=request.user)
        for cart in carts:
            quantity = quantity + cart.quantity
    return {'global_cart_quantity' : quantity}