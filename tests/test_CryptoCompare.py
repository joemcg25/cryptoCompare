import unittest
from src.api import CryptoCompare

class TestCryptoCompare(unittest.TestCase):
    def setUp(self) -> None: # Called before every test
        self.apiCrypto = CryptoCompare.CryptoCompare()
    def tearDown(self) -> None: # Called after every test
        pass
    def test_createArgs(self):
        res=self.apiCrypto.createArgs({"a":12,"b":"testArg","c":["testArg1","testArg2"]})
        self.assertEqual("a=12&b=testArg&c=testArg1,testArg2",res)
    def test_parseArgs(self):
        res=self.apiCrypto.parseArgs(["EUR","RUB"])
        self.assertEqual("EUR,RUB",res)
    def test_parseArgsSingle(self):
        res=self.apiCrypto.parseArgs(["RUB"])
        self.assertEqual("RUB",res)
    def test_parseArgsSingle1(self):
        res=self.apiCrypto.parseArgs("RUB")
        self.assertEqual("RUB",res)