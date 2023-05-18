# Wagtail Humanitarian Icons

This Wagtail package brings [Ocha Humanitarian Icons](https://brand.unocha.org/d/xEPytAUjC3sH/icons) to Wagtail Admin.

`NOTE`: The recent versions of Wagtail supports uploading SVGs directly to the images section of the CMS interface. If
you just need to upload SVG images and use them on you frontend, consider using that. This package aims to provide a way
to select and use predefined humanitarian icons from OCHA.

# Installation

```
pip install wagtail-humanitarian-icons
```

Add `wagtailhumanitarianicons` to your installed apps

```
 INSTALLED_APPS = [
        ...
        "wagtailhumanitarianicons",
        ...
        ]
```

# Usage

This package uses the Wagtail `register_icons` hook to register all the Ocha Humanitarian svg icons. For more details on
how this works, please look at the [Wagtail Docs](https://docs.wagtail.org/en/latest/advanced_topics/icons.html) and
the `wagtail_hooks.py` file of this package

You can find a list of all the icons in the file `wagtailhumanitarianicons/icons.json`. You can refer any icon by the
name, without the `.svg` extension.

The best way to visually choose an icon is to use the package `wagtail-icon-chooser` as below:

- First install the `wagtail-icon-chooser` package

```shell
pip install wagtal-icon-chooser
```

- Add to `wagtailiconchooser` to your installed apps

```
   INSTALLED_APPS = [
          ...
          "wagtailhumanitarianicons",
          "wagtailiconchooser",
          ...
          ]
```

Then you can use the widgets provided by `wagtal-icon-chooser`. Refer
the [package docs](https://github.com/wmo-raf/wagtail-icon-chooser) for specific details on how to use the widgets, and
how to show selected icons on your frontend templates.

Have a look on the `sandbox/home/models.py` for a complete example, and `sandbox/home/templates` for an example on
rendering on the frontend.

The code used to prepare the OCHA icons can be found at `wagtailhumanitarianicons/utils.py`