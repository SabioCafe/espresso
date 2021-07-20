"""Tests class model."""
import unittest

from app.core.databases import MySqlDriver
from app.main import create_app

app = create_app()


class TestRoutes(unittest.TestCase):
    """TestRoutes unittest class."""

    def setUp(self):
        """Test Case configuration."""
        self.database = MySqlDriver()
        self.client = app.test_client()

    def testMainRouteSucess(self):
        """Tests if the endpoint has returned success."""
        response = self.client.get("/main")
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        """Function to be executed at the end of the test's execution."""
        pass
