from django import template
from accounts.models import products
register = template.Library()


@register.filter(name="samecat")
def samecat(c, p):
    if c.catid==p.catid_id:
        return True
    return False 
