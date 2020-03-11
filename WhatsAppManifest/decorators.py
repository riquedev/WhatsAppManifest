class classproperty(property):
    """
    Decorator to call a classmethod as if it were a property
    """

    def __get__(self, cls, owner):
        return classmethod(self.fget).__get__(None, owner)()


class classpathproperty(property):
    """
    Decorator to call a classmethod as if it were a property
    """

    def __get__(self, cls, owner):
        return str(classmethod(self.fget).__get__(None, owner)()).replace("\\", "/")
