import unittest
from tp_final.core import dssp


class MyTestCase(unittest.TestCase):
    def test_calculate_conserved_zone_of_inline_structures_with_length_10_and_3_B(self):
        inline_aminoacids = "BBBHH--DDE"
        expected = ("B", 30)

        res = dssp.calculateConservation(inline_aminoacids)

        self.assertEqual(res, expected)

    def test_calculate_conserved_zone_of_inline_structures_with_length_10_and_1_B_and_the_rest_are_gaps(self):
        inline_aminoacids = "B---------"
        expected = ("B", 10)

        res = dssp.calculateConservation(inline_aminoacids)

        self.assertEqual(res, expected)

    def test_filter_by_conservation_percentage_works_correctly_if_all_pass(self):
        sequence = [("B", 90), ("B", 100), ("B", 85), ("B", 80), ("B", 80), ("B", 80), ("B", 80), ("B", 80), ("B", 80),
                    ("B", 80)]
        porcentage = 80

        res = dssp.filterByConservationPorcentage(porcentage, sequence)

        self.assertEqual(res, "BBBBBBBBBB")

    def test_filter_by_conservation_percentage_works_correctly_with_three_below_porcentage(self):
        sequence = [("B", 80), ("B", 80), ("B", 80), ("B", 80), ("B", 80), ("B", 80), ("B", 80), ("B", 40), ("B", 0),
                    ("B", 79)]
        porcentage = 80

        res = dssp.filterByConservationPorcentage(porcentage, sequence)

        self.assertEqual(res, "BBBBBBB---")


if __name__ == '__main__':
    unittest.main()
