import json
import urllib.parse
import urllib.request

#api key: AWeLhVHRZwow7As8WpQ48fuCT9IDwJOk
class MapQuest:
	#constructor
	def __init__(self, api):
		self._apiKey = api
		self._baseURL = "http://open.mapquestapi.com/directions/v2/route?"

	#base url builder
	def buildURLDirections(self, loc1, loc2):
		query_parameters = [ ('key', self._apiKey), ('from', loc1), ('to', loc2)]
		return self._baseURL + urllib.parse.urlencode(query_parameters)

	#json results
	def getResult(self, url):
		response = None
		try:
			response = urllib.request.urlopen(url)
			return json.load(response)
		finally:
			if response != None:
				response.close()

	#total distance from each location to the other
	def totalDistance(self, locations:list)->float:
		dist = 0.0
		if len(locations) < 2:
			dist = 0
		else:
			i = 0
			while i < (len(locations)-1):
				u = self.buildURLDirections(locations[i], locations[i+1])
				r = self.getResult(u)
				dist = dist + r["route"]["distance"]
				i = i + 1
		return dist

	#total time from each location to the other
	def totalTime(self, locations:list)->int:
		time = 0
		if len(locations) < 2:
			time = 0
		else:
			i = 0
			while i < (len(locations)-1):
				u = self.buildURLDirections(locations[i], locations[i+1])
				r = self.getResult(u)
				time = time + r["route"]["time"]
				i = i + 1
		return time

	#directions from each location to the other
	def directions(self, locations:list)->str:
		dir = ""
		if len(locations) < 2:
			dir = ""
		else:
			i = 0
			while i < (len(locations)-1):
				u = self.buildURLDirections(locations[i], locations[i+1])
				r = self.getResult(u)
				numM = r["route"]["legs"][0]["maneuvers"]
				for j in numM:
					n = j["narrative"]
					if n.find("Welcome") != -1:
						n.replace("Welcome to ", "", 1)
					dir = dir + n + "\n"
				i = i + 1
		return dir

	#finds points of interest ie. gas stations around location
	def pointOfInterest(self, locations: str, keyword: str, results:int)->list:
		#find lat/long data
		url1 = "http://www.mapquestapi.com/geocoding/v1/address?"
		query_parameters_one = [ ('key', self._apiKey), ('location', locations)]
		url1 = url1 + urllib.parse.urlencode(query_parameters_one)
		r1 = self.getResult(url1)
		lat = r1["results"][0]["locations"][0]["latLng"]["lat"]
		lng = r1["results"][0]["locations"][0]["latLng"]["lng"]
		lnglat = str(lng) + ", " + str(lat)

		#place search url
		url2 = "https://www.mapquestapi.com/search/v4/place?"
		query_parameters_two = [ ('location', lnglat), ("sort", "distance"), ("feedback", "false"), ('key', self._apiKey), ("pageSize", results), ("q", keyword)]
		url2 = url2 + urllib.parse.urlencode(query_parameters_two)
		r2 = self.getResult(url2)

		print(url2)
		
		myDict = []
		for i in r2["results"]:
			myDict.append(i["displayString"])

		return myDict