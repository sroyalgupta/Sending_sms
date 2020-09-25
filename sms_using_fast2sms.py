import requests

url = "https://www.fast2sms.com/dev/bulk"

number=input('Enter your number :')
message=input('Enter your message :')

querystring = {"authorization":"ZM2aEdmsy3WHNI8xejK6kiJ4hCYrBuwfn9t5QSLpov0VRb7lcP0qHGS5fkgWtPNX2YhFrQy9JnBOZTD6","sender_id":"FSTSMS",
               "message":message,"language":"english","route":"p",
               "numbers":number}

headers = {
    'cache-control': "no-cache"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print("This was successfull")
print(response.text)
