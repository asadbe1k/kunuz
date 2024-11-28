from django import template
from bs4 import BeautifulSoup  

register = template.Library()


@register.filter(name="remove_images") 
def remove_images(value):
    soup = BeautifulSoup(value, "html.parser")
    for img in soup.find_all("img"):
        img.decompose()
    return str(soup)
