from os import path


class dataBlock:

    def __init__(self, filePath, autoUpdate=False):
        self.storeUpdate = None
        self.tempList = None
        self.update = autoUpdate
        self.data = {}
        if not path.exists(filePath):
            print('file does not exist')
            self.dataFilePath = None
        else:
            self.dataFilePath = filePath

    def __str__(self):
        out = '\n'*2 + '-- DATABASE --' + '\n'*2
        counter = -1
        for x in self.data:
            counter += 1
            if counter != len(self.data) - 1:
                out += str(x) + ' : ' + str(type(self.data[x]))[8:-2] + '\n' + ' '*5 + str(self.data[x]) + '\n'
            else:
                out += str(x) + ' : ' + str(type(self.data[x]))[8:-2] + '\n' + ' '*5 + str(self.data[x])
        return out + '\n'

    def __getitem__(self, item):
        return self.data[str(item)]

    def AddValue(self, name, value):
        self.data[name] = value
        if self.update:
            self.Serialize()

    def Serialize(self):
        return None

    def Deserialize(self):  # ↑ ↓
        self.data = {}
        if self.update:
            self.storeUpdate = True
            self.update = False
        # Decrypt
        # Interpreter ↓↓
        file = open(self.dataFilePath, 'r', encoding='UTF-8')
        b = len(file.readlines())
        file.close()
        readString = False
        readInt = False
        readFloat = False
        readBool = False
        file = open(self.dataFilePath, 'r', encoding='UTF-8')
        for x in range(b):
            tString = file.readline()
            if tString[-1] == '\n':
                tString = tString[0:-1]
            if (not readString) and (not readInt) and (not readFloat) and (not readBool):
                if tString == '|↑|str|↑|':
                    readString = True
                    self.tempList = []
                if tString == '|↑|int|↑|':
                    readInt = True
                    self.tempList = []
                if tString == '|↑|float|↑|':
                    readFloat = True
                    self.tempList = []
                if tString == '|↑|bool|↑|':
                    readBool = True
                    self.tempList = []
            else:
                if readString:
                    if tString == '|↓|str|↓|':
                        self.AddValue(self.tempList[0], self.tempList[1])
                        readString = False
                    else:
                        self.tempList.append(tString)
                if readInt:
                    if tString == '|↓|int|↓|':
                        self.AddValue(self.tempList[0], int(self.tempList[1]))
                        readInt = False
                    else:
                        self.tempList.append(tString)
                if readFloat:
                    if tString == '|↓|float|↓|':
                        self.AddValue(self.tempList[0], float(self.tempList[1]))
                        readFloat = False
                    else:
                        self.tempList.append(tString)
                if readBool:
                    if tString == '|↓|bool|↓|':
                        self.AddValue(self.tempList[0], bool(self.tempList[1]))
                        readBool = False
                    else:
                        self.tempList.append(tString)
        file.close()
        if self.storeUpdate:
            self.storeUpdate = None
            self.update = True


a = dataBlock('E:\\testing.txt', True)
a.Deserialize()
print(a)
