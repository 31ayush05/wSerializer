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
        out = '\n' * 2 + '-- DATABASE --' + '\n' * 2
        counter = -1
        for x in self.data:
            counter += 1
            if counter != len(self.data) - 1:
                out += str(x) + ' : ' + str(type(x))[8:-2] + ' - ' + str(type(self.data[x]))[8:-2] + '\n' + ' ' * 5 + \
                       str(self.data[x]) + '\n'
            else:
                out += str(x) + ' : ' + str(type(x))[8:-2] + ' - ' + str(type(self.data[x]))[8:-2] + '\n' + ' ' * 5 + \
                       str(self.data[x])
        return out + '\n'

    def __getitem__(self, item):
        return self.data[str(item)]

    def AddValue(self, name, value, dataSet, d, called=True):
        if called:
            if d == 0:
                self.data[name] = value
            else:
                d -= 1
                self.data[list(self.data.keys())[-1]] = self.AddValue(name, value,
                                                                      self.data[list(self.data.keys())[-1]], d, False)
        else:
            if d == 0:
                dataSet[name] = value
                return dataSet
            else:
                d -= 1
                dataSet[list(dataSet.keys())[-1]] = self.AddValue(name, value,
                                                                  dataSet[list(dataSet.keys())[-1]], d, False)
                return dataSet

    def convertLis(self, d, lis, typeLis='tuple', firstTime=False):
        if d == 1:
            if typeLis == 'tuple':
                lis = tuple(lis)
            else:
                lis = set(lis)
            if firstTime:
                return lis
        else:
            d -= 1
            if typeLis == 'tuple':
                self.convertLis(d, lis[-1], 'tuple')
            else:
                self.convertLis(d, lis[-1], 'set')
            if firstTime:
                return lis

    def keyWiseAdder(self, tString, keyType):
        if tString == '|↑str↑|':
            keyType = 'str'
        elif tString == '|↑int↑|':
            keyType = 'int'
        elif tString == '|↑float↑|':
            keyType = 'float'
        elif tString == '|↑bool↑|':
            keyType = 'bool'
        elif tString == '|↑complex↑|':
            keyType = 'complex'
        else:
            if keyType == 'str':
                self.tempList.append(tString)
                keyType = None
            elif keyType == 'int':
                self.tempList.append(int(tString))
                keyType = None
            elif keyType == 'float':
                self.tempList.append(float(tString))
                keyType = None
            elif keyType == 'bool':
                self.tempList.append(bool(tString))
                keyType = None
            elif keyType == 'complex':
                v = tString.split(' ')
                self.tempList.append(complex(float(v[0]), float(v[1])))
                keyType = None
            else:
                self.tempList.append(tString)
        return keyType

    def addToList(self, d, lis, val, firstTime=False):
        if d == 0:
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

    def Deserialize(self, usersCall=True, data=None):  # ↑ ↓
        self.data = {}
        if self.update:
            self.storeUpdate = True
            self.update = False
        # Decrypt
        # Interpreter ↓↓
        file = open(self.dataFilePath, 'r', encoding='UTF-8')
        b = len(file.readlines())
        file.close()
        listDepth = None
        listStore = None
        readString = False
        readInt = False
        readFloat = False
        readBool = False
        readList = False
        readDict = False
        readComplex = False
        listFirstTime = False
        readInListStr = False
        readInListInt = False
        readInListFloat = False
        readInListBool = False
        readInListComplex = False
        keyType = None
        dictDepth = 0
        file = open(self.dataFilePath, 'r', encoding='UTF-8')
        for x in range(b):
            tString = file.readline()
            if tString[-1] == '\n':
                tString = tString[0:-1]
            if tString == '|↑|dict|↑|':
                dictDepth += 1
                readDict = True
                continue
            if readDict:
                if tString == '|↑str↑|':
                    keyType = 'str'
                elif tString == '|↑int↑|':
                    keyType = 'int'
                elif tString == '|↑float↑|':
                    keyType = 'float'
                elif tString == '|↑bool↑|':
                    keyType = 'bool'
                elif tString == '|↑complex↑|':
                    keyType = 'complex'
                else:
                    if keyType == 'str':
                        self.AddValue(str(tString), {}, self.data, dictDepth - 1)
                        keyType = None
                        readDict = False
                    if keyType == 'int':
                        self.AddValue(int(tString), {}, self.data, dictDepth - 1)
                        keyType = None
                        readDict = False
                    if keyType == 'float':
                        self.AddValue(float(tString), {}, self.data, dictDepth - 1)
                        keyType = None
                        readDict = False
                    if keyType == 'bool':
                        self.AddValue(bool(tString), {}, self.data, dictDepth - 1)
                        keyType = None
                        readDict = False
                    if keyType == 'complex':
                        v = tString.split(' ')
                        self.AddValue(complex(float(v[0]), float(v[1])), {}, self.data, dictDepth - 1)
                        keyType = None
                        readDict = False
            if tString == '|↓|dict|↓|':
                dictDepth -= 1
            if (not readString) and (not readInt) and (not readFloat) and (not readBool) and (not readList) and \
                    (not readComplex):
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
                if tString == '|↑|complex|↑|':
                    readComplex = True
                    self.tempList = []
                if (tString == '|↑|list|↑|') or (tString == '|↑|tuple|↑|') or (tString == '|↑|set|↑|'):
                    readList = True
                    listFirstTime = True
                    listDepth = 1
                    self.tempList = None
                    listStore = []
            else:
                if readString:
                    if tString == '|↓|str|↓|':
                        self.AddValue(self.tempList[0], self.tempList[1], self.data, dictDepth)
                        readString = False
                    else:
                        keyType = self.keyWiseAdder(tString, keyType)
                if readInt:
                    if tString == '|↓|int|↓|':
                        self.AddValue(self.tempList[0], int(self.tempList[1]), self.data, dictDepth)
                        readInt = False
                    else:
                        keyType = self.keyWiseAdder(tString, keyType)
                if readFloat:
                    if tString == '|↓|float|↓|':
                        self.AddValue(self.tempList[0], float(self.tempList[1]), self.data, dictDepth)
                        readFloat = False
                    else:
                        keyType = self.keyWiseAdder(tString, keyType)
                if readBool:
                    if tString == '|↓|bool|↓|':
                        self.AddValue(self.tempList[0], bool(self.tempList[1]), self.data, dictDepth)
                        readBool = False
                    else:
                        keyType = self.keyWiseAdder(tString, keyType)
                if readComplex:
                    if tString == '|↓|complex|↓|':
                        self.AddValue(self.tempList[0], complex(float(self.tempList[1].split(' ')[0]),
                                                                float(self.tempList[1].split(' ')[1])),
                                      self.data, dictDepth)
                        readComplex = False
                    else:
                        keyType = self.keyWiseAdder(tString, keyType)
                if readList:
                    if (tString == '|↓|list|↓|') or (tString == '|↓|tuple|↓|') or (tString == '|↓|set|↓|'):
                        if tString == '|↓|tuple|↓|':
                            listStore = self.convertLis(listDepth, listStore, 'tuple', True)
                        if tString == '|↓|set|↓|':
                            listStore = self.convertLis(listDepth, listStore, 'set', True)
                        self.AddValue(self.tempList, listStore, self.data, dictDepth)
                        readList = False
                    else:
                        if listFirstTime:
                            if tString == '|↑str↑|':
                                keyType = 'str'
                            elif tString == '|↑int↑|':
                                keyType = 'int'
                            elif tString == '|↑float↑|':
                                keyType = 'float'
                            elif tString == '|↑bool↑|':
                                keyType = 'bool'
                            elif tString == '|↑complex↑|':
                                keyType = 'complex'
                            else:
                                if keyType == 'str':
                                    self.tempList = tString
                                    keyType = None
                                    listFirstTime = False
                                if keyType == 'int':
                                    self.tempList = int(tString)
                                    keyType = None
                                    listFirstTime = False
                                if keyType == 'float':
                                    self.tempList = float(tString)
                                    keyType = None
                                    listFirstTime = False
                                if keyType == 'bool':
                                    self.tempList = bool(tString)
                                    keyType = None
                                    listFirstTime = False
                                if keyType == 'complex':
                                    v = tString.split(' ')
                                    self.tempList = complex(float(v[0]), float(v[1]))
                                    keyType = None
                                    listFirstTime = False
                        else:
                            if (tString == '|↓l↓|') or (tString == '|↓t↓|') or (tString == '|↓s↓|'):
                                if tString == '|↓t↓|':
                                    listStore = self.convertLis(listDepth, listStore, 'tuple', True)
                                if tString == '|↓s↓|':
                                    listStore = self.convertLis(listDepth, listStore, 'set', True)
                                listDepth -= 1
                            if (tString == '|↑l↑|') or (tString == '|↑t↑|') or (tString == '|↑s↑|'):
                                listDepth += 1
                                listStore = self.addToList(listDepth - 1, listStore, [], True)
                            if (not readInListStr) and (not readInListInt) and (not readInListBool) and \
                                    (not readInListFloat) and (not readInListComplex):
                                if tString == '|↑|str|↑|':
                                    readInListStr = True
                                if tString == '|↑|int|↑|':
                                    readInListInt = True
                                if tString == '|↑|float|↑|':
                                    readInListFloat = True
                                if tString == '|↑|bool|↑|':
                                    readInListBool = True
                                if tString == '|↑|complex|↑|':
                                    readInListComplex = True
                            else:
                                if readInListStr:
                                    if tString == '|↓|str|↓|':
                                        readInListStr = False
                                    else:
                                        listStore = self.addToList(listDepth - 1, listStore, str(tString), True)
                                if readInListInt:
                                    if tString == '|↓|int|↓|':
                                        readInListInt = False
                                    else:
                                        listStore = self.addToList(listDepth - 1, listStore, int(tString), True)
                                if readInListFloat:
                                    if tString == '|↓|float|↓|':
                                        readInListFloat = False
                                    else:
                                        listStore = self.addToList(listDepth - 1, listStore, float(tString), True)
                                if readInListBool:
                                    if tString == '|↓|bool|↓|':
                                        readInListBool = False
                                    else:
                                        listStore = self.addToList(listDepth - 1, listStore, bool(tString), True)
                                if readInListComplex:
                                    if tString == '|↓|complex|↓|':
                                        readInListComplex = False
                                    else:
                                        listStore = self.addToList(listDepth - 1, listStore,
                                                                   complex(float(tString.split(' ')[0]),
                                                                           float(tString.split(' ')[1])), True)
        file.close()
        if self.storeUpdate:
            self.storeUpdate = None
            self.update = True


a = dataBlock('E:\\testing.txt', True)
a.Deserialize()
print(a)
