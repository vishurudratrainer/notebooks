import doctest
import my_doc
import unittest
 
def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(my_doc))
    return tests
