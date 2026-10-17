"""Regression checks for the public, intentionally non-AI FAQ example."""
import unittest
from faq_demo import answer


class FAQDemoTests(unittest.TestCase):
    def test_report(self):
        result=answer("Tell me about automated weekly reports")
        self.assertIsNotNone(result["matched_question"])
        self.assertIn("KPI",result["answer"])
    def test_unknown_is_explicit(self):
        result=answer("What is the meaning of Jupiter")
        self.assertIsNone(result["matched_question"])
    def test_privacy_warning(self):
        result=answer("handling customer API keys")
        self.assertIn("should not be sent",result["answer"])
    def test_oversize(self):
        self.assertIsNone(answer("A"*900)["matched_question"])


if __name__ == "__main__":
    unittest.main()
