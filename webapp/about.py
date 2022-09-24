import justpy as jp
import layout


class About:
    path = "/about"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)
        div = jp.Div(a=container, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="Hello World!! This is about", classes="text-4xl m-2")
        jp.Div(a=div, text="""
        Latin Text Meow
        """, classes="text-lg")
        return wp




