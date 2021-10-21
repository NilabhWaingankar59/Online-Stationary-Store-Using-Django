from django import template
from accounts.models import products,cartproduct
register = template.Library()

@register.filter(name="samecat")
def samecat(c, p):
    if c.catid==p.catid_id:
        return True
    return False


@register.filter(name="counter")
def counter(c, counter):
    print(counter)
    if counter<=4:
        return True
    return False


@register.filter(name="display1")
def display1(c, product):
    print(c.pid_id)
    p=products.objects.get(id=c.pid_id)
    return p.name

@register.filter(name="display2")
def display2(c, product):
    print(c.pid_id)
    p=products.objects.get(id=c.pid_id)
    return p.price

@register.filter(name="display3")
def display3(c, product):
    p=products.objects.get(id=c.pid_id)
    return p.price*c.n

n=1
@register.filter(name="limit")
def limit(c, product):
    global n
    if n<=4 :
        n = n+1
        return True
    else:
        return False

@register.filter(name="nilabh")
def nilabh(c, product):
    global n
    n=1
    return False


@register.filter(name="adx")
def adx(c, cust):
    s=cust.address+","+cust.district+","+cust.pin
    return s
