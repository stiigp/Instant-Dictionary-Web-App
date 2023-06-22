import justpy as jp


class Home:
    path = '/home'

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        layout = jp.QLayout(a=wp,
                            view="hHh lpR fFf")
        header = jp.QHeader(a=layout)
        toolbar = jp.QToolbar(a=header)

        drawer = jp.QDrawer(a=layout,
                            show_if_above=True,
                            v_mode='left',
                            bordered=True)

        scroll_area = jp.QScrollArea(a=drawer,
                                     classes='fit')
        qlist = jp.QList(a=scroll_area)
        a_classes = 'p-2 m-2 text-lg text-blue-400 hover:text-blue-700'
        jp.A(a=qlist,
             text='Home',
             href='/home',
             classes=a_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist,
             text='Dictionary',
             href='/dictionary',
             classes=a_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist,
             text='About',
             href='/about',
             classes=a_classes)
        jp.Br(a=qlist)

        jp.QBtn(a=toolbar,
                dense=True,
                flat=True,
                round=True,
                icon='menu',
                click=cls.move_drawer,
                drawer=drawer)
        jp.QToolbarTitle(a=toolbar,
                         text='Instant Dictionary')

        container = jp.QPageContainer(a=layout)

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
