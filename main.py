from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label


class Calculator(App):
    def build(self):
        layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        self.num1 = TextInput(hint_text="Enter 1st Number", multiline=False)
        self.num2 = TextInput(hint_text="Enter 2nd Number", multiline=False)

        self.result = Label(text="Answer will appear here")

        add = Button(text="Add")
        sub = Button(text="Subtract")
        mul = Button(text="Multiply")
        div = Button(text="Divide")

        add.bind(on_press=self.add)
        sub.bind(on_press=self.sub)
        mul.bind(on_press=self.mul)
        div.bind(on_press=self.div)

        layout.add_widget(self.num1)
        layout.add_widget(self.num2)
        layout.add_widget(add)
        layout.add_widget(sub)
        layout.add_widget(mul)
        layout.add_widget(div)
        layout.add_widget(self.result)

        return layout

    def get_numbers(self):
        try:
            a = int(self.num1.text)
            b = int(self.num2.text)
            return a, b
        except:
            self.result.text = "Invalid Input"
            return None

    def add(self, instance):
        nums = self.get_numbers()
        if nums:
            a, b = nums
            self.result.text = f"Answer: {a+b}"

    def sub(self, instance):
        nums = self.get_numbers()
        if nums:
            a, b = nums
            self.result.text = f"Answer: {a-b}"

    def mul(self, instance):
        nums = self.get_numbers()
        if nums:
            a, b = nums
            self.result.text = f"Answer: {a*b}"

    def div(self, instance):
        nums = self.get_numbers()
        if nums:
            a, b = nums
            if b == 0:
                self.result.text = "Math Error"
            else:
                self.result.text = f"Answer: {a/b}"


Calculator().run()