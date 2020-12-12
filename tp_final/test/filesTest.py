import unittest
import os
from tp_final.core import pdb


class MyTestCase(unittest.TestCase):
    def test_when_fetching_from_pdb_in_pdb_format_it_downloads_the_correct_file(self):
        pdb.fetchInPDBFormat("7B1G")
        exist = os.path.exists(pdb.getRepositoryPath() + "/7B1G.pdb")

        self.assertEqual(exist, True)


if __name__ == '__main__':
    unittest.main()
