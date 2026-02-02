# test_dappscribble.py
"""
Tests for DappScribble module.
"""

import unittest
from dappscribble import DappScribble

class TestDappScribble(unittest.TestCase):
    """Test cases for DappScribble class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DappScribble()
        self.assertIsInstance(instance, DappScribble)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DappScribble()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
