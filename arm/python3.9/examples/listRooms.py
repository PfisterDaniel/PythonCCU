#!/usr/bin/env python
import requests, json

url = 'http://localhost/api/homematic.cgi'
loginJson = { "method":"Session.login", "params":{"username":"Admin", "password":"xxx"}}
Response = json.loads(requests.post(url, json = loginJson).text)
SessionID = Response["result"]
print("Your SessionID is: " + SessionID)
getRoomsJson = { "method":"Room.getAll", "params":{"_session_id_":SessionID}}
Response = json.loads(requests.post(url, json = getRoomsJson).text)
print("Your defined Rooms:")
for room in Response['result']:
    print (room['id'] + ": " + room['name'])

print("Logout, please wait...")
logoutJson =  {"method":"Session.logout", "params":{"_session_id_":SessionID}}
Response = json.loads(requests.post(url, json = logoutJson).text)

if Response["result"]:
    print("Successfully logout.")

