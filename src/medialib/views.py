from django.shortcuts import render_to_response
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, InvalidPage

from medialib.models import Picture

## AJAX views
def media_browser(request, template='medialib/media_browser.html'):
    """
    Our ajax view that will get the media list for the page, and return is as
    JSON

    We also accept 2 GET variables:

    ``count`` is the number of objects per page we want, if 0 return a full list
    without pagination. If not supplied, defaults to 20.
    ``page`` is the actual page that we are on, if 0 or unspecified, defaults to
    page 1

    """
    pictures = Picture.objects.filter(is_visible=True)
        
    context = {}

    if 'count' in request.GET:
        try:
            count = int(request.GET['count'])
        except ValueError:
            count = 20
    else:
        count = 20

    if 'page' in request.GET:
        try:
            page = int(request.GET['page'])
        except ValueError:
            page = 1
    else:
        page = 1

    if count == 0:
        context['pictures'] = pictures
    elif count > 0:
        paginator = Paginator(pictures, int(count))
        try:
            p = paginator.page(page)
        except (EmptyPage, InvalidPage):
            p = paginator.page(paginator.num_pages)
        context['pictures'] = p
    context['count'] = count

    if 'xhr' in request.GET:
        data = serializers.serialize("json", pictures)
        return HttpResponse(data, mimetype="application/json")
    else:
        return render_to_response(template, context)
