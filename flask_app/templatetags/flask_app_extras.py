from django import template

register = template.Library()

@register.filter
def split_and_strip(value, sep=','):
    """Splits a string by the given separator and strips each element in the resulting list."""
    return [item.strip() for item in value.split(sep) if item.strip()]
