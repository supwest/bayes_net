from context import bn


import unittest


class BayesNetTest(unittest.TestCase):

    def test_init_net_has_no_nodes(self):
        net = bn.BayesNet()
        self.assertIsNone(net.nodes)



if __name__ == '__main__':
    unittest.main()



