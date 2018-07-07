import sys
import json
import telegram.model


class SystemProperties:
    def __init__(self):
        for param in sys.argv:
            if 'id=' in param:
                bid = param[len('id='): len(param)]
                self.id = bid



class UpdateDecoder(json.JSONDecoder):
    def default(self, obj):
        if isinstance(obj, telegram.model.Update):
            print()


