from os import path


class dataBlock:

    def __init__(self, filePath, autoUpdate=False):
        self.storeUpdate = None
        self.tempList = None
        self.listDepth = None
        self.listStore = None
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

    def addBlank(self, d, lis, firstTime=False):
        if d == 1:
            lis.append([])
            if firstTime:
                return lis
        else:
            d -= 1
            self.addBlank(d, lis[-1])
            if firstTime:
                return lis

    def addToList(self, d, lis, val, firstTime=False):
        if d == 1:
            d -= 1
            lis.append(val)
            if firstTime:
                return lis
        else:
            d -= 1
            self.addToList(d, lis[-1], val)
            if firstTime:
                return lis

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
        readList = False
        listFirstTime = False
        readInListStr = False
        file = open(self.dataFilePath, 'r', encoding='UTF-8')
        for x in range(b):
            tString = file.readline()
            if tString[-1] == '\n':
                tString = tString[0:-1]
            if (not readString) and (not readInt) and (not readFloat) and (not readBool) and (not readList):
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
                if tString == '|↑|list|↑|':
                    readList = True
                    listFirstTime = True
                    self.listDepth = 1
                    self.tempList = None
                    self.listStore = []
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
                if readList:
                    if tString == '|↓|list|↓|':
                        self.AddValue(self.tempList, list(self.listStore))
                        readList = False
                    else:
                        if listFirstTime:
                            self.tempList = str(tString)
                            listFirstTime = False
                        else:
                            if tString == '|↓↓|':
                                self.listDepth -= 1
                            if tString == '|↑↑|':
                                self.listDepth += 1
                                self.listStore = self.addBlank(self.listDepth - 1, self.listStore, True)
                            if not readInListStr:
                                if tString == '|↑|str|↑|':
                                    readInListStr = True
                            else:
                                if readInListStr:
                                    if tString == '|↓|str|↓|':
                                        readInListStr = False
                                    else:
                                        self.listStore = self.addToList(self.listDepth, self.listStore, tString, True)
        file.close()
        if self.storeUpdate:
            self.storeUpdate = None
            self.update = True


a = dataBlock('E:\\testing.txt', True)
a.Deserialize()
print(a)
'''


def addBlank(d, lis, firstTime=False):
    if d == 1:
        lis.append([])
        if firstTime:
            return lis
    else:
        d -= 1
        addBlank(d, lis[-1])
        if firstTime:
            return lis


a = ['5', 'AY', ['25', 70]]
a = addBlank(1, a, True)
print(a)
'''