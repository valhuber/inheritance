import base


class Sub(base.Super):
    def __init__(self):
        super(Sub, self).__init__()
        print("Sub here")
