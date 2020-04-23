class Invoice:

    def __init__(self, client, total):
        self._client = client
        self._total = total

    def formatter(self):
        return f'{self._client} owes: ${self._total}'

    # Hints at the fact that you might want to access this information at some point
    # Items not included are most likely things you shouldn't need to access
    @property
    def client(self):
        return self._client

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, total):
        self._total = total


google = Invoice('Google', 100)
google.total = 300
print(google.formatter())
