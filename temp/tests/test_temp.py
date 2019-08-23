"""
Unit and regression test for the temp package.
"""

# Import package, test suite, and other packages as needed
import temp
import pytest
import sys

def test_temp_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "temp" in sys.modules
