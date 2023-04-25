import requests
from PIL import Image
import urllib.request

# Test REST
def testREST (api_url = "https://jsonplaceholder.typicode.com/todos/1"):
    response     = requests.get(api_url)
    jsonResponse = response.json ()
    print (f"get ({api_url}) response = {response.status_code}\n")
    print (jsonResponse, "\n")
    
    # Display if an image URL was returned
    try: 
        imageURL = jsonResponse ["message"]
        # print (imageURL)
        urllib.request.urlretrieve (imageURL, "testImg.jpg")
        imageJpg = Image.open ("testImg.jpg")
        imageJpg.show ()
        
    except:
        print ("Keep moving -- no image here...\n")
        
    return
    
# Main
print ("\n\n—BOJ—\n\n")
testREST ()
testREST ("https://dog.ceo/api/breeds/image/random")
print ("\n\n—EOJ—\n\n")
