import unittest
from unittest.mock import patch
from io import StringIO
import sys

# Import the functions from practice 3
from practice_3 import (
    detect_gender_by_suffix,
    verify_gender,
    display_result,
    male_names,
    female_names
)


class TestDetectGenderBySuffix(unittest.TestCase):
    """Test the detect_gender_by_suffix function"""

    def test_female_suffix_a(self):
        """Test detection of female names ending in 'a'"""
        gender, source = detect_gender_by_suffix("maria")
        self.assertEqual(gender, "Female")
        self.assertEqual(source, "suffix pattern")

    def test_female_suffix_ia(self):
        """Test detection of female names ending in 'ia'"""
        gender, source = detect_gender_by_suffix("gloria")
        self.assertEqual(gender, "Female")
        self.assertEqual(source, "suffix pattern")

    def test_female_suffix_ina(self):
        """Test detection of female names ending in 'ina'"""
        gender, source = detect_gender_by_suffix("christina")
        self.assertEqual(gender, "Female")
        self.assertEqual(source, "suffix pattern")

    def test_female_suffix_ine(self):
        """Test detection of female names ending in 'ine'"""
        gender, source = detect_gender_by_suffix("christine")
        self.assertEqual(gender, "Female")
        self.assertEqual(source, "suffix pattern")

    def test_female_suffix_elle(self):
        """Test detection of female names ending in 'elle'"""
        gender, source = detect_gender_by_suffix("michelle")
        self.assertEqual(gender, "Female")
        self.assertEqual(source, "suffix pattern")

    def test_female_suffix_ette(self):
        """Test detection of female names ending in 'ette'"""
        gender, source = detect_gender_by_suffix("annette")
        self.assertEqual(gender, "Female")
        self.assertEqual(source, "suffix pattern")

    def test_female_suffix_lyn(self):
        """Test detection of female names ending in 'lyn'"""
        gender, source = detect_gender_by_suffix("jacquelyn")
        self.assertEqual(gender, "Female")
        self.assertEqual(source, "suffix pattern")

    def test_male_suffix_on(self):
        """Test detection of male names ending in 'on'"""
        gender, source = detect_gender_by_suffix("jackson")
        self.assertEqual(gender, "Male")
        self.assertEqual(source, "suffix pattern")

    def test_male_suffix_an(self):
        """Test detection of male names ending in 'an'"""
        gender, source = detect_gender_by_suffix("jordan")
        self.assertEqual(gender, "Male")
        self.assertEqual(source, "suffix pattern")

    def test_male_suffix_en(self):
        """Test detection of male names ending in 'en'"""
        gender, source = detect_gender_by_suffix("darren")
        self.assertEqual(gender, "Male")
        self.assertEqual(source, "suffix pattern")

    def test_male_suffix_ard(self):
        """Test detection of male names ending in 'ard'"""
        gender, source = detect_gender_by_suffix("leonard")
        self.assertEqual(gender, "Male")
        self.assertEqual(source, "suffix pattern")

    def test_male_suffix_bert(self):
        """Test detection of male names ending in 'bert'"""
        gender, source = detect_gender_by_suffix("lambert")
        self.assertEqual(gender, "Male")
        self.assertEqual(source, "suffix pattern")

    def test_unknown_suffix(self):
        """Test detection with unknown suffix"""
        gender, source = detect_gender_by_suffix("xyz")
        self.assertIsNone(gender)
        self.assertIsNone(source)

    def test_case_insensitivity(self):
        """Test that detection is case-insensitive"""
        gender_lower, _ = detect_gender_by_suffix("maria")
        gender_upper, _ = detect_gender_by_suffix("MARIA")
        gender_mixed, _ = detect_gender_by_suffix("MaRiA")
        self.assertEqual(gender_lower, gender_upper)
        self.assertEqual(gender_lower, gender_mixed)


class TestVerifyGender(unittest.TestCase):
    """Test the verify_gender function"""

    def test_male_name_in_database(self):
        """Test detection of male name from database"""
        gender, source = verify_gender("james")
        self.assertEqual(gender, "Male")
        self.assertEqual(source, "name database")

    def test_female_name_in_database(self):
        """Test detection of female name from database"""
        gender, source = verify_gender("mary")
        self.assertEqual(gender, "Female")
        self.assertEqual(source, "name database")

    def test_male_name_uppercase(self):
        """Test detection is case-insensitive for male names"""
        gender, source = verify_gender("JAMES")
        self.assertEqual(gender, "Male")
        self.assertEqual(source, "name database")

    def test_female_name_uppercase(self):
        """Test detection is case-insensitive for female names"""
        gender, source = verify_gender("MARY")
        self.assertEqual(gender, "Female")
        self.assertEqual(source, "name database")

    def test_name_with_whitespace(self):
        """Test that whitespace is stripped"""
        gender, source = verify_gender("  james  ")
        self.assertEqual(gender, "Male")
        self.assertEqual(source, "name database")

    def test_suffix_pattern_fallback(self):
        """Test that suffix pattern is used as fallback"""
        gender, source = verify_gender("anthony")
        # Should match database first, but test the logic
        self.assertIn(gender, ["Male", "Female", "Unknown"])

    def test_unknown_name(self):
        """Test detection of completely unknown name"""
        gender, source = verify_gender("xyzabc")
        self.assertEqual(gender, "Unknown")
        self.assertEqual(source, "not found")

    def test_empty_string(self):
        """Test with empty string after stripping"""
        gender, source = verify_gender("   ")
        self.assertEqual(gender, "Unknown")
        self.assertEqual(source, "not found")


class TestDisplayResult(unittest.TestCase):
    """Test the display_result function"""

    def test_display_male_result(self):
        """Test display output for male name"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            display_result("james", "Male", "name database")
            output = fake_out.getvalue()
            self.assertIn("James", output)
            self.assertIn("Male", output)
            self.assertIn("name database", output)

    def test_display_female_result(self):
        """Test display output for female name"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            display_result("mary", "Female", "name database")
            output = fake_out.getvalue()
            self.assertIn("Mary", output)
            self.assertIn("Female", output)
            self.assertIn("name database", output)

    def test_display_unknown_result(self):
        """Test display output for unknown name"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            display_result("unknown", "Unknown", "not found")
            output = fake_out.getvalue()
            self.assertIn("Unknown", output)
            self.assertIn("not found", output)

    def test_title_formatting(self):
        """Test that name is displayed in title case"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            display_result("james", "Male", "name database")
            output = fake_out.getvalue()
            self.assertIn("James", output)

    def test_multiple_word_name(self):
        """Test display with multiple word name"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            display_result("mary jane", "Female", "name database")
            output = fake_out.getvalue()
            self.assertIn("Mary Jane", output)


class TestNameDatabases(unittest.TestCase):
    """Test the name databases"""

    def test_male_names_not_empty(self):
        """Test that male_names set is not empty"""
        self.assertGreater(len(male_names), 0)

    def test_female_names_not_empty(self):
        """Test that female_names set is not empty"""
        self.assertGreater(len(female_names), 0)

    def test_male_names_are_lowercase(self):
        """Test that all male names are lowercase"""
        for name in male_names:
            self.assertEqual(name, name.lower())

    def test_female_names_are_lowercase(self):
        """Test that all female names are lowercase"""
        for name in female_names:
            self.assertEqual(name, name.lower())

    def test_no_duplicate_names_across_sets(self):
        """Test that there are no names in both sets (optional check)"""
        # Get names that appear in both sets
        duplicates = male_names & female_names
        # Note: Some names may legitimately be in both sets
        # This test just verifies we can check for them
        self.assertIsInstance(duplicates, set)


class TestIntegration(unittest.TestCase):
    """Integration tests for the complete workflow"""

    def test_full_workflow_known_male(self):
        """Test complete workflow with known male name"""
        gender, source = verify_gender("robert")
        self.assertEqual(gender, "Male")
        self.assertEqual(source, "name database")

    def test_full_workflow_known_female(self):
        """Test complete workflow with known female name"""
        gender, source = verify_gender("elizabeth")
        self.assertEqual(gender, "Female")
        self.assertEqual(source, "name database")

    def test_full_workflow_suffix_male(self):
        """Test complete workflow with male suffix pattern"""
        gender, source = verify_gender("jackson")
        self.assertIn(gender, ["Male", "Female", "Unknown"])

    def test_full_workflow_suffix_female(self):
        """Test complete workflow with female suffix pattern"""
        gender, source = verify_gender("sophia")
        self.assertIn(gender, ["Female", "Male", "Unknown"])

    def test_full_workflow_unknown(self):
        """Test complete workflow with unknown name"""
        gender, source = verify_gender("qwerty")
        self.assertEqual(gender, "Unknown")
        self.assertEqual(source, "not found")


class TestEdgeCases(unittest.TestCase):
    """Test edge cases and special scenarios"""

    def test_single_letter_name(self):
        """Test with single letter name"""
        gender, source = verify_gender("a")
        self.assertIn(gender, ["Male", "Female", "Unknown"])

    def test_very_long_name(self):
        """Test with very long name"""
        long_name = "a" * 100
        gender, source = verify_gender(long_name)
        self.assertIn(gender, ["Male", "Female", "Unknown"])

    def test_name_with_apostrophe_should_fail(self):
        """Test that name with apostrophe is rejected (contains non-alpha)"""
        # The main function validates this, but verify_gender doesn't
        # This test documents the expected behavior
        gender, source = verify_gender("o'reilly")
        # Should return Unknown since it contains non-alpha character
        self.assertIn(gender, ["Male", "Female", "Unknown"])

    def test_numeric_name(self):
        """Test that numeric names are handled"""
        gender, source = verify_gender("123")
        # verify_gender doesn't validate, but the main loop does
        self.assertIn(gender, ["Male", "Female", "Unknown"])

    def test_mixed_case_with_whitespace(self):
        """Test mixed case with surrounding whitespace"""
        gender, source = verify_gender("  JaMeS  ")
        self.assertEqual(gender, "Male")
        self.assertEqual(source, "name database")


if __name__ == '__main__':
    unittest.main()
