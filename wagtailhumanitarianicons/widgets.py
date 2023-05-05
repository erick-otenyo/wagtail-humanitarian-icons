from django.forms.widgets import Input


class IconChooserWidget(Input):
    input_type = "hidden"
    template_name = "wagtailhumanitarianicons/widgets/icon_chooser.html"
