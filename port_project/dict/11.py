from jinja2 import Template


class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def getname(self):
        return self.name

    def getage(self):
        return self.age

pers= Person("Ainura", 37)

per= {'name': 'Ainura', 'age': '35'}



tm = Template("Hello, my name is {{ p['name'] }}, and I am {{ p['age'] }}")
msg= tm.render(p=per)


print(msg)

