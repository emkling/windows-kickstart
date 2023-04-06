import unittest
import main

class TestMain(unittest.TestCase):

    def test_get_notepad_window_handle(self):
        hwnd = main.get_notepad_window_handle()
        self.assertIsNotNone(hwnd, "Notepad window handle should not be None")
    
    def test_get_window_position_and_size(self):
        hwnd = main.get_notepad_window_handle()
        self.assertIsNotNone(hwnd, "Notepad window handle should not be None")
        
        left, top, width, height = main.get_window_position_and_size(hwnd)
        self.assertIsNotNone(left, "Left should not be None")
        self.assertIsNotNone(top, "Top should not be None")
        self.assertIsNotNone(width, "Width should not be None")
        self.assertIsNotNone(height, "Height should not be None")

if __name__ == "__main__":
    unittest.main()