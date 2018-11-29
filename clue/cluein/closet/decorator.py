
def welcomeOut(func):
    def welcomeInside():
        return func() + "clueIn"
    return welcomeInside

@welcomeOut
def welcome():
    return "Welcome to "

print(welcome())