from django.db import models

from photologue.models import ImageModel

class MediaManager(models.Manager):
    def get_query_set(self):
        queryset = super(MediaManager, self).get_query_set().filter(is_visible=True)
        return queryset

class Picture(ImageModel):
    """
    This is a basic picture, based on the photologue ImageModel.
    The following sizes needs to be created in photo_sizes:

        ``medialib_small``
        ``medialib_medium``
        ``medialib_large``

    To be sure that you can see the thumbnails of images in the admin,
    remember to add a photo_size for that:

        ``admin_thumbnail``

    """
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True,
                help_text="A unique, url-friendly slug based on the title")
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    is_visible = models.BooleanField(default=True)

    objects = models.Manager()
    media_objects = MediaManager()

    def __unicode__(self):
        return "%s" % self.title

    def small_picture(self):
        return '<a class="medialib_picture" id="picture_%s_small" href="%s">Small</a>' % (
            self.id,
            self.get_medialib_small_url()
        )
    small_picture.allow_tags = True

    def medium_picture(self):
        return '<a class="medialib_picture" id="picture_%s_medium" href="%s">Medium</a>' % (
            self.id,
            self.get_medialib_medium_url()
        )
    medium_picture.allow_tags = True

    def large_picture(self):
        return '<a class="medialib_picture" id="picture_%s_large" href="%s">Large</a>' % (
            self.id,
            self.get_medialib_large_url()
        )
    large_picture.allow_tags = True
