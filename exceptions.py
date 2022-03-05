class InvalidFileError(Exception):
    def __init__(self, message="The file is not a .jpg file."):
        self.message = message
        super().__init__(self.message)

class NonExistantFile(Exception):
    def __init__(self, message="The file does not exist."):
        self.message = message
        super().__init__(self.message)

class NotAFile(Exception):
    def __init__(self, message="The path is not a file."):
        self.message = message
        super().__init__(self.message)

class InvalidColorSpace(Exception):
    def __init__(self, message="The Colorspace is not a instance of CSpaceOBJ."):
        self.message = message
        super().__init__(self.message)

class MetadataExists(Exception):
    def __init__(self, message="The .jpg file is already formatted as a mdj."):
        self.message = message
        super().__init__(self.message)