from django import template

register = template.Library()

@register.filter(name="custom_cut")
def custom_cut(value, arg) : 
    return value.replace(arg, 'bjir')