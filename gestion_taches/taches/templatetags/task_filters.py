from django import template

register = template.Library()

@register.filter
def filter(queryset, arg):
    try:
        field, value = arg.split('=')
        return queryset.filter(**{field: value})
    except:
        return queryset.none() 