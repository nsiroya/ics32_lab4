import unittest
from Lab4_XXXXXXXX import *
# You must import your script name (ex: Lab4_12345678), no file extension,
# followed by 'import *'
# example: from Lab4_12345678 import *
# You must also enter YOUR API key in each test


class Lab4StudentTest(unittest.TestCase):
    def test1(self):
        m = MapQuest('!!!!!ENTER YOUR API HERE!!!!!')
        locations = ['3750 barranca pkwy, Irvine, CA 92606', '4143 Campus Dr, Irvine, CA 92612', '3333 Bristol St, Costa Mesa, CA']
        self.assertEqual( m.totalDistance(locations), 10.318)
    def test2(self):
        m = MapQuest('!!!!!ENTER YOUR API HERE!!!!!')
        locations = ['3750 barranca pkwy, Irvine, CA 92606', '4143 Campus Dr, Irvine, CA 92612', '3333 Bristol St, Costa Mesa, CA']
        self.assertEqual( 946 <= m.totalTime(locations) <= 947, True)
    def test3(self):
        m = MapQuest('!!!!!ENTER YOUR API HERE!!!!!')
        locations = ['3750 barranca pkwy, Irvine, CA 92606', '4143 Campus Dr, Irvine, CA 92612', '3333 Bristol St, Costa Mesa, CA']
        directions = 'Start out going east on Barranca Pkwy toward Culver Dr.\nTurn right onto Culver Dr.\nTurn right onto Campus Dr.\nTurn left onto Cornell.\nTurn left onto Campus Dr.\nCAMPUS DRIVE.\nStart out going east on Campus Dr toward California Ave.\nTurn left onto Culver Dr.\nMerge onto I-405/San Diego Fwy.\nTake the Bristol St/Anton Blvd exit, EXIT 9B, toward Avenue of the Arts.\nKeep left at the fork in the ramp.\nTurn right onto Bristol St.\nTurn right to stay on Bristol St.\nTurn left to stay on Bristol St.\nTurn left onto Sunflower Ave.\nTurn left onto Bristol St.\nBRISTOL STREET.\n'
        self.assertEqual( m.directions(locations), directions)
    def test4(self):
        results = ['R & M Pacific Rim Inc, 4601 Campus Dr, Irvine, CA 92612', 'Extra Mile, 18002 Culver Dr, Irvine, CA 92612', 'CHEVRON #96698, 18002 Culver Dr, Irvine, CA 92612', 'Culver Auto Spa, 18011 Culver Dr, Irvine, CA 92612', 'Chevron Station, 1240 Bison Ave, Newport Beach, CA 92660', '76, 2690 San Miguel Dr, Newport Beach, CA 92660', 'New Port Hills 76, 2690 San Miguel Dr, Newport Beach, CA 92660', 'J R Enterprises, 4299 Macarthur Blvd, Newport Beach, CA 92660', 'R & M Shell, 3090 Main St, Irvine, CA 92614', 'Chevron USA Inc, 2121 SE Bristol St, Newport Beach, CA 92660']
        m = MapQuest('!!!!!ENTER YOUR API HERE!!!!!')
        yourResults = m.pointOfInterest('4143 Campus Dr, Irvine, CA 92612', 'gas station', 10)
        for i in range(len(results)):
            self.assertEqual( results[i], yourResults[i])
if __name__ == "__main__":
    unittest.main()

