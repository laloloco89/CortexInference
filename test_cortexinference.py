# test_cortexinference.py
"""
Tests for CortexInference module.
"""

import unittest
from cortexinference import CortexInference

class TestCortexInference(unittest.TestCase):
    """Test cases for CortexInference class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CortexInference()
        self.assertIsInstance(instance, CortexInference)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CortexInference()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
