import unittest
from age import *
from tag_parse import *

class TestAge(unittest.TestCase):

    def test_age_less_than_150(self):
        people, families = read_file('./sprint1/jt_sprint1.ged')
        people = store_ages(families, people)
        self.assertEqual(less_than_one_fifty('@I1@', people), 'Death Age Invalid')

if __name__ == '__main__':
    unittest.main()