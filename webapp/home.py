import justpy as jp
import layout


class Home:
    path = "/"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)

        container = jp.QPageContainer(a=lay)
        div = jp.Div(a=container, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="Hello World!! This is home", classes="text-4xl m-2 p-4")
        jp.Div(a=div, text="""
                Latin Text Meow
                """, classes="text-lg p-4")
        return wp
