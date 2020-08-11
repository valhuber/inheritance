import base  # works for run_local (only), 'problem' reported
# from src.inheritance_pkg import base  # PyCharm ok, not vsc (good grief)


class Sub(base.Super):
    def __init__(self):
        super(Sub, self).__init__()
        print("Sub here")
