import json
from prettytable import PrettyTable
from prettytable import MARKDOWN

# Read JSON
with open("icons.json", "r") as json_file:
  data = json.load(json_file)

# Setup the table
x = PrettyTable()
x.set_style(MARKDOWN)
x.align = "l"
x.field_names = ["Icon","Name", "Icon Source", "Icon Guidelines"]

# For each item inside "icons"
for item in data["icons"]:
  name = item['name']
  path = item['path']
  source = item['source']
  guidelines = item['guidelines']

  # Markdown-formatted links
  f_img=f"![]({path})"
  f_source=f"[Source]({source})"
  # If guidelines are missing, do not add a link
  if not guidelines:
   f_guidelines=f""
  if guidelines:
    f_guidelines=f"[Guidelines]({guidelines})"
  
  # Add the row
  x.add_row([f_img, name, f_source, f_guidelines])

# Print to a file
with open("ICONS.md", "w") as output:
    print("# Icons\n", file=output)
    print(x, file=output)
    output.close()