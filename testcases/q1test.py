import unittest
from q1 import Q1

class testQ1(unittest.TestCase):

    def setUp(self):
        pass

    def test_case_1(self):
        Q1()
        f = open("q1_out.txt", "r")
        f1 = open("q1_out_true.txt", "r")
        q1out = [int(line.strip("\n")) for line in f.readlines()]
        q1out_true = [int(line.strip("\n")) for line in f1.readlines()]
        f.close
        f1.close
        self.assertEqual(q1out, q1out_true)

    def test_case_2(self):
        Q1("q1_in(1).txt","1")
        f = open("q1_out1.txt", "r")
        f1 = open("q1_out(1)_true.txt", "r")
        q1out = [int(line.strip("\n")) for line in f.readlines()]
        q1out_true = [int(line.strip("\n")) for line in f1.readlines()]
        f.close
        f1.close
        self.assertEqual(q1out, q1out_true)

    def test_case_3(self):
        Q1("q1_in(2).txt","2")
        f = open("q1_out2.txt", "r")
        f1 = open("q1_out(2)_true.txt", "r")
        q1out = [int(line.strip("\n")) for line in f.readlines()]
        q1out_true = [int(line.strip("\n")) for line in f1.readlines()]
        f.close
        f1.close
        self.assertEqual(q1out, q1out_true)

    def test_case_4(self):
        Q1("q1_in(3).txt","3")
        f = open("q1_out3.txt", "r")
        f1 = open("q1_out(3)_true.txt", "r")
        q1out = [int(line.strip("\n")) for line in f.readlines()]
        q1out_true = [int(line.strip("\n")) for line in f1.readlines()]
        f.close
        f1.close
        self.assertEqual(q1out, q1out_true)

if __name__ == '__main__':
    unittest.main()