import unittest
import sample
class TestPrinp(unittest.TestCase):
 def setUp(self):
    p =sample.Person("hhh",23)
    self.p = p

 def test_getName(self):
    self.assertEqual(self.p.getName(self.p),"hhh")

 def test_getAge(self):
    self.assertEqual(self.p.getAge(self.p),23)
    
if __name__ == '__main__':
    unittest.main()
