from os import path


class dataBlock:
    """
    A python class capable of serializing data in the form of predefined data types that include -
    INT, FLOAT, STR, BOOL, COMPLEX, LIST, TUPLE, DICT, SET
    You can add infinitely many LISTS, TUPLES, DICTS or SETS inside other LISTS, TUPLES, DICTS or SETS and also
    successfully retriving them by using the specific variable names.

    Author : Ayush Yadav
    GitHub : https://github.com/31ayush05
    Link to this repo : https://github.com/31ayush05/wSerializer
    """

    def __init__(self, filePath, autoSync=False):
        """
        dataBlock is the block of data in which you are going to store numerous values linked to their specific
        names(variable names).
        Then in future you can access the values of variables using the variable names

        #RESTRICTIONS
        don't use keywords reserved by this library as names or values
        variable names cannot be TUPLES, DICT, LIST or SET

        #RESERVED KEYWORDS
        |↑|int|↑| |↓|int|↓| |↑int↑|
        |↑|str|↑| |↓|str|↓| |↑str↑|
        |↑|float|↑|  |↓|float|↓| |↑float↑|
        |↑|bool|↑| |↓|bool|↓| |↑bool↑|
        |↑|complex|↑| |↓|complex|↓| |↑complex↑|
        |↑|dict|↑| |↓|dict|↓| |↑|dictInList|↑| |↓|dictInList|↓|
        |↑|list|↑| |↓|list|↓| |↑l↑| |↓l↓|
        |↑|tuple|↑| |↓|tuple|↓| |↑t↑| |↓t↓|
        |↑|set|↑| |↓|set|↓| |↑s↑| |↓s↓|
        :param filePath: Path of the file to which data is to be written
        :param autoSync: if enabled it will update the dataFile as soon as new variables are added
        """
        self.storeUpdate = None
        self.tempList = None
        self.update = autoSync
        self.reservedKeywords = (
            '|↑|int|↑|', '|↓|int|↓|', '|↑int↑|',
            '|↑|str|↑|', '|↓|str|↓|', '|↑str↑|',
            '|↑|float|↑|', '|↓|float|↓|', '|↑float↑|',
            '|↑|bool|↑|', '|↓|bool|↓|', '|↑bool↑|',
            '|↑|complex|↑|', '|↓|complex|↓|', '|↑complex↑|',
            '|↑|dict|↑|', '|↓|dict|↓|',
            '|↑|dictInList|↑|', '|↓|dictInList|↓|',
            '|↑|list|↑|', '|↓|list|↓|', '|↑l↑|', '|↓l↓|',
            '|↑|tuple|↑|', '|↓|tuple|↓|', '|↑t↑|', '|↓t↓|',
            '|↑|set|↑|', '|↓|set|↓|', '|↑s↑|', '|↓s↓|'
        )
        self.data = {}
        if not path.exists(filePath):
            file = open(filePath, 'x')
            file.close()
        self.dataFilePath = filePath
        self.Deserializer()

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

    def reset(self):
        """
        resets the dataBlock that is the data resets back to {}.

        Moreover the data file is emptied.
        
        If the specified file does not exist a new blank file is created at the defined file path
        :returns: nothing
        """
        if path.exists(self.dataFilePath):
            file = open(self.dataFilePath, 'w')
            file.truncate(0)
            file.close()
        else:
            file = open(self.dataFilePath, 'x')
            file.close()
        self.__init__(self.dataFilePath, self.update)

    def Add(self, name, value):
        """
        Function responsible for adding new variables with their values to the dataBlock.
        Using this "name" the specified value can be accessed in future.
        :param name: name of the variable
        :param value: value to be stored in the variable
        :return: nothing
        """
        if not (name in self.data):
            if not (name in self.reservedKeywords):
                if not (value in self.reservedKeywords):
                    self.AddValue(name, value, None, 0, True)
                    if self.update:
                        self.Serialize()
                else:
                    print('variable value : ' + str(value) + ' is a reserved keyword')
            else:
                print('variable name : ' + str(name) + ' is a reserved keyword')
        else:
            print('Similar name exists cannot create duplicate names')

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

    def Deserialize(self, printOutPut):
        """
        This function is responsible for Deserializing the data previously stored in the specified file.
        Once the data is Deserialized it can be accessed anytime while the code is still running.
        The code tries to Deserialize a file if exists once the dataBlock is created thus you don't need to call it
        again and again.
        :param printOutPut: if set True prints the dataSet every time called
        :return: nothing
        """
        self.Deserializer(printOutPut)

    def Deserializer(self, printOutPut=False, usersCall=True, data=None):
        if usersCall:
            self.data = {}
            if self.update:
                self.storeUpdate = True
                self.update = False
            if path.exists(self.dataFilePath):
                file = open(self.dataFilePath, 'r', encoding='UTF-8')
            else:
                print('Defined file path does not exist')
                return None
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
        justNow = False
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
            if path.exists(self.dataFilePath):
                file = open(self.dataFilePath, 'r', encoding='UTF-8')
            else:
                print('Defined file path does not exist')
                return None
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
                            m = self.keyWiseAdder(tString, keyType, tempList, False)
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
                            m = self.keyWiseAdder(tString, keyType, tempList, False)
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
                            m = self.keyWiseAdder(tString, keyType, tempList, False)
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
                            m = self.keyWiseAdder(tString, keyType, tempList, False)
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
                                    justNow = True
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
                                                                       self.Deserializer(False, False, dictToRead), True)
                                        else:
                                            dictToRead.append(tString)
                                    else:
                                        if not justNow:
                                            dictToRead.append(tString)
                                        else:
                                            justNow = False
        if usersCall:
            file.close()
        if self.storeUpdate and usersCall:
            self.storeUpdate = None
            self.update = True
        if not usersCall:
            return tempData
        else:
            if printOutPut:
                print(self.__str__())

    def basicVarSerializer(self, key, value, outOfList=True):
        tpe = str(type(value))[8:-2]
        out = '|↑|' + tpe + '|↑|\n'
        if outOfList:
            er = str(type(key))[8:-2]
            if (er == 'str') or (er != 'int') or (er != 'float') or (er != 'bool') or (er != 'complex'):
                out += '|↑' + er + '↑|\n'
                if er != 'complex':
                    out += str(key) + '\n'
                else:
                    out += str(key.real) + ' ' + str(key.imag) + '\n'
        if tpe == 'complex':
            out += str(value.real) + ' ' + str(value.imag) + '\n' + '|↓|' + tpe + '|↓|\n'
        else:
            out += str(value) + '\n' + '|↓|' + tpe + '|↓|\n'
        return out

    def serializeLTS(self, key, value, LoD):
        out = ''
        tpe = str(type(value))[8:-2]
        if (LoD == 0) or (LoD == 1):
            out += '|↑|' + tpe + '|↑|\n'
            er = str(type(key))[8:-2]
            if (er == 'str') or (er != 'int') or (er != 'float') or (er != 'bool') or (er != 'complex'):
                out += '|↑' + er + '↑|\n'
                if er != 'complex':
                    out += str(key) + '\n'
                else:
                    out += str(key.real) + ' ' + str(key.imag) + '\n'
        else:
            out += '|↑' + tpe[0] + '↑|\n'
        for x in value:
            tpe = str(type(x))[8:-2]
            if (tpe == 'list') or (tpe == 'tuple') or (tpe == 'set'):
                out += self.serializeLTS(None, x, -1)
            elif (tpe == 'str') or (tpe == 'int') or (tpe == 'bool') or (tpe == 'float') or (tpe == 'complex'):
                out += self.basicVarSerializer(None, x, False)
            elif tpe == 'dict':
                out += self.serializeDICT(None, x, -1)
            else:
                print('Unrecognizable data-type')
        if (LoD == 0) or (LoD == 1):
            out += '|↓|' + str(type(value))[8:-2] + '|↓|\n'
        else:
            out += '|↓' + str(type(value))[8:-2][0] + '↓|\n'
        return out

    def serializeDICT(self, key, value, LoD):
        out = ''
        if LoD == -1:
            out += '|↑|dictInList|↑|\n'
        else:
            out += '|↑|dict|↑|\n'
            er = str(type(key))[8:-2]
            if (er == 'str') or (er == 'int') or (er == 'float') or (er == 'bool') or (er == 'complex'):
                out += '|↑' + er + '↑|\n'
                if er != 'complex':
                    out += str(key) + '\n'
                else:
                    out += str(key.real) + ' ' + str(key.imag) + '\n'
        for x in value:
            tpe = str(type(value[x]))[8:-2]
            if (tpe == 'str') or (tpe == 'int') or (tpe == 'float') or (tpe == 'bool') or (tpe == 'complex'):
                out += self.basicVarSerializer(x, value[x])
            elif (tpe == 'list') or (tpe == 'tuple') or (tpe == 'dict'):
                out += self.serializeLTS(x, value[x], 1)
            elif tpe == 'dict':
                out += self.serializeDICT(x, value[x], 1)
            else:
                print('Unrecognizable data-type')
        if LoD == -1:
            out += '|↓|dictInList|↓|\n'
        else:
            out += '|↓|dict|↓|\n'
        return out

    def Serialize(self):
        """
        Serializes the data stored by you in the dataSet using the Add() function that is it writes the data in the
        specified text file
        :return: nothing
        """
        out = ''
        for x in self.data:
            tpe = str(type(self.data[x]))[8:-2]
            if (tpe == 'int') or (tpe == 'float') or (tpe == 'bool') or (tpe == 'str') or (tpe == 'complex'):
                out += self.basicVarSerializer(x, self.data[x], True)
            elif (tpe == 'set') or (tpe == 'tuple') or (tpe == 'list'):
                out += self.serializeLTS(x, self.data[x], 0)
            elif tpe == 'dict':
                out += self.serializeDICT(x, self.data[x], 0)
            else:
                print('ERROR')
        if path.exists(self.dataFilePath):
            f = open(self.dataFilePath, 'r', encoding='UTF-8')
            f.truncate(0)
            f.write(out)
            f.close()
        else:
            f = open(self.dataFilePath, 'x', encoding='UTF-8')
            f.truncate(0)
            f.write(out)
            f.close()


a = dataBlock('E://testing.txt', True)
'''
a.Add('name', 'JOHN')
a.Add('subjects', ['maths', 'chemistry', 'physics', 'physical education', 'english', 'computer science'])
a.Add('marks', [99.85, 91.1, 85, 100, 80, 100])
'''
print(a['subjects'])
