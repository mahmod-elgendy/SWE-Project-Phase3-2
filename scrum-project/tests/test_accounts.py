from django.test import TestCase
from firebase_config.firebase_helpers import get_data, set_data, delete_data
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class UserProfileTests(TestCase):
    def setUp(self):
        """
        Set up the test case by adding data to Firebase that will be used across test methods.
        """
        self.test_user = {
            "UserName": "TestUser",
            "UserEmail": "testuser@example.com",
            "UserBio": "Testing Bio"
        }

        # Insert test data into Firebase
        set_data("User/TestUser1", self.test_user)

    def test_get_user_profile(self):
        """
        Test that the user profile data can be retrieved from Firebase correctly.
        """
        # Retrieve the data from Firebase
        response = get_data("User/TestUser1")

        # Assert that the data matches
        self.assertEqual(response["UserName"], "TestUser")
        self.assertEqual(response["UserEmail"], "testuser@example.com")
        self.assertEqual(response["UserBio"], "Testing Bio")

    def tearDown(self):
        """
        Clean up after each test by deleting the test user from Firebase.
        """
        delete_data("User/TestUser1")
