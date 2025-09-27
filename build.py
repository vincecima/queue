from jinja2 import Environment, FileSystemLoader, select_autoescape

jinja = Environment(loader=FileSystemLoader(["."]), autoescape=select_autoescape())
template = jinja.get_template("input/site.j2")
print(template.render())
