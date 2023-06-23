import justpy as jp
import inspect
from webapp.about import About
from webapp.home import Home
from webapp.dictionary import Dictionary
from webapp.page import Page


imports = list(globals().values())

for value in imports:
    if inspect.isclass(value):
        if (value, Page) and hasattr(value, 'path'):
            jp.Route(value.path, value.serve)

jp.Route(Home.path, Home.serve)
jp.Route(About.path, About.serve)
jp.Route(Dictionary.path, Dictionary.serve)

jp.justpy()
