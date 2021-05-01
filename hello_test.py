def hello(name):
    return "Hello " + name + "!"

def test_hello():
    assert hello('world') == "Hello world!"
