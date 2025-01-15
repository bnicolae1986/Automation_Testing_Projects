import unittest
from request_apis.books_api import BookApi


class BooksTests(unittest.TestCase):

    accessToken = ""

    # for the backend tests, we only need the setup method, we dont need the teardown method
    def setUp(self):
        self.books = BookApi() # books is an object from the BookApi class
        if self.accessToken == '':
            self.accessToken = self.books.post_api_clients().json()['accessToken'] # we get the value from this key

    # all the test must begin with "test"
    # this test will check the status code and body for /status endpoint
    def test_books_status(self):
        response = self.books.get_api_status_response()
        self.assertEqual(response.status_code, 200, "Status code is not the same:")
        self.assertEqual(response.json()['status'], "OK", "GET /status responce value for key 'status' is not the same: ") # key, value, message

    def tests_all_books(self):
        response = self.books.get_api_books_response()
        self.assertEqual(response.status_code, 200, "Status code is not the same:")
        expected_number = 6
        self.assertEqual(len(response.json()), expected_number, "GET /books length is not the same: ")
        self.assertEqual(response.json()[0]['id'], 1, "Id for the first book si not the same: ")
        # todo , use for book in response.json() and check every fields received!

    def test_book_by_id(self):
        response = self.books.get_api_books_book_by_id(1)
        self.assertEqual(response.status_code, 200, "Status code is not the same: ")
        self.assertEqual(response.json()['name'], "The Russian", "GET /books/{id} response value for key 'name' is not the same:")
        # todo, verify other fields

    def test_book_by_id_negative(self):
        non_existing_id = 100
        response = self.books.get_api_books_book_by_id(non_existing_id)
        self.assertEqual(response.status_code, 404, "Status code is not the same")
        self.assertEqual(response.json()['error'], f"No book with id {non_existing_id}", "GET /books/{id} error message is not the same")

    # no token test
    def test_book_orders_no_token(self):
        response = self.books.get_api_orders_response('213')
        self.assertEqual(response.status_code, 401, "Status code is not the same: ")

    # positive test with token
    def test_all_orders(self):
        response = self.books.get_api_orders_response(self.accessToken)
        self.assertEqual(response.status_code, 200, "Status code is not the same: ")

    def test_post_orders(self):
        book_id = 1
        customer_name = "Bogdan"
        response = self.books.post_books_order(self.accessToken, book_id, customer_name)
        self.assertEqual(response.status_code, 201, "Status code is not the same: ")

    # todo verify if the "created" field is true!

    # flow, placed order, checked status, GET req, i verified that the list contains only one order
    def test_post_orders_flow(self):
        book_id = 1
        customer_name = "Bogdan"
        response = self.books.post_books_order(self.accessToken, book_id, customer_name)
        self.assertEqual(response.status_code, 201, "Status code is not the same: ")

        # now i check that we have 1 order
        response = self.books.get_api_orders_response(self.accessToken)
        self.assertEqual(response.status_code, 200, "Status code is not the same: ")

        expected_number = 1
        self.assertEqual(len(response.json()), expected_number, "GET /orders length is not the same: ")

    def test_patch_order_flow(self):
        book_id = 1
        customer_name = "Bogdan"
        response = self.books.post_books_order(self.accessToken, book_id, customer_name)
        self.assertEqual(response.status_code, 201, "Status code is not the same: ")

        order_id = response.json()['orderId']
        new_customer_name = "Bogdan1"
        response = self.books.patch_books_orders(self.accessToken, order_id, new_customer_name)
        self.assertEqual(response.status_code, 204, "PATCH /orders/{id} Status code is not the same: ")

    # todo a test for get pe order by id "get_order_by_id_route" , id that exists, id that doesnt exist!
    # todo complete flow, create an oder, modify it, req GET then DELETE, then verify that on orders that the status code is 200!

    def test_books_by_filters_only_limit(self):
        limit = 20
        book_type = ''
        response = self.books.get_api_books_by_filters(limit, book_type)

        # Check if the response status code is 200
        self.assertEqual(response.status_code, 200, "Status code is not the same")

        # Check if the response contains the expected number of books
        self.assertTrue(len(response.json()) <= limit, f"The number of books returned should be at most {limit}")

    def test_books_by_filters_wrong_limit(self):
        limit = 21
        book_type = ''
        response = self.books.get_api_books_by_filters(limit, book_type)

        # Check if the response status code is 400
        self.assertEqual(response.status_code, 400, "Status code is not the same")

        # Check if the response contains the expected number of books
        self.assertTrue(len(response.json()) <= limit, f"The number of books returned should be at most {limit}")

    def test_books_by_filters_wrong_limit2(self):
        limit = -1
        book_type = ''
        response = self.books.get_api_books_by_filters(limit, book_type)

        # Check if the response status code is 400
        self.assertEqual(response.status_code, 400, "Status code is not the same")

        # Check if the response contains the expected number of books
        self.assertTrue(len(response.json()) >= 0, "The number of books returned should be at least 0")

    def test_books_by_filters_only_type(self):
        limit = ''
        book_type = "fiction"
        response = self.books.get_api_books_by_filters(limit, book_type)
        self.assertEqual(response.status_code, 200, "Status code is not the same")

        # I extract the JSON content from the response and compare it with book_type = fiction
        books_from_api = response.json()
        for i in range(0, len(books_from_api)):
            book = books_from_api[i]
            self.assertEqual(book["type"], 'fiction', "Type of the book is not the same")

    # test pozitiv limit 20 and type fiction or non-fiction
    def test_books_by_filters(self):
        limit = 20
        book_type = "fiction"
        response = self.books.get_api_books_by_filters(limit, book_type)

        # Check if the response status code is 200
        self.assertEqual(response.status_code, 200, "Status code is not the same")

        # Check if the response contains the expected number of books
        self.assertTrue(len(response.json()) <= limit, f"The number of books returned should be at most {limit}")

        # Check if all books in the response are of type 'fiction'
        books_from_api = response.json()
        for i in range(0, len(books_from_api)):
            book = books_from_api[i]
            self.assertEqual(book["type"], 'fiction', "Type of the book is not the same")


    def test_delete_order_by_order_id(self):
        # Create an order
        book_id = 1
        customer_name = "Bogdan"
        response = self.books.post_books_order(self.accessToken, book_id, customer_name)
        self.assertEqual(response.status_code, 201, "Status code is not the same: ")
        order_id = response.json()['orderId']

        # Delete the created order
        response = self.books.delete_order_by_id(self.accessToken, order_id)
        self.assertEqual(response.status_code, 204, "Status code is not the same: ")

        # Verify the order has been deleted by checking the orders list
        response = self.books.get_api_orders_response(self.accessToken)
        self.assertEqual(response.status_code, 200, "Status code is not the same: ")

        # Check that the deleted order is no longer in the orders list
        orders_list = response.json()
        self.assertFalse(any(i['orderId'] == order_id for i in orders_list),"Deleted order is still present in the orders list")



