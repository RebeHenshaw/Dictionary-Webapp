import justpy as jp

class Home:
    path = "/"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        layout = jp.QLayout(a=wp, view="hHh lpR fFf")
        header = jp.QHeader(a=layout)
        tool = jp.QToolbar(a=header)
        drawer = jp.QDrawer(a=layout, show_if_above=True, v_mode="left", bordered=True)

        scroll = jp.QScrollArea(a=drawer, classes="fit")
        list_area = jp.QList(a=scroll)
        a_classes = "p-2 m-2 text-lg text-blue-400 hover:text-blue-700"
        jp.A(a=list_area, text="Home", href="/", classes=a_classes)
        jp.Br(a=list_area)
        jp.A(a=list_area, text="About", href="/about", classes=a_classes)
        jp.Br(a=list_area)
        jp.A(a=list_area, text="Dictionary", href="/dictionary", classes=a_classes)

        jp.QBtn(a=tool, dense=True, flat=True, round=True, icon="menu",
                click=cls.move_drawer, drawer=drawer)
        jp.QToolbarTitle(a=tool, text="Instant Dictionary")
        container = jp.QPageContainer(a=layout)
        div = jp.Div(a=container, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="Hello World!! This is home", classes="text-4xl m-2 p-4")
        jp.Div(a=div, text="""
                Latin Text Meow
                """, classes="text-lg p-4")
        return wp


    @staticmethod
    def move_drawer(widget, msg):
        if widget.drawer.value:
            widget.drawer.value = False
        else:
            widget.drawer.value = True




