import unittest
import wSerializer.wSerializer as wSL


class test_targeted(unittest.TestCase):
    """
    STR - int float complex list tuple set dict
    BOOL - str bool int float complex list tuple set dict
    INT - str bool int float complex list tuple set dict
    FLOAT - str bool int float complex list tuple set dict
    COMPLEX - str bool int float complex list tuple set dict

    add - retrieve         : outputs same : AR
    update - retrieve      : outputs      : UR
    add duplicate          : raises error : AD
    retrieve non existing  : raises error : RNE
    containing check       : T/F          : CC
    add name = reserved    : raises error : ANR
    value name = reserved  : raises error : VNR
    remove check exists    : T/F          : RCE
    """

    # region STR TESTS

    # region STR-STR

    def test_str_str_AR(self):
        SL = wSL.dataBlock('E:\\test.txt')
        SL.reset()
        # Method 1 --------------------------------------------
        # ADD
        SL.Add('variable 1', 'value 1')
        SL.Add('variable 2', 'value 2')
        SL.Add('variable 3', 'value 3')
        SL.Add('variable 4', 'value 4')
        # LOAD
        self.assertEqual(SL['variable 1'], 'value 1')
        self.assertEqual(SL['variable 2'], 'value 2')
        self.assertEqual(SL['variable 3'], 'value 3')
        self.assertEqual(SL['variable 4'], 'value 4')
        # Method 2 --------------------------------------------
        # ADD
        SL['variable 5'] = 'value 5'
        SL['variable 6'] = 'value 6'
        SL['variable 7'] = 'value 7'
        SL['variable 8'] = 'value 8'
        # LOAD
        self.assertEqual(SL['variable 5'], 'value 5')
        self.assertEqual(SL['variable 6'], 'value 6')
        self.assertEqual(SL['variable 7'], 'value 7')
        self.assertEqual(SL['variable 8'], 'value 8')

    def test_str_str_UR(self):
        SL = wSL.dataBlock('E:\\test.txt')
        SL.reset()
        # ADD -------------------------------------------------
        SL.Add('variable 1', 'value 1')
        SL.Add('variable 2', 'value 2')
        SL.Add('variable 3', 'value 3')
        SL.Add('variable 4', 'value 4')
        # UPDATE ----------------------------------------------
        SL['variable 1'] = 'updated value 1'
        SL['variable 2'] = 'updated value 2'
        SL['variable 3'] = 'updated value 3'
        SL['variable 4'] = 'updated value 4'
        # CHECK -----------------------------------------------
        self.assertEqual(SL['variable 1'], 'updated value 1')
        self.assertEqual(SL['variable 2'], 'updated value 2')
        self.assertEqual(SL['variable 3'], 'updated value 3')
        self.assertEqual(SL['variable 4'], 'updated value 4')

    def test_str_str_AD(self):
        SL = wSL.dataBlock('E:\\test.txt')
        SL.reset()
        # ADD -------------------------------------------------
        SL.Add('var 1', 'val 1')
        SL.Add('var 2', 'val 2')
        # ADD DUPLICATE ---------------------------------------
        self.assertRaises(KeyError, SL.Add, 'var 1', 'new value')
        self.assertRaises(KeyError, SL.Add, 'var 2', 'new value')

    def test_str_str_RNE(self):
        SL = wSL.dataBlock('E:\\test.txt')
        SL.reset()
        # ADD -------------------------------------------------
        SL.Add('var 1', 'val 1')
        SL.Add('var 2', 'val 2')
        # RETRIEVE NON - EXISTING -----------------------------
        self.assertRaises(KeyError, SL.__getitem__, 'var 3')
        self.assertRaises(KeyError, SL.__getitem__, 'var 4')

    def test_str_str_CC(self):
        SL = wSL.dataBlock('E:\\test.txt')
        SL.reset()
        # ADD -------------------------------------------------
        SL.Add('var 1', 'val 1')
        SL.Add('var 2', 'val 2')
        # CHECK EXISTING --------------------------------------
        # TRUE ------------------------------------------------
        self.assertEqual(SL.__contains__('var 1'), True)
        self.assertEqual(SL.__contains__('var 2'), True)
        # FALSE -----------------------------------------------
        self.assertEqual(SL.__contains__('var 3'), False)
        self.assertEqual(SL.__contains__('var 4'), False)

    def test_str_str_ANR(self):
        reservedKeywords = (
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
        SL = wSL.dataBlock('E:\\test.txt')
        SL.reset()
        # ADD -------------------------------------------------
        for x in reservedKeywords:
            self.assertRaises(KeyError, SL.Add, x, 'value')

    def test_str_str_VNR(self):
        reservedKeywords = (
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
        SL = wSL.dataBlock('E:\\test.txt')
        SL.reset()
        # ADD -------------------------------------------------
        for x in reservedKeywords:
            self.assertRaises(ValueError, SL.Add, 'name', x)

    def test_str_str_RCE(self):
        SL = wSL.dataBlock('E:\\test.txt')
        SL.reset()
        # ADD -------------------------------------------------
        SL.Add('var 1', 'val 1')
        SL.Add('var 2', 'val 2')
        # REMOVE NON EXISTING ---------------------------------
        self.assertRaises(KeyError, SL.Remove, 'var 3')
        self.assertRaises(KeyError, SL.Remove, 'var 4')

    # endregion

    # region STR-BOOL

    def test_str_bool_AR(self):
        SL = wSL.dataBlock('E:\\test.txt')
        SL.reset()
        # Method 1 --------------------------------------------
        # ADD
        SL.Add('variable 1', True)
        SL.Add('variable 2', False)
        SL.Add('variable 3', True)
        SL.Add('variable 4', False)
        # LOAD
        self.assertEqual(SL['variable 1'], True)
        self.assertEqual(SL['variable 2'], False)
        self.assertEqual(SL['variable 3'], True)
        self.assertEqual(SL['variable 4'], False)
        # Method 2 --------------------------------------------
        # ADD
        SL['variable 5'] = True
        SL['variable 6'] = False
        SL['variable 7'] = True
        SL['variable 8'] = False
        # LOAD
        self.assertEqual(SL['variable 5'], True)
        self.assertEqual(SL['variable 6'], False)
        self.assertEqual(SL['variable 7'], True)
        self.assertEqual(SL['variable 8'], False)

    def test_str_bool_UR(self):
        SL = wSL.dataBlock('E:\\test.txt')
        SL.reset()
        # ADD -------------------------------------------------
        SL.Add('variable 1', True)
        SL.Add('variable 2', False)
        SL.Add('variable 3', True)
        SL.Add('variable 4', False)
        # UPDATE ----------------------------------------------
        SL['variable 1'] = False
        SL['variable 2'] = True
        SL['variable 3'] = False
        SL['variable 4'] = True
        # CHECK -----------------------------------------------
        self.assertEqual(SL['variable 1'], False)
        self.assertEqual(SL['variable 2'], True)
        self.assertEqual(SL['variable 3'], False)
        self.assertEqual(SL['variable 4'], True)

    def test_str_bool_AD(self):
        SL = wSL.dataBlock('E:\\test.txt')
        SL.reset()
        # ADD -------------------------------------------------
        SL.Add('var 1', True)
        SL.Add('var 2', True)
        # ADD DUPLICATE ---------------------------------------
        self.assertRaises(KeyError, SL.Add, 'var 1', False)
        self.assertRaises(KeyError, SL.Add, 'var 2', False)

    def test_str_bool_RNE(self):
        SL = wSL.dataBlock('E:\\test.txt')
        SL.reset()
        # ADD -------------------------------------------------
        SL.Add('var 1', True)
        SL.Add('var 2', True)
        # RETRIEVE NON - EXISTING -----------------------------
        self.assertRaises(KeyError, SL.__getitem__, 'var 3')
        self.assertRaises(KeyError, SL.__getitem__, 'var 4')

    def test_str_bool_CC(self):
        SL = wSL.dataBlock('E:\\test.txt')
        SL.reset()
        # ADD -------------------------------------------------
        SL.Add('var 1', True)
        SL.Add('var 2', False)
        # CHECK EXISTING --------------------------------------
        # TRUE ------------------------------------------------
        self.assertEqual(SL.__contains__('var 1'), True)
        self.assertEqual(SL.__contains__('var 2'), True)
        # FALSE -----------------------------------------------
        self.assertEqual(SL.__contains__('var 3'), False)
        self.assertEqual(SL.__contains__('var 4'), False)

    def test_str_bool_ANR(self):
        reservedKeywords = (
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
        SL = wSL.dataBlock('E:\\test.txt')
        SL.reset()
        # ADD -------------------------------------------------
        for x in reservedKeywords:
            self.assertRaises(KeyError, SL.Add, x, True)

    def test_str_bool_RCE(self):
        SL = wSL.dataBlock('E:\\test.txt')
        SL.reset()
        # ADD -------------------------------------------------
        SL.Add('var 1', False)
        SL.Add('var 2', False)
        # REMOVE NON EXISTING ---------------------------------
        self.assertRaises(KeyError, SL.Remove, 'var 3')
        self.assertRaises(KeyError, SL.Remove, 'var 4')

    # endregion

    # region STR-INT

    def test_str_int_AR(self):
        SL = wSL.dataBlock('E:\\test.txt')
        SL.reset()
        # Method 1 --------------------------------------------
        # ADD
        SL.Add('variable 1', 123)
        SL.Add('variable 2', 356)
        SL.Add('variable 3', 549)
        SL.Add('variable 4', 791)
        # LOAD
        self.assertEqual(SL['variable 1'], 123)
        self.assertEqual(SL['variable 2'], 356)
        self.assertEqual(SL['variable 3'], 549)
        self.assertEqual(SL['variable 4'], 791)
        # Method 2 --------------------------------------------
        # ADD
        SL['variable 5'] = 564
        SL['variable 6'] = 951
        SL['variable 7'] = 987
        SL['variable 8'] = 254
        # LOAD
        self.assertEqual(SL['variable 5'], 564)
        self.assertEqual(SL['variable 6'], 951)
        self.assertEqual(SL['variable 7'], 987)
        self.assertEqual(SL['variable 8'], 254)

    def test_str_int_UR(self):
        SL = wSL.dataBlock('E:\\test.txt')
        SL.reset()
        # ADD -------------------------------------------------
        SL.Add('variable 1', 149)
        SL.Add('variable 2', 654)
        SL.Add('variable 3', 988)
        SL.Add('variable 4', 284)
        # UPDATE ----------------------------------------------
        SL['variable 1'] = 546
        SL['variable 2'] = 156
        SL['variable 3'] = 148
        SL['variable 4'] = 954
        # CHECK -----------------------------------------------
        self.assertEqual(SL['variable 1'], 546)
        self.assertEqual(SL['variable 2'], 156)
        self.assertEqual(SL['variable 3'], 148)
        self.assertEqual(SL['variable 4'], 954)

    def test_str_int_AD(self):
        SL = wSL.dataBlock('E:\\test.txt')
        SL.reset()
        # ADD -------------------------------------------------
        SL.Add('var 1', 154)
        SL.Add('var 2', 174)
        # ADD DUPLICATE ---------------------------------------
        self.assertRaises(KeyError, SL.Add, 'var 1', False)
        self.assertRaises(KeyError, SL.Add, 'var 2', False)

    def test_str_int_RNE(self):
        SL = wSL.dataBlock('E:\\test.txt')
        SL.reset()
        # ADD -------------------------------------------------
        SL.Add('var 1', 145)
        SL.Add('var 2', 148)
        # RETRIEVE NON - EXISTING -----------------------------
        self.assertRaises(KeyError, SL.__getitem__, 'var 3')
        self.assertRaises(KeyError, SL.__getitem__, 'var 4')

    def test_str_int_CC(self):
        SL = wSL.dataBlock('E:\\test.txt')
        SL.reset()
        # ADD -------------------------------------------------
        SL.Add('var 1', 145)
        SL.Add('var 2', 515)
        # CHECK EXISTING --------------------------------------
        # TRUE ------------------------------------------------
        self.assertEqual(SL.__contains__('var 1'), True)
        self.assertEqual(SL.__contains__('var 2'), True)
        # FALSE -----------------------------------------------
        self.assertEqual(SL.__contains__('var 3'), False)
        self.assertEqual(SL.__contains__('var 4'), False)

    def test_str_int_ANR(self):
        reservedKeywords = (
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
        SL = wSL.dataBlock('E:\\test.txt')
        SL.reset()
        # ADD -------------------------------------------------
        for x in reservedKeywords:
            self.assertRaises(KeyError, SL.Add, x, 111)

    def test_str_int_RCE(self):
        SL = wSL.dataBlock('E:\\test.txt')
        SL.reset()
        # ADD -------------------------------------------------
        SL.Add('var 1', 174)
        SL.Add('var 2', 159)
        # REMOVE NON EXISTING ---------------------------------
        self.assertRaises(KeyError, SL.Remove, 'var 3')
        self.assertRaises(KeyError, SL.Remove, 'var 4')

    # endregion

    # endregion


if __name__ == '__main__':
    unittest.main()
