import sys


class SystemProperties:

    def __init__(self):
        for param in sys.argv:
            if 'id=' in param:
                bid = param[len('id='): len(param)]
                self.id = bid
