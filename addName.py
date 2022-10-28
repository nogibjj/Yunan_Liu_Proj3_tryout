class AddName:
    def __init__(self, first, last, score):
        self.first = first
        self.last = last
        self.score = score

    @property
    def __repr__(self):
        return "AddName('{}', '{}', '{}')".format(self.first, self.last, self.score)
