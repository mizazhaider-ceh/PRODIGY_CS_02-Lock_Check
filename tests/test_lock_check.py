"""Unit tests for lock_check.py. Run with: python3 -m unittest discover -s tests"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lock_check import evaluate


class TestEvaluate(unittest.TestCase):
    def test_strong(self):
        strength, results = evaluate("Str0ng!Pass")
        self.assertEqual(strength, "strong")
        self.assertTrue(all(passed for _, passed in results))

    def test_weak_too_short(self):
        strength, results = evaluate("Ab1!")
        self.assertEqual(strength, "weak")
        self.assertFalse(results[0][1])  # length check fails

    def test_short_with_all_other_criteria_still_weak(self):
        strength, _ = evaluate("Ab1!cDe")  # 7 chars, has upper/lower/digit/special
        self.assertEqual(strength, "weak")

    def test_medium(self):
        strength, _ = evaluate("password123")  # length + lower + digit = 3
        self.assertEqual(strength, "medium")

    def test_medium_four_criteria(self):
        strength, _ = evaluate("Password1")  # length + upper + lower + digit = 4
        self.assertEqual(strength, "medium")

    def test_weak_two_criteria(self):
        strength, _ = evaluate("password")  # length + lower = 2
        self.assertEqual(strength, "weak")

    def test_empty(self):
        strength, _ = evaluate("")
        self.assertEqual(strength, "weak")

    def test_results_have_five_criteria(self):
        _, results = evaluate("x")
        self.assertEqual(len(results), 5)


if __name__ == "__main__":
    unittest.main()
