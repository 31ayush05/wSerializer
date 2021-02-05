from os import path


class dataBlock:

    def __init__(self, filePath, autoUpdate=False):
        self.storeUpdate = None
        self.tempList = None
        self.listDepth = None
        self.listStore = None
        self.dictDepth = 0
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
        readDict = False
        readComplex = False
        listFirstTime = False
        readInListStr = False
        readInListInt = False
        readInListFloat = False
        readInListBool = False
        readInListComplex = False
        file = open(self.dataFilePath, 'r', encoding='UTF-8')
        for x in range(b):
            tString = file.readline()
            if tString[-1] == '\n':
                tString = tString[0:-1]
            if tString == '|↑|dict|↑|':
                self.dictDepth += 1
                readDict = True
                continue
            if readDict:
                readDict = False
                self.AddValue(str(tString), {}, self.data, self.dictDepth - 1)
            if tString == '|↓|dict|↓|':
                self.dictDepth -= 1
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
                    self.listDepth = 1
                    self.tempList = None
                    self.listStore = []
            else:
                if readString:
                    if tString == '|↓|str|↓|':
                        self.AddValue(self.tempList[0], self.tempList[1], self.data, self.dictDepth)
                        readString = False
                    else:
                        self.tempList.append(tString)
                if readInt:
                    if tString == '|↓|int|↓|':
                        self.AddValue(self.tempList[0], int(self.tempList[1]), self.data, self.dictDepth)
                        readInt = False
                    else:
                        self.tempList.append(tString)
                if readFloat:
                    if tString == '|↓|float|↓|':
                        self.AddValue(self.tempList[0], float(self.tempList[1]), self.data, self.dictDepth)
                        readFloat = False
                    else:
                        self.tempList.append(tString)
                if readBool:
                    if tString == '|↓|bool|↓|':
                        self.AddValue(self.tempList[0], bool(self.tempList[1]), self.data, self.dictDepth)
                        readBool = False
                    else:
                        self.tempList.append(tString)  # self.tempList[1]
                if readComplex:
                    if tString == '|↓|complex|↓|':
                        self.AddValue(self.tempList[0], complex(float(self.tempList[1].split(' ')[0]),
                                                                float(self.tempList[1].split(' ')[1])),
                                      self.data, self.dictDepth)
                        readComplex = False
                    else:
                        self.tempList.append(tString)
                if readList:
                    if (tString == '|↓|list|↓|') or (tString == '|↓|tuple|↓|') or (tString == '|↓|set|↓|'):
                        if tString == '|↓|tuple|↓|':
                            self.listStore = self.convertLis(self.listDepth, self.listStore, 'tuple', True)
                        if tString == '|↓|set|↓|':
                            self.listStore = self.convertLis(self.listDepth, self.listStore, 'set', True)
                        self.AddValue(self.tempList, self.listStore, self.data, self.dictDepth)
                        readList = False
                    else:
                        if listFirstTime:
                            self.tempList = str(tString)
                            listFirstTime = False
                        else:
                            if (tString == '|↓l↓|') or (tString == '|↓t↓|') or (tString == '|↓s↓|'):
                                if tString == '|↓t↓|':
                                    self.listStore = self.convertLis(self.listDepth, self.listStore, 'tuple', True)
                                if tString == '|↓s↓|':
                                    self.listStore = self.convertLis(self.listDepth, self.listStore, 'set', True)
                                self.listDepth -= 1
                            if (tString == '|↑l↑|') or (tString == '|↑t↑|') or (tString == '|↑s↑|'):
                                self.listDepth += 1
                                self.listStore = self.addBlank(self.listDepth - 1, self.listStore, True)
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
                                        self.listStore = self.addToList(self.listDepth, self.listStore, str(tString),
                                                                        True)
                                if readInListInt:
                                    if tString == '|↓|int|↓|':
                                        readInListInt = False
                                    else:
                                        self.listStore = self.addToList(self.listDepth, self.listStore, int(tString),
                                                                        True)
                                if readInListFloat:
                                    if tString == '|↓|float|↓|':
                                        readInListFloat = False
                                    else:
                                        self.listStore = self.addToList(self.listDepth, self.listStore, float(tString),
                                                                        True)
                                if readInListBool:
                                    if tString == '|↓|bool|↓|':
                                        readInListBool = False
                                    else:
                                        self.listStore = self.addToList(self.listDepth, self.listStore, bool(tString),
                                                                        True)
                                if readInListComplex:
                                    if tString == '|↓|complex|↓|':
                                        readInListComplex = False
                                    else:
                                        self.listStore = self.addToList(self.listDepth, self.listStore,
                                                                        complex(float(tString.split(' ')[0]),
                                                                                float(tString.split(' ')[1])), True)
        file.close()
        if self.storeUpdate:
            self.storeUpdate = None
            self.update = True


'''
a = dataBlock('E:\\testing.txt', False)
a.data = {}
a.AddValue('name', 'value', a.data, 0)
a.AddValue('dict', {}, a.data, 0)
a.AddValue('a', [1,2,3,4], a.data, 1)
a.AddValue('b', 'value 2', a.data, 1)
a.AddValue('dict 2', {}, a.data, 1)
a.AddValue('me', 3105, a.data, 2)
print(a)
'''
a = dataBlock('E:\\testing.txt', True)
a.Deserialize()
print(a)
