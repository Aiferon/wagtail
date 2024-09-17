from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

class HomePage(Page):
    
    #Поля в базе данных   
    subtitle = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Подзаголовок"
    )

    #Поля для ввода данных в интерфейсе

    content_panels = Page.content_panels + [
        FieldPanel('subtitle')
    ]