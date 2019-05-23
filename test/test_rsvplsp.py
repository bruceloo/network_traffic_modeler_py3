import unittest

from network_modeling import Node
from network_modeling import RSVP_LSP


class TestRSVPLSP(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        node_a = Node(name='nodeA', lat=0, lon=0)
        node_b = Node(name='nodeB', lat=0, lon=0)
        self.rsvp_lsp = RSVP_LSP(source_node_object=node_a, dest_node_object=node_b, lsp_name='A-to-B')
