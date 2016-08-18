from context import bn
import numpy as np


import unittest



class BayesNetTest(unittest.TestCase):

    def test_ancestor_node_has_no_parents(self):
        pass
        

    def test_net_is_empty_to_start(self):
        net = bn.BayesNet()
        self.assertIsNone(net.nodes)
    
    def test_node_has_table(self):
        table = np.array({'a':.5, "na": .5})
        state = "a"
        node = bn.Node(table, state)
        self.assertIsNotNone(node.table)
        self.assertIsNotNone(node.state)
        


if __name__ == '__main__':
    unittest.main()



