# Set up the url and send a GET request to it. The base url is:
import requests
import json
paramters = {}
get_request = requests.get("https://api.nasa.gov/planetary/apod?api_key=Xi5EuakFsi9PbNLqqyGjACec9OXz90feQ0z323x9&date=1998-01-29")
get_request = json.loads(get_request.text)
image_url = get_request["url"]
print(image_url)

# Make the request and print out the "url" key in the response, which is the image url
