import justpy as jp
from definition import Definition
from webapp.layout import DefaultLayout
from webapp.page import Page


class Dictionary(Page):
    path = '/dictionary'

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        lay = DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container,
                     classes='bg-gray-200'
                             ' h-screen')

        jp.Div(a=div,
               text='Instant english dictionary!',
               classes='text-4xl'
                       ' m-2')

        jp.Div(a=div,
               text='Get the definition of any English word instantly as you type.',
               classes='text-lg')

        input_div = jp.Div(a=div,
                           classes='grid grid-cols-2')

        output_div = jp.Div(a=div,
                            classes=' border-2'
                                    ' m-2'
                                    ' p-2'
                                    ' text-lg'
                                    ' h-40')

        input_box = jp.Input(a=input_div,
                             placeholder='Type in a word here',
                             classes='m-2'
                                     ' bg-gray-100'
                                     ' border-2'
                                     ' border-gray-200'
                                     ' rounded'
                                     ' w-64'
                                     ' focus:outline-none'
                                     ' focus:border-purple-500'
                                     ' focus:bg-white'
                                     ' py-2'
                                     ' px-4',
                             outputdiv=output_div)

        input_box.on('input', cls.get_definition)

        return wp

    @staticmethod
    def get_definition(widget, msg):
        def_object = Definition(widget.value)
        definition = def_object.get()
        widget.outputdiv.text = ', '.join(definition)
