from value import Value
from value_abstract import ValueAbstract


class Main:
    def __init__(self):
        self.list_open: [] = list()
        self.list_close: [] = list()

        self.go_through: [] = list()

        self.go_through.append({"primary": Value(name="A 1", value_end=6, value_back=0, value_weight=6),
                                "neighbors": Value(name="A 2", value_end=5, value_back=1, value_weight=6)})
        self.go_through.append({"primary": Value(name="A 1", value_end=6, value_back=0, value_weight=6),
                                "neighbors": Value(name="B 1", value_end=6, value_back=1, value_weight=7)})

        self.go_through.append({"primary": Value(name="A 2", value_end=5, value_back=0, value_weight=5),
                                "neighbors": Value(name="A 1", value_end=7, value_back=1, value_weight=8)})
        self.go_through.append({"primary": Value(name="A 2", value_end=5, value_back=0, value_weight=5),
                                "neighbors": Value(name="A 3", value_end=4, value_back=1, value_weight=5)})
        self.go_through.append({"primary": Value(name="A 2", value_end=5, value_back=0, value_weight=5),
                                "neighbors": Value(name="B 2", value_end=4, value_back=1, value_weight=4)})

        self.go_through.append({"primary": Value(name="A 3", value_end=4, value_back=0, value_weight=4),
                                "neighbors": Value(name="A 2", value_end=5, value_back=1, value_weight=6)})
        self.go_through.append({"primary": Value(name="A 3", value_end=4, value_back=0, value_weight=4),
                                "neighbors": Value(name="A 4", value_end=5, value_back=1, value_weight=6)})
        self.go_through.append({"primary": Value(name="A 3", value_end=4, value_back=0, value_weight=4),
                                "neighbors": Value(name="B 3", value_end=4, value_back=1, value_weight=5)})

        self.go_through.append({"primary": Value(name="A 4", value_end=5, value_back=0, value_weight=5),
                                "neighbors": Value(name="A 3", value_end=4, value_back=1, value_weight=5)})
        self.go_through.append({"primary": Value(name="A 4", value_end=5, value_back=0, value_weight=5),
                                "neighbors": Value(name="A 5", value_end=6, value_back=1, value_weight=7)})
        self.go_through.append({"primary": Value(name="A 4", value_end=5, value_back=0, value_weight=5),
                                "neighbors": Value(name="B 4", value_end=5, value_back=1, value_weight=6)})

        self.go_through.append({"primary": Value(name="A 5", value_end=6, value_back=0, value_weight=6),
                                "neighbors": Value(name="A 4", value_end=5, value_back=1, value_weight=6)})
        self.go_through.append({"primary": Value(name="A 5", value_end=6, value_back=0, value_weight=6),
                                "neighbors": Value(name="B 5", value_end=5, value_back=1, value_weight=6)})

        for row in self.go_through:
            print(row['neighbors'].__str__())


if __name__ == "__main__":
    Main()
