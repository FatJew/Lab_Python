

class CustomException(Exception):
    def __init__(self):
        super().__init__("Custom exception class")