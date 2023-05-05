from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page

from wagtailhumanitarianicons.models import CustomIconPage
from wagtailhumanitarianicons.widgets import IconChooserWidget


class HomePage(CustomIconPage, Page):
    icon = models.CharField(max_length=100, null=True, blank=True, help_text="Humanitarian Icon")

    content_panels = Page.content_panels + [
        FieldPanel("icon", widget=IconChooserWidget)
    ]
