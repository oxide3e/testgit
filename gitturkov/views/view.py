import os
from jinja2 import Environment, FileSystemLoader

class View:
    def __init__(self, layout):
        self.env = Environment
        (loader=FileSystemLoader('views'),
         autoescape=(["html", "xml"]))

    def render_html(self, view_name, vars):
        file_vars.update(vars)
        template = self.env.get_template
        (layout_file)
        return template.render(fileVars)