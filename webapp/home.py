import justpy as jp
from webapp.layout import DefaultLayout
from webapp.page import Page


class Home(Page):
    path = '/'

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        lay = DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container,
                     classes='bg-gray-200'
                             ' h-screen')

        jp.Div(a=div,
               text='This is the home page!',
               classes='text-4xl'
                       ' m-2')

        jp.Div(a=div,
               text='Ih caralho, ele é foda!',
               classes='text-lg')

        return wp

    @staticmethod
    def move_drawer(widget, msg):
        if not widget.drawer.value:
            widget.drawer.value = True
        else:
            widget.drawer.value = False
