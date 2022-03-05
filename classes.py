from logging import exception
from . import exceptions
from . import consts
import json
import os

class mdj:
    def __init__(self, path: str):
        if os.path.isfile(path):
            if os.path.exists(path):
                if path.split(".")[1] == "jpg":
                    self.path = path
                else:
                    raise exceptions.InvalidFileError
            else:
                raise exceptions.NonExistantFile
        else:
            raise exceptions.NotAFile

        self.timestamp = 0
        self.colorspace = ""
        self.location = ""
        self.device_name = ""
        self.iso = 0
        self.width = 0
        self.length = 0

        e = self._attempt_load(self.path)

        if not e:
            print("WARN: loading failed.")

    def meta(self, timestamp: float, colorspace, location: str, device_name: str, iso: int, width: int, length: int):
        if not isinstance(colorspace, type(consts.CSpaceOBJ)):
            raise exceptions.InvalidColorSpace
        else:
            self.timestamp = timestamp
            self.colorspace = colorspace
            self.location = location
            self.device_name = device_name
            self.iso = iso
            self.width = width
            self.length = length

            with open(self.path, "rb") as f:
                content = f.read()
                f.seek(content.index(bytes.fromhex("FFD9")) + 2)
                data = f.read().decode()
                f.close()

            if data == "":
                data = {"ts": self.timestamp, "cs": self.colorspace, "ln": self.location, "dn": self.device_name, "iso": self.iso, "sw": self.width, "sl": self.length}
                with open(self.path, "ab") as f:
                    f.write(json.dumps(data).encode())
                    f.close()
            else:
                raise exceptions.MetadataExists

    def _attempt_load(self, path):
        with open(path, "rb") as f:
            content = f.read()
            f.seek(content.index(bytes.fromhex("FFD9")) + 2)
            data = f.read().decode()
            f.close()

        if data == "":
            return False
        else:
            try:
                d = json.loads(data)
                if list(d.keys()) == ["ts", "cs", "ln", "dn", "iso", "sw", "sl"]:
                    self.timestamp = d["ts"]
                    self.colorspace = d["cs"]
                    self.location = d["ln"]
                    self.device_name = d["dn"]
                    self.iso = d["iso"]
                    self.width = d["sw"]
                    self.length = d["sl"]
                    return True
                else:
                    return False
            except Exception as e:
                print(e)
                return False