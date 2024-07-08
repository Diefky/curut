import requests
data = ""
with open('initdata.txt', 'r') as file:
    data = file.read()

# decode url
auth = requests.post("https://api.hamsterkombat.io/auth/auth-by-telegram-webapp",
                     json={"initDataRaw": data}).json()['authToken']
print(f"Token : {auth}")
