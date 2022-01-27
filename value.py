from value_abstract import ValueAbstract


class Value(ValueAbstract):
    def __init__(self, name: str, value_weight: int, value_back: int, value_end: int):
        super(Value, self).__init__(name=name, value_weight=value_weight, value_back=value_back, value_end=value_end)

    def get_value_weight(self) -> int:
        return super(Value, self).get_value_weight()

    def get_value_back(self) -> int:
        return super(Value, self).get_value_back()

    def get_value_end(self):
        return super(Value, self).get_value_end()

    def get_name(self) -> str:
        return super(Value, self).get_name()

    def __str__(self):
        return super(Value, self).__str__()
