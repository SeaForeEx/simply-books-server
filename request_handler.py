import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from views import get_single_author, get_all_authors, get_single_book, get_all_books

class HandleRequests(BaseHTTPRequestHandler):
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """
    
    def parse_url(self, path):
        """Parse the url into the resource and id
        """
        parsed_url = urlparse(path)
        path_params = parsed_url.path.split('/')  # ['', 'animals', 1]
        resource = path_params[1]

        if parsed_url.query:
            query = parse_qs(parsed_url.query)
            return (resource, query)

        pk = None
        try:
            pk = int(path_params[2])
        except (IndexError, ValueError):
            pass
        return (resource, pk)
    
    def _set_headers(self, status):
        # self - current instance of the class
        # status - HTTP status code to be sent back to client
        """Sets the status code, Content-Type and Access-Control-Allow-Origin headers on the response

        Args: status (number): the status code to return to the front end
        """
        # This method is used to set the headers of an HTTP response that will be sent back to the client
        
        # Set the HTTP response status code to status
        self.send_response(status)

        # Send an extra response, required by some browsers
        self.send_response(status)

        # Set the Content-Type header to indicate that the response will be in JSON format
        self.send_header('Content-type', 'application/json')

        # Set the Access-Control-Allow-Origin header to allow cross-origin resource sharing (CORS)
        self.send_header('Access-Control-Allow-Origin', '*')

        # End the response headers, the response body will follow
        self.end_headers()
    
    # Another method! This supports requests with the OPTIONS verb.
    def do_OPTIONS(self):
        """Sets the options headers
        """
        # HTTP OPTIONS requests are used by the browser to check what HTTP methods and headers are allowed for a given resource
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type, Accept')
        self.end_headers() # response body will follow

    def do_GET(self):
        """Handles any GET request
        """
        self._set_headers(200)
        response = {} # default response
        
        # parse URL and store entire tuple in a variable
        parsed = self.parse_url(self.path)
        
        # if path doesn't have a query it stays with original if block
        if '?' not in self.path:
            ( resource, id ) = parsed
            
            if resource == "authors":
                if id is not None:
                    response = get_single_author(id)
                    
                else: 
                    response = get_all_authors()
            
            if resource == "books":
                if id is not None:
                    response = get_single_book(id)
                
                else:
                    response = get_all_books()
                    
        else: # there is a ? in the path, run query param funcs
            (resource, query) = parsed
            
        self.wfile.write(json.dumps(response).encode())
            
      
# This function is not inside the class. It is the starting
# point of this application.
def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
