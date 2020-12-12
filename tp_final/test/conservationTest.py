import unittest
from tp_final.core import conservation


class MyTestCase(unittest.TestCase):
    def test_calculate_conserved_zone_of_inline_aminoacids_with_length_10_and_3_A(self):
        inline_aminoacids = "AAABBCCDDE"
        expected = ("A", 30)

        res = conservation.calculateConservation(inline_aminoacids)

        self.assertEqual(res, expected)

    def test_calculate_conserved_zone_of_inline_aminoacids_with_length_10_and_1_A_and_the_rest_are_gaps(self):
        inline_aminoacids = "A---------"
        expected = ("A", 10)

        res = conservation.calculateConservation(inline_aminoacids)

        self.assertEqual(res, expected)


    def test_filter_by_conservation_percentage_works_correctly_if_all_pass(self):
        sequence = [("A", 90), ("A", 100), ("A", 85), ("A", 80), ("A", 80), ("A", 80), ("A", 80), ("A", 80), ("A", 80),
                    ("A", 80)]
        porcentage = 80

        res = conservation.filterByConservationPorcentage(porcentage, sequence)

        self.assertEqual(res, "AAAAAAAAAA")

    def test_filter_by_conservation_percentage_works_correctly_with_one_below_porcentage(self):
        sequence = [("A", 80), ("A", 80), ("A", 80), ("A", 80), ("A", 80), ("A", 80), ("A", 80), ("A", 40), ("A", 0),
                    ("A", 79)]
        porcentage = 80

        res = conservation.filterByConservationPorcentage(porcentage, sequence)

        self.assertEqual(res, "AAAAAAA---")


if __name__ == '__main__':
    unittest.main()
