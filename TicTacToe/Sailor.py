# This Python file uses the following encoding: utf-8


class base:
    text:str = "Vous ne passerez pas"

    def __init__(self,name):
        if name != None:
            self.text = name

    def saySecret(self):
        print(self.text)
