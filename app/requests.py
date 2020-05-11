from app import app
import urllib.request,json
from app.models import Quote

Quote = quote.Quote
# Getting the movie base url
base_url = app.config["QUOTE_API_BASE_URL"]

def get_quote(category):
    '''
    Function that gets the json response to our url request
    '''
    get_quote_url = base_url

    with urllib.request.urlopen(get_quote_url) as url:
        get_quote_data = url.read()
        get_quote_response = json.loads(get_quote_data)

        quote_results = None

        if get_quote_response['results']:
            quote_results_list = get_quote_response['results']
            quote_results = process_results(quote_results_list)


    return quote_results

def process_results(movie_list):
    '''
    Function  that processes the quote result and transform them to a list of Objects

    Args:
        quote_list: A list of dictionaries that contain quote details

    Returns :
        quote_results: A list of quotes objects
    '''
    quote_results = []
    for quote_item in quote_list:
        id = quote_item.get('id')
        author = quote_item.get('author')
        quote = quote_item.get('quote')
        permalink = quote_item.get('permalink')
        
        if quote:
            quote_object = Quote(id,auther,permalink)
            quote_results.append(quote_object)

    return quote_results