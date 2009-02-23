import unittest

class BufferOverflowTest(unittest.TestCase):
    # Test a buffer overflow found in older versions of PyCrypto

    def setUp(self):
        global ARC2
        from Crypto.Cipher import ARC2

    def runTest(self):
        """ARC2 with keylength > 128"""
        key = "x" * 16384
        mode = ARC2.MODE_ECB
        self.assertRaises(ValueError, ARC2.new, key, mode)

if __name__ == '__main__':
    unittest.main()
