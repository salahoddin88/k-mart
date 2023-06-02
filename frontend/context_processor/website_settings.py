from cms.models import WebsiteSetting


def website_setting(request):
    """ Website setting, Display dynamic LOGO, TITLE and address details on frontend """
    website_setting = WebsiteSetting.objects.all().last()
    return { 'global_website_setting' : website_setting }