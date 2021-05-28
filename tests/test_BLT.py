import blt
import unittest

class TestBlt(unittest.TestCase):

    def test_hcitool_scan(self):
        scan = BLT.hcitool_scan()
        self.assertEqual(len(scan) > 0, True, f"Unexpected number of devices returned {len(scan)}")


if __name__ == '__main__':
    unittest.main()
