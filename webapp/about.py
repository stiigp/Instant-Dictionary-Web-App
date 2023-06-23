import justpy as jp
from webapp.layout import DefaultLayout
from webapp.page import Page


class About(Page):
    path = '/about'

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)

        lay = DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container,
                     classes='bg-gray-200'
                             ' h-screen')

        jp.Div(a=div,
               text='This is the about page!',
               classes='text-4xl'
                       ' m-2')

        jp.Div(a=div,
               text='Ih caralho ele é foda! v2',
               classes='text-lg')

        return wp
