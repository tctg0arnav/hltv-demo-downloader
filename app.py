import requests as re
import beautifulsoup4 as bs

teamID = input("Enter the team ID: ")
eventID = input("Enter the event ID: ")
mapCode = input("Enter the map code: ")

url = f"https://www.hltv.org/stats/teams/{teamID}/?event={eventID}&maps={mapCode}"

response = re.get(url)
soup = bs(response.text, "html.parser")