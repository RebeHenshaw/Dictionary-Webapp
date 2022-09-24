import justpy as jp

class Home:
    path = "/"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="Hello World!! This is home", classes="text-4xl m-2")
        jp.Div(a=div, text="""
                Latin Text Meow
                """, classes="text-lg")
        return wp



