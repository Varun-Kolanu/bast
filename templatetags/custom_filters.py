from django import template
from datetime import datetime, timedelta
from django.utils import timezone

register = template.Library()

@register.filter
def custom_date_display(value):
    now = datetime.now()
    if value.date() == now.date():
        return "Today"
    elif value.date() == now.date() - timedelta(days=1):
        return "Yesterday"
    else:
        return value.strftime("%d %b %Y")

@register.filter
def compare_date(date):
    if not date:
        return False
    return date < timezone.now()
