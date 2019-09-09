from django.test import TestCase

# Create your tests here.
class SmokeTest(TestCase):
    """description"""

    def test_bad_math(self):
        self.assertEqual(1 + 1, 3)
        
