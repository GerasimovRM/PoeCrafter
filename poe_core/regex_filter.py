class RegexFilter(str):
    def __init__(self, *args):
        super().__init__(*args)
        if len(self) > 50:
            raise AttributeError("Length of regex filter can not be more than 50")
        elif len(self) == 0:
            raise AttributeError("Length of regex filter can not be equal 0")
