from django.template.defaulttags import register
from config import settings


@register.filter(is_safe=True)
def mediapath(text):
    return f'/media/{text}'

# {settings.MEDIA_URL}
@register.simple_tag
def mediapath(text):
    return f'/media/{text}'


