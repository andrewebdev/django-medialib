from django import template
from django.conf import settings

register = template.Library()

@register.inclusion_tag('medialib/cke_mediabrowser_head.html')
def cke_mediabrowser_head(fields='id_content'):
    """
    Renders the template which includes the HEAD section for the CKEditor media
    browser.

    ``fields`` is the label of the field that will use the media browser.

    Multiple field id's can be passed to the tag by seperating them with spaces
    for example:
    {% cke_mediabrowser_head 'id_content id_other_content' %}

    """
    MEDIA_URL = getattr(settings, 'MEDIA_URL', '/media/')
    AJAX_LOADER_LOCATION = getattr(settings, 'AJAX_LOADER_LOCATION') 
    CKEDITOR_SCRIPT_LOCATION = getattr(settings, 'CKEDITOR_SCRIPT_LOCATION')
    field_ids = fields.split(' ')
    return locals()
