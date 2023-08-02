from IData import IData

class Text(IData):
    def __init__(self, text: str):
        self.text = text

    def get_data(self) -> str:
        return self.text
