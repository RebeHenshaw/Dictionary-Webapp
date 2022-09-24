import justpy as jp


class DefaultLayout(jp.QLayout):

    def __init__(self, **kwargs):
        super().__init__(view="hHh lpR fFf", **kwargs)

        header = jp.QHeader(a=self)
        tool = jp.QToolbar(a=header)
        drawer = jp.QDrawer(a=self, show_if_above=True, v_mode="left", bordered=True)

        scroll = jp.QScrollArea(a=drawer, classes="fit")
        list_area = jp.QList(a=scroll)
        a_classes = "p-2 m-2 text-lg text-blue-400 hover:text-blue-700"
        jp.A(a=list_area, text="Home", href="/", classes=a_classes)
        jp.Br(a=list_area)
        jp.A(a=list_area, text="About", href="/about", classes=a_classes)
        jp.Br(a=list_area)
        jp.A(a=list_area, text="Dictionary", href="/dictionary", classes=a_classes)

        jp.QBtn(a=tool, dense=True, flat=True, round=True, icon="menu",
                click=self.move_drawer, drawer=drawer)
        jp.QToolbarTitle(a=tool, text="Instant Dictionary")

    @staticmethod
    def move_drawer(widget, msg):
        if widget.drawer.value:
            widget.drawer.value = False
        else:
            widget.drawer.value = True
