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

    def convertLis(self, d, lis, typeLis='tuple'):
        if d == 1:
            if typeLis == 'tuple':
                lis = tuple(lis)
            else:
                lis = set(lis)
            return lis
        else:
            d -= 1
            if typeLis == 'tuple':
                lis[-1] = self.convertLis(d, lis[-1], 'tuple')
            else:
                lis[-1] = self.convertLis(d, lis[-1], 'set')
            return lis

    def keyWiseAdder(self, tString, keyType, dataSet=None, usersCall=True):
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
                if usersCall:
                    self.tempList.append(tString)
                else:
                    dataSet.append(tString)
                keyType = None
            elif keyType == 'int':
                if usersCall:
                    self.tempList.append(int(tString))
                else:
                    dataSet.append(int(tString))
                keyType = None
            elif keyType == 'float':
                if usersCall:
                    self.tempList.append(float(tString))
                else:
                    dataSet.append(float(tString))
                keyType = None
            elif keyType == 'bool':
                if usersCall:
                    self.tempList.append(bool(tString))
                else:
                    dataSet.append(bool(tString))
                keyType = None
            elif keyType == 'complex':
                v = tString.split(' ')
                if usersCall:
                    self.tempList.append(complex(float(v[0]), float(v[1])))
                else:
                    dataSet.append(complex(float(v[0]), float(v[1])))
                keyType = None
            else:
                if usersCall:
                    self.tempList.append(tString)
                else:
                    dataSet.append(tString)
        if usersCall:
            return keyType
        else:
            return [keyType, dataSet]

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
        if usersCall:
            self.data = {}
            if self.update:
                self.storeUpdate = True
                self.update = False
            file = open(self.dataFilePath, 'r', encoding='UTF-8')
            b = len(file.readlines())
            file.close()
        else:
            b = len(data)
        tempData = {}
        dictToRead = []
        tempList = []
        file = None
        keyType = None
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
        readDictInList = 0
        dictDepth = 0
        if usersCall:
            file = open(self.dataFilePath, 'r', encoding='UTF-8')
        for x in range(b):
            if usersCall:
                tString = file.readline()
            else:
                tString = data[x]
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
                        if usersCall:
                            self.AddValue(str(tString), {}, self.data, dictDepth - 1)
                        else:
                            tempData = self.AddValue(str(tString), {}, tempData, dictDepth - 1, False)
                        keyType = None
                        readDict = False
                    if keyType == 'int':
                        if usersCall:
                            self.AddValue(int(tString), {}, self.data, dictDepth - 1)
                        else:
                            tempData = self.AddValue(int(tString), {}, tempData, dictDepth - 1, False)
                        keyType = None
                        readDict = False
                    if keyType == 'float':
                        if usersCall:
                            self.AddValue(float(tString), {}, self.data, dictDepth - 1)
                        else:
                            tempData = self.AddValue(float(tString), {}, tempData, dictDepth - 1, False)
                        keyType = None
                        readDict = False
                    if keyType == 'bool':
                        if usersCall:
                            self.AddValue(bool(tString), {}, self.data, dictDepth - 1)
                        else:
                            tempData = self.AddValue(bool(tString), {}, tempData, dictDepth - 1, False)
                        keyType = None
                        readDict = False
                    if keyType == 'complex':
                        v = tString.split(' ')
                        if usersCall:
                            self.AddValue(complex(float(v[0]), float(v[1])), {}, self.data, dictDepth - 1)
                        else:
                            tempData = self.AddValue(complex(float(v[0]), float(v[1])), {}, tempData, dictDepth - 1,
                                                     False)
                        keyType = None
                        readDict = False
            if tString == '|↓|dict|↓|':
                dictDepth -= 1
            if (not readString) and (not readInt) and (not readFloat) and (not readBool) and (not readList) and \
                    (not readComplex):
                if tString == '|↑|str|↑|':
                    readString = True
                    if usersCall:
                        self.tempList = []
                    else:
                        tempList = []
                if tString == '|↑|int|↑|':
                    readInt = True
                    if usersCall:
                        self.tempList = []
                    else:
                        tempList = []
                if tString == '|↑|float|↑|':
                    readFloat = True
                    if usersCall:
                        self.tempList = []
                    else:
                        tempList = []
                if tString == '|↑|bool|↑|':
                    readBool = True
                    if usersCall:
                        self.tempList = []
                    else:
                        tempList = []
                if tString == '|↑|complex|↑|':
                    readComplex = True
                    if usersCall:
                        self.tempList = []
                    else:
                        tempList = []
                if (tString == '|↑|list|↑|') or (tString == '|↑|tuple|↑|') or (tString == '|↑|set|↑|'):
                    readList = True
                    listFirstTime = True
                    listDepth = 1
                    listStore = []
                    if usersCall:
                        self.tempList = []
                    else:
                        tempList = []
            else:
                if readString:
                    if tString == '|↓|str|↓|':
                        if usersCall:
                            self.AddValue(self.tempList[0], self.tempList[1], self.data, dictDepth)
                        else:
                            tempData = self.AddValue(tempList[0], tempList[1], tempData, dictDepth, False)
                        readString = False
                    else:
                        if usersCall:
                            keyType = self.keyWiseAdder(tString, keyType)
                        else:
                            m = self.keyWiseAdder(tString, keyType, tempList, False)
                            keyType = m[0]
                            tempList = m[1]
                if readInt:
                    if tString == '|↓|int|↓|':
                        if usersCall:
                            self.AddValue(self.tempList[0], int(self.tempList[1]), self.data, dictDepth)
                        else:
                            tempData = self.AddValue(tempList[0], int(tempList[1]), tempData, dictDepth, False)
                        readInt = False
                    else:
                        if usersCall:
                            keyType = self.keyWiseAdder(tString, keyType)
                        else:
                            m = self.keyWiseAdder(tString, keyType, tempData, False)
                            keyType = m[0]
                            tempList = m[1]
                if readFloat:
                    if tString == '|↓|float|↓|':
                        if usersCall:
                            self.AddValue(self.tempList[0], float(self.tempList[1]), self.data, dictDepth)
                        else:
                            tempData = self.AddValue(tempList[0], float(tempList[1]), tempData, dictDepth, False)
                        readFloat = False
                    else:
                        if usersCall:
                            keyType = self.keyWiseAdder(tString, keyType)
                        else:
                            m = self.keyWiseAdder(tString, keyType, tempData, False)
                            keyType = m[0]
                            tempList = m[1]
                if readBool:
                    if tString == '|↓|bool|↓|':
                        if usersCall:
                            self.AddValue(self.tempList[0], bool(self.tempList[1]), self.data, dictDepth)
                        else:
                            tempData = self.AddValue(tempList[0], bool(tempList[1]), tempData, dictDepth, False)
                        readBool = False
                    else:
                        if usersCall:
                            keyType = self.keyWiseAdder(tString, keyType)
                        else:
                            m = self.keyWiseAdder(tString, keyType, tempData, False)
                            keyType = m[0]
                            tempList = m[1]
                if readComplex:
                    if tString == '|↓|complex|↓|':
                        if usersCall:
                            n = self.tempList[1].split(' ')
                            self.AddValue(self.tempList[0], complex(float(n[0]), float(n[1])), self.data, dictDepth)
                        else:
                            n = tempList[1].split(' ')
                            tempData = self.AddValue(tempList[0], complex(float(n[0]), float(n[1])), tempData,
                                                     dictDepth, False)
                        readComplex = False
                    else:
                        if usersCall:
                            keyType = self.keyWiseAdder(tString, keyType)
                        else:
                            m = self.keyWiseAdder(tString, keyType, tempData, False)
                            keyType = m[0]
                            tempList = m[1]
                if readList:
                    if ((tString == '|↓|list|↓|') or (tString == '|↓|tuple|↓|') or (tString == '|↓|set|↓|')) and (
                            readDictInList == 0):
                        if tString == '|↓|tuple|↓|':
                            listStore = self.convertLis(listDepth, listStore, 'tuple')
                        if tString == '|↓|set|↓|':
                            listStore = self.convertLis(listDepth, listStore, 'set')
                        if usersCall:
                            self.AddValue(self.tempList, listStore, self.data, dictDepth)
                        else:
                            tempData = self.AddValue(tempList, listStore, tempData, dictDepth, False)
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
                                    if usersCall:
                                        self.tempList = tString
                                    else:
                                        tempList = tString
                                    keyType = None
                                    listFirstTime = False
                                if keyType == 'int':
                                    if usersCall:
                                        self.tempList = int(tString)
                                    else:
                                        tempList = int(tString)
                                    keyType = None
                                    listFirstTime = False
                                if keyType == 'float':
                                    if usersCall:
                                        self.tempList = float(tString)
                                    else:
                                        tempList = float(tString)
                                    keyType = None
                                    listFirstTime = False
                                if keyType == 'bool':
                                    if usersCall:
                                        self.tempList = bool(tString)
                                    else:
                                        tempList = bool(tString)
                                    keyType = None
                                    listFirstTime = False
                                if keyType == 'complex':
                                    v = tString.split(' ')
                                    if usersCall:
                                        self.tempList = complex(float(v[0]), float(v[1]))
                                    else:
                                        tempList = complex(float(v[0]), float(v[1]))
                                    keyType = None
                                    listFirstTime = False
                        else:
                            if (tString == '|↓l↓|') or (tString == '|↓t↓|') or (tString == '|↓s↓|'):
                                if tString == '|↓t↓|':
                                    listStore = self.convertLis(listDepth, listStore, 'tuple')
                                if tString == '|↓s↓|':
                                    listStore = self.convertLis(listDepth, listStore, 'set')
                                listDepth -= 1
                            if (tString == '|↑l↑|') or (tString == '|↑t↑|') or (tString == '|↑s↑|'):
                                listStore = self.addToList(listDepth - 1, listStore, [], True)
                                listDepth += 1
                            if tString == '|↑|dictInList|↑|':
                                if readDictInList == 0:
                                    dictToRead = []
                                readDictInList += 1
                            if (not readInListStr) and (not readInListInt) and (not readInListBool) and \
                                    (not readInListFloat) and (not readInListComplex) and (readDictInList == 0):
                                if (tString == '|↑|str|↑|') and (readDictInList == 0):
                                    readInListStr = True
                                if (tString == '|↑|int|↑|') and (readDictInList == 0):
                                    readInListInt = True
                                if (tString == '|↑|float|↑|') and (readDictInList == 0):
                                    readInListFloat = True
                                if (tString == '|↑|bool|↑|') and (readDictInList == 0):
                                    readInListBool = True
                                if (tString == '|↑|complex|↑|') and (readDictInList == 0):
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
                                if readDictInList != 0:
                                    if tString == '|↓|dictInList|↓|':
                                        readDictInList -= 1
                                        if readDictInList == 0:
                                            listStore = self.addToList(listDepth - 1, listStore,
                                                                       self.Deserialize(False, dictToRead), True)
                                        else:
                                            dictToRead.append(tString)
                                    else:
                                        dictToRead.append(tString)
        if usersCall:
            file.close()
        if self.storeUpdate and usersCall:
            self.storeUpdate = None
            self.update = True
        if not usersCall:
            return tempData


a = dataBlock('E:\\testing.txt', True)
a.Deserialize()
print(a)
