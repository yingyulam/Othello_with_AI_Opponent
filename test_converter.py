import unittest
from converter import Converter

class TestBoard(unittest.TestCase):

    def test_converter_basic(self):
        converter = Converter(4)
        self.assertEqual(converter.name, "Converter")
        self.assertEqual(converter.board_size, 4)

    def test_converter_not_integer(self):
        with self.assertRaises(TypeError):
            converter = Converter("four")

    def test_converter_negative(self):
        with self.assertRaises(ValueError):
            converter = Converter(-1)
    
    def test_converter_too_big(self):
        with self.assertRaises(ValueError):
            converter = Converter(5)

    def test_get_cell_coordinates(self):
        converter = Converter(4)
        self.assertEqual(converter.get_cell_coordinates(1,2), (25.0, 25.0))

    def test_get_cell_coordinates_row_not_integer(self):
        with self.assertRaises(TypeError):
            converter = Converter(4)
            converter.get_cell_coordinates(1.1, 0)

    def test_get_cell_coordinates_row_negative(self):
        with self.assertRaises(ValueError):
            converter = Converter(4)
            converter.get_cell_coordinates(-1, 0)

    def test_get_cell_coordinates_row_too_big(self):
        with self.assertRaises(ValueError):
            converter = Converter(4)
            converter.get_cell_coordinates(4, 0)

    def test_get_cell_coordinates_column_not_integer(self):
        with self.assertRaises(TypeError):
            converter = Converter(4)
            converter.get_cell_coordinates(1, "one")

    def test_get_cell_coordinates_column_negative(self):
        with self.assertRaises(ValueError):
            converter = Converter(4)
            converter.get_cell_coordinates(1, -1)

    def test_get_cell_coordinates_column_too_big(self):
        with self.assertRaises(ValueError):
            converter = Converter(4)
            converter.get_cell_coordinates(1, 4)
    
    def test_convert_coordinates_to_index_basic(self):
        converter = Converter(4)
        self.assertEqual(converter.convert_coordinates_to_index(25.0, 25.0), (1, 2))

    def test_convert_coordinates_to_index_not_number(self):
        with self.assertRaises(TypeError):
            converter = Converter(4)
            converter.convert_coordinates_to_index("one", "two")

    def test_printing(self):
        converter = Converter(4)
        self.assertEqual(str(converter), "converter for 4 x 4 board")

    def test_equality_true(self):
        converter = Converter(4)
        other = Converter(4)
        self.assertEqual(converter, other)

    def test_equality_false(self):
        converter = Converter(4)
        other = Converter(6)
        self.assertNotEqual(converter, other)

    def test_equality_error(self):
        with self.assertRaises(TypeError):
            converter = Converter(4)
            converter == "Converter"

def main():

    unittest.main(verbosity = 3)

if __name__ == "__main__":
    main()