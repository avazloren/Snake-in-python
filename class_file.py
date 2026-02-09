import json

class File():
    def __init__(self, file):
        self.__file = file

    @property
    def file(self):
        return self.__file

    def __validateInputc(self, inputc): #inputc is suposed to be like [key, value]
        if isinstance(inputc, list) or isinstance(inputc,tuple):
            if len(inputc) == 2:
                self.__inputc = inputc
            else:
                raise ValueError("Only 2 item suported on list or tuple")
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
            content = str(json.load(f))

        return content

    def getHeight(self):
        with open(self.__file, "r") as f:
            data=json.load(f)
        return data["height"]

    def getWidth(self):
        with open(self.__file, "r") as f:
            data=json.load(f)
        return data["width"]


    def writeContent(self, inputc): #this will erase all the content and create neo one
        '''
        saving self.__input in self.__file, json file looks like this:
        {
        "width": 800,
        "height": 600
        }

        '''
        self.__validateInputc(inputc) # this will create self.__inputc

        try:
            with open(self.__file, "w") as f:
                json.dump({self.__inputc[0]: self.__inputc[1]}, f)
            return True
        except FileNotFoundError as e:
            return f"File not found, error output: {e}"
        except FileExistsError as e:
            return f"An error related to the file occurred, error output: {e}"
        except Exception as e:
            return f"An unexpected error occurred, error output: {e}"

    def appendContent(self, inputc):
        '''
        First validate inputc and read the content of the json file
        2nd append the new input (inputc) into the file content
        Finally rewrite from zero all the content
        '''
        self.__validateInputc(inputc)

        try:
            try:
                with open(self.__file, "r") as f:
                    content = json.load(f)
            except FileNotFoundError:
                content = {}

            if isinstance(content, list):
                content.append(inputc)

            elif isinstance(content, dict):
                key, value = inputc
                content[key] = value

            else:
                raise TypeError("Unsupported JSON content type")

            with open(self.__file, "w") as f:
                json.dump(content, f, indent=2) #ident=2 adds two spaces

            return True

        except Exception as e:
            return f"An unexpected error occurred, error output: {e}"

    def __str__(self): #__str__ function return all the content of self.__file
        return f"File path: {self.__file}, content: \n {self.getFileContent()}"

if __name__ == "__main__":
    file = File("./config.json")
    file.writeContent(["width", 800])
    print(file.appendContent(["height", 600]))
    print(file)
    print(file.getWidth())
    print(file.getHeight())
