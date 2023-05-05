import json
import os
import re

from django.utils.text import slugify


def prepare_ocha_icons(ocha_icons_download_path, output_template_path, out_icons_list_json_file):
    icons = []
    for icon_file_name in os.listdir(ocha_icons_download_path):
        name = os.path.splitext(icon_file_name)[0]
        icon_name = slugify(name)

        with open(os.path.join(ocha_icons_download_path, icon_file_name), 'r') as file:
            icon_content = file.read()
            icon_str_with_id = icon_content.replace('xmlns="http://www.w3.org/2000/svg"',
                                                    f'xmlns="http://www.w3.org/2000/svg" id="icon-{icon_name}"')
            # remove all fill colors
            icon_str_without_fill = re.sub(r'fill="#[0-9a-fA-F]{6}"', '', icon_str_with_id)
            # remove all fill styles
            icon_str_without_style_fill = re.sub(r'style="fill: #[0-9a-fA-F]{6};"', '', icon_str_without_fill)

            icon_template_path = os.path.join(output_template_path, f"{icon_name}.svg")

        with open(icon_template_path, "w") as file:
            # Write data to the file
            file.write(icon_str_without_style_fill)

        icons.append(f"{icon_name}.svg")

        print(f"Processed {icon_name}")

    with open(out_icons_list_json_file, "w") as outfile:
        outfile.write(json.dumps(icons, indent=4))
