print(__name__)

class MyCustomError(TypeError):
    pass

raise MyCustomError("OUCH: This is a custom error")