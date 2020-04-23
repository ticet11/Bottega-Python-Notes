# Dunder methods should not be overridden.
class Invoice:
    def __init__(self, client, total):
        self.client = client
        self.total = total
    # You are basically telling python what the pretty str of this object is.
    def __str__(self):
        return f'Invoice from {self.client} for ${self.total}:'
    # Gives you a more raw output than __str__
    def __repr__(self):
        return f'Invoice{{{self.client}:{self.total}}}'


inv = Invoice('Google', 500)
print(str(inv))
print(repr(inv))

