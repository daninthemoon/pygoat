from django.test import TestCase

# Create your tests here.
class HomePageTest(TestCase):
    """Test home page view"""

    def test_uses_home_template(self):
        """
        Test to make sure template is served
        """
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
