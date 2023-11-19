import unittest
from unittest import TestCase
from q3 import move

class MoveTestSuite(TestCase):

    def test_move_right(self):
        state = (
            "#####   ",
            "###    #",
            "#   o ##",
            "   #####"
        )
        actual = move(state, "right")
        expected = (
            (
                "#####   ",
                "###    #",
                "#    o##",
                "   #####"
            ),
            ("left", "up")
        )

        self.assertEqual(expected, actual)

    def test_move_up(self):

        state = (
            "#####   ",
            "###    #",
            "#   o ##",
            "   #####"
        )
        actual = move(state, "up")
        expected = (
            (
                "#####   ",
                "### o  #",
                "#     ##",
                "   #####"
            ),
            ("down", "left", "right")
        )

        self.assertEqual(expected, actual)

    # Test move out of boundaries
    def test_move_out_of_boundaries(self):
        state = (
            "#####   ",
            "###    o",
            "#     ##",
            "   #####"
        )
        with self.assertRaises(Warning):
            move(state, "right")

    # Test only player
    def test_only_player(self):

        state = (
            "        ",
            "        ",
            "    o   ",
            "        "
        )
        actual = move(state, "up")
        expected = (
            (
                "        ",
                "    o   ",
                "        ",
                "        "
            ),
            ("down", "left", "right", 'up')
        )

        self.assertEqual(expected, actual)
    
    # Invalid move
    def test_move_down(self):

        state = (
            "#####   ",
            "###    #",
            "#   o ##",
            "   #####"
        )

        with self.assertRaises(Warning):
            move(state, "down")

    # Test invalid characters
    def test_invalid_characters(self):

        state = (
            "#####   ",
            "###    #",
            "#z  o ##",
            "   #####"
        )

        with self.assertRaises(Warning):
            move(state, "down")

    # Test invalid characters 2
    def test_invalid_characters_2(self):

        state = (
            "#####   ",
            "###$   #",
            "#   o ##",
            "   #####"
        )

        with self.assertRaises(Warning):
            move(state, "right")

    # Test invalid characters 3
    def test_invalid_characters_3(self):

        state = (
            "#####   ",
            "#x#    #",
            "#   o ##",
            "   #####"
        )

        with self.assertRaises(Warning):
            move(state, "right")

    # Test invalid characters 4
    def test_invalid_characters_4(self):

        state = (
            "        ",
            "        ",
            "        ",
            "        "
        )

        with self.assertRaises(Warning):
            move(state, "right")

    # Test invalid characters 5
    def test_invalid_characters_5(self):

        state = (
            "",
            "",
            "",
            ""
        )

        with self.assertRaises(Warning):
            move(state, "right")

    # Test inconsistent map
    def test_inconsistent_map(self):

        state = (
            "#####  ",
            "###    #",
            "#   o ##",
            "   #####"
        )

        with self.assertRaises(Warning):
            move(state, "right")

    # Test invalid moves
    def test_invalid_moves(self):

        state = (
            "#####   ",
            "### #  #",
            "#  #o###",
            "   #####"
        )

        with self.assertRaises(Warning):
            move(state, "down")

    # Test no player
    def test_no_player(self):
        state = (
            "#####   ",
            "###    #",
            "#       ",
            "   #####"
        )
        with self.assertRaises(Warning):
            move(state, "right")

    # Test more players
    def test_more_players(self):
        state = (
            "#####   ",
            "###  o #",
            "#   o   ",
            "   #####"
        )
        with self.assertRaises(Warning):
            move(state, "right")

    # Test empty grid
    def test_empty_grid(self):
        state = ()
        with self.assertRaises(Warning):
            move(state, "up")

if __name__ == "__main__":
    test_suite = unittest.TestLoader().loadTestsFromTestCase(MoveTestSuite)
    unittest.TextTestRunner(verbosity=2).run(test_suite)