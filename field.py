
class Field:  # Базовий клас для полів запису.
    def __init__(self, value):
        self._value = value

    def __str__(self):
        return str(self._value)
