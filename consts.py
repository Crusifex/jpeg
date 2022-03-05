class CSpaceOBJ:
    def __init__(self, colorspace):
        self.colorspace = colorspace

class sRGB(CSpaceOBJ):
    def __init__(self):
        super().__init__("sRGB")

class CIE(CSpaceOBJ):
    def __init__(self):
        super().__init__("CIE")

class Adobe(CSpaceOBJ):
    def __init__(self):
        super().__init__("Adobe")