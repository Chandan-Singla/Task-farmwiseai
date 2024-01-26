import unittest
import requests

class TestBookstoreAPI(unittest.TestCase):
    BASE_URL = 'http://localhost:5000'  # Update with your Flask app URL
    AUTH = ('admin', 'password')  # Basic Auth credentials

    def test_1_get_books(self):
        response = requests.get(f'{self.BASE_URL}/books', auth=self.AUTH)
        self.assertEqual(response.status_code, 200)
        # Add assertions to verify the response data

    def test_2_add_book(self):
        book_data = {
            'title': 'Test Book',
            'author': 'Test Author',
            'isbn': '1234567890123',
            'price': 9.99,
            'quantity': 10
        }
        response = requests.post(f'{self.BASE_URL}/books', json=book_data, auth=self.AUTH)
        self.assertEqual(response.status_code, 201)
        # Add assertions to verify the response data

    def test_3_get_book(self):
        isbn = '1234567890123'  # Use the ISBN of a book that exists in the database
        response = requests.get(f'{self.BASE_URL}/books/{isbn}', auth=self.AUTH)
        self.assertEqual(response.status_code, 200)
        # Add assertions to verify the response data

    def test_4_update_book(self):
        isbn = '1234567890123'  # Use the ISBN of a book that exists in the database
        update_data = {
            'title': 'Updated Book Title',
            'price': 12.99
        }
        response = requests.put(f'{self.BASE_URL}/books/{isbn}', json=update_data, auth=self.AUTH)
        self.assertEqual(response.status_code, 200)
        # Add assertions to verify the response data

    def test_5_delete_book(self):
        isbn = '1234567890123'  # Use the ISBN of a book that exists in the database
        response = requests.delete(f'{self.BASE_URL}/books/{isbn}', auth=self.AUTH)
        self.assertEqual(response.status_code, 200)
        # Add assertions to verify the response data

if __name__ == '__main__':
    unittest.main()
