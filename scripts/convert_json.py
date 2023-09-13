import base64
import json
import re
from prettytable import PrettyTable
from prettytable import MARKDOWN

# Read JSON file
with open("icons.json", "r") as json_file:
    data = json.load(json_file)

# Setup the Markdown table
x = PrettyTable()
x.set_style(MARKDOWN)
x.align = "l"
x.field_names = ["Icon", "Name", "Icon Source", "Icon Guidelines"]

# Initialize an empty list
json_obj_list = []

# For each item inside "icons"
for item in data["icons"]:
    name = item['name']
    path = item['path']
    source = item['source']
    guidelines = item['guidelines']

    #
    # Markdown
    #

    # Markdown-formatted links
    f_img = f"![]({path})"
    # If source begin with "https", then make a link, otherwise use a string
    if re.match(r'^https', source):
        f_source = f"[Source]({source})"
    else:
        f_source = f"{source}"
    # If guidelines are missing, do not add a Markdown link
    if not guidelines:
        f_guidelines = ""
    if guidelines:
        f_guidelines = f"[Guidelines]({guidelines})"

    # Add the row
    x.add_row([f_img, name, f_source, f_guidelines])

    #
    # XML
    #

    # Open each image
    with open(path, "rb") as image_file:
        # The data is binary, so need to get it to a string
        data = base64.b64encode(image_file.read()).decode('ascii')

        # Build a string
        data_string = "data:image/svg+xml;base64,"+data

        # Create the JSON object for each icon
        json_obj_list .append({"data": data_string,
                               "w": 48,
                               "h": 48,
                               "title": name,
                               "aspect": "fixed"})
        image_file.close()

# The actual JSON string, with all whitespace removed
json_dump = json.dumps(json_obj_list, separators=(',', ':'))

# Print Markdown table
with open("ICONS.md", "w") as md_output:
    print("# Icons\n", file=md_output)
    print(x, file=md_output)
    md_output.close()

# Print XML (Diagram.net's XML is actually just JSON wrapped in a single XML tag)
with open("homelab-svg-assets.xml", "w") as xml_output:
    print("<mxlibrary>"+json_dump+"</mxlibrary>", file=xml_output)
    xml_output.close()
