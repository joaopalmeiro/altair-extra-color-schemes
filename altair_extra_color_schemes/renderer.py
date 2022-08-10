# https://stackoverflow.com/questions/40196059/how-to-include-extend-jinja2-template-string-variable-in-another-variable
# https://jinja.palletsprojects.com/en/3.1.x/templates/#template-objects
# https://stackoverflow.com/a/63103365
# https://github.com/altair-viz/altair/blob/v4.2.0/altair/vegalite/__init__.py
# https://github.com/altair-viz/altair/blob/v4.2.0/altair/utils/plugin_registry.py#L39
# https://github.com/altair-viz/altair/blob/v4.2.0/altair/utils/display.py#L166
# https://github.com/altair-viz/altair/blob/v4.2.0/altair/utils/html.py#L84
# https://github.com/altair-viz/altair/blob/v4.2.0/altair/utils/html.py#L225
# https://github.com/altair-viz/altair/blob/v4.2.0/requirements.txt
# https://altair-viz.github.io/user_guide/display_frontends.html#renderer-api
# https://stackoverflow.com/a/5035382

import os

from altair.utils.display import HTMLRenderer
from altair.utils.html import HTML_TEMPLATE_UNIVERSAL
from altair.vegalite import VEGA_VERSION, VEGAEMBED_VERSION, VEGALITE_VERSION
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader(os.path.dirname(__file__)), auto_reload=False)
env.globals["ALTAIR_TEMPLATE"] = HTML_TEMPLATE_UNIVERSAL

EXTRA_COLOR_SCHEMES_TEMPLATE = env.get_template("template.jinja")

# https://github.com/altair-viz/altair/blob/v4.2.0/altair/vegalite/v4/display.py#L76
extra_color_schemes_renderer = HTMLRenderer(
    mode="vega-lite",
    template=EXTRA_COLOR_SCHEMES_TEMPLATE,
    vega_version=VEGA_VERSION,
    vegaembed_version=VEGAEMBED_VERSION,
    vegalite_version=VEGALITE_VERSION,
)