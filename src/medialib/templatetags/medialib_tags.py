from django import template
from django.conf import settings

register = template.Library()

@register.inclusion_tag('medialib/cke_mediabrowser_head.html')
def cke_mediabrowser_head(field_id='id_content'):
    """
    Renders the template which includes the HEAD section for the CKEditor media
    browser.

    ``field_label`` is the label of the field that will use the media browser.
    ``ajax_loader_location`` is the location for the gif loader. Defaults to the
    MEDIA_URL setting.

    """
    MEDIA_URL = getattr(settings, 'MEDIA_URL', '/media/')
    AJAX_LOADER_LOCATION = getattr(settings, 'AJAX_LOADER_LOCATION') 
    CKEDITOR_SCRIPT_LOCATION = getattr(settings, 'CKEDITOR_SCRIPT_LOCATION')

    return {
        'field_id': field_id,
        'AJAX_LOADER_LOCATION': AJAX_LOADER_LOCATION,
        'CKEDITOR_SCRIPT_LOCATION': CKEDITOR_SCRIPT_LOCATION,
    }
