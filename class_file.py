class File():
    def __init__(self, inputc, file):
        self.__file = file
        self.__inputc = inputc

    @property
    def inputc(self):
        return self.__input

    @property
    def file(self):
        return self.__file

    @inputc.setter
    def inputc(self, inputc):
        if isinstance(inputc, str):
            self.__inputc = inputc
        elif isinstance(inputc, int) or isinstance(inputc, float):
            self.__inputc = str(inputc)
        elif isinstance(inputc, list) or isinstance(inputc,tuple):
            if len(inputc) == 1:
                self.__inputc = str(inputc[0])
            else:
                raise ValueError("Only 1 item suported on list or tuple")
        else:
            raise TypeError("Incorrect type for input")
    @file.setter
    def file(self, file):
        if isinstance(file, str):
            self.__file = file
        else:
            raise TypeError("Incorrect type for file")

    def getFileContent(self):
        content=""
        with open(self.__file, "r") as f:
            for i in self.__file.readlines():
                content+=str(i)
            #idk if I need to close the file
        return content

    def writeContent(self):
        # saving self.__input in self.__file
        pass

    def __str__(self):
        return self.getFileContent()