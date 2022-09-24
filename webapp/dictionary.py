import justpy as jp
import definition


class Dictionary:
    path = "/dictionary"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="Instant English Dictionary", classes="text-4xl m-2")
        jp.Div(a=div, text="Get the definition of any English word instantly as you type.", classes="text-lg m-2")

        output_div = jp.Div(a=div, classes="text-lg m-2 p-2 border-2 h-40")
        input_div = jp.Div(a=div, classes="grid grid-cols-2")
        input_box = jp.Input(a=input_div, placeholder="Type your word here...", outputdiv=output_div,
                             classes="m-2 bg-gray-100 border-2 border-gray-200 rounded "
                                     "width-64 focus:bg-white focus:outline-none focus:border-purple-500 py-2 px-4")
        input_box.on('input', cls.get_definition)


        # jp.Button(a=input_div, text="Get Definition", classes="border-2 text-gray-500",
        #           click=cls.get_definition, outputdiv=output_div, inputbox=input_box)

        return wp

    @staticmethod
    def get_definition(widget, msg):
        defined = definition.Definition(widget.value).get()
        output_text = ""
        counter = 1
        for each in defined:
            output_text += f"\n{str(counter)}. {each}"
            counter += 1

        widget.outputdiv.text = output_text
