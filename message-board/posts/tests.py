from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse
from .models import Post


class PostTests(TestCase):
    # ALL methods should start with the phrase "test_" so tha Django knows to test them!
    # This part checks to see if the post a user makes is equal to what is stored in the database
    @classmethod
    # "setUptTestData()" is used to create the "test data"
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="This is a test!")

    def test_model_content(self):
        self.assertEqual(self.post.text, "This is a test!")

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    # This function combines all the other three (bottom) functions in the quotations together using one response since all three  tests are really just testing that the homepage works as expected.
    def test_homepage(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "This is a test!")

    """
    def test_urls_avaialbe_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")

    def test_template_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "This is a test!")
    """

    # This function combines all the other three functions in the quottions together using one response
    def test_homepage(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "This is a test!")
