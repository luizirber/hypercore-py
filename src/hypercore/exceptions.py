class Error(Exception):
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            if getattr(self, key, object()) is not None:  # pragma: no cover
                raise TypeError("Invalid argument: {}".format(key))
            setattr(self, key, value)

        super(Error, self).__init__(*args)
