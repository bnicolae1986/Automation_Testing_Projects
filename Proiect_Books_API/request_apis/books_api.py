import requests
import random
class BookApi():

    # constante
    # daca vreau ca aceste constante sa fie protected, adaug la inceput _ iar pentru private __
    BASE_URL = "https://simple-books-api.glitch.me"
    STATUS_ENDPOINT = "/status"
    BOOKS_ENDPOINT = "/books"
    ORDERS_ENDPOINT = "/orders"
    API_CLIENTS_ENDPOINT = "/api-clients"

    # cu aceasta metoda obtinem ruta pentru primul endpoint, cel pt /status
    def get_status_route(self):
        return self.BASE_URL + self.STATUS_ENDPOINT

    # cu aceasta metoda obtinem ruta pentru al doilea endpoint, cel pt /books
    def get_books_route(self):
        return self.BASE_URL + self.BOOKS_ENDPOINT

    def get_book_by_id_route(self, book_id):
        return self.get_books_route() + f'/{book_id}'

    # cu aceasta metoda obtinem ruta pentru al treilea endpoint, cel pt /orders
    def get_orders_route(self):
        return self.BASE_URL + self.ORDERS_ENDPOINT

    def get_order_by_id_route(self, order_id):
        return self.get_orders_route() + f'/{order_id}'
    def get_api_clients_route(self):
        return self.BASE_URL + self.API_CLIENTS_ENDPOINT

    # cu aceasta metoda ne folosim de libraria requests, pentru a face requestul de GET pt /status
    def get_api_status_response(self):
        URL = self.get_status_route()
        return requests.get(url=URL)

    # cu aceasta metoda ne folosim de libraria requests, pentru a face requestul de GET pt /books
    # avem nevoie de url si de requestul de GET
    def get_api_books_response(self):
        URL = self.get_books_route()
        return requests.get(url=URL)

    def get_api_books_book_by_id(self, book_id):
        URL = self.get_book_by_id_route(book_id)
        return  requests.get(url=URL)

    def get_api_books_by_filters(self, limit, book_type):
        URL = self.get_books_route()

        if limit =='':
            query_params = {
                "type": book_type
            }
        elif book_type =='':
            query_params = {
                "limit": limit
            }
        else:
            query_params = {
                "limit": limit,
                "type": book_type
            }
        # query_params = {
        #     "limit": limit,
        #     "type": book_type
        # }
        return requests.get(url=URL, params=query_params)

    def get_api_orders_response(self,access_token):
        URL = self.get_orders_route()
        headers = {
            'Authorization': f'Bearer {access_token}'
        }
        return requests.get(url=URL, headers=headers)

    def post_api_clients(self):
        URL = self.get_api_clients_route()
        random_number  = random.randint(1, 9999999999)
        body = {
            "clientName": "Bogdan",
            "clientEmail": f"bogdan_api{random_number}@api.com"
        }
        return requests.post(url=URL, json=body)


    def post_books_order(self, access_token, book_id, customer_name):
        URL = self.get_orders_route()
        headers = {
            'Authorization': f'Bearer {access_token}'
        }
        body = {
            "bookId": book_id,
            "costomerName": customer_name
        }
        return requests.post(url=URL, json=body, headers=headers)

    def patch_books_orders(self, access_token, order_id, customer_name):
        URL = self.get_order_by_id_route(order_id)
        headers = {
            'Authorization': f'Bearer {access_token}'
        }
        body = {
            "customerName": customer_name
        }
        return requests.patch(url=URL, json=body, headers=headers)

    def delete_order_by_id(self, access_token, order_id):
        URL = self.get_order_by_id_route(order_id)
        headers = {
            'Authorization': f'Bearer {access_token}'
        }
        return requests.delete(url=URL, headers=headers)

