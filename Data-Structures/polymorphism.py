#polymorphism
class Bhandari:
    def looks(self):
        print("smart")


class Pandey:
    def looks(self):
        print("chuttad")


def look(object):
    object.looks()


ayush = Bhandari()
vijay = Pandey()

look(ayush)
look(vijay)
