from tokenize import String


def build_hello(name: str) -> str:
    return "Hello, " + name.__str__() + "!"
