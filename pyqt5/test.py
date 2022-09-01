class Entry:
    def __init__(self):
        pass

class Timer:

    Entry = Entry
    def t (self):
        print (type(self.Entry))
        print('ok')

v = Timer()
v.t()