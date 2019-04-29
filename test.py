import os, unittest, argparse, json, client
import xml.etree.ElementTree as ET

class TestPerson(unittest.TestCase):

    test_data = ('first_name,surname,age,nationality,favourite_color,interest\n'
      'John,Keynes,29,British,red,cricket\n'
      'Sarah,Robinson,54,,blue,badminton\n')
      
    def test_json_file(self):
        """
        Test if the JSON response returned is valid  - Input through file (sample_data.csv)
        """
        #response = os.system("python3 client.py -f filename.csv")
        response = client.result(False, 'json', 'unittest',file = 'test_file.csv')
        response = json.loads(response)
        first_name = response['person'][0]['first_name']
        self.assertEqual(first_name,'John','Should print John')
        length = len(response['person'])
        for count in range(0,length):
          self.assertNotIn('nationality',response['person'][count], 'Nationality should not be present')
    
    def test_xml_file(self):
        """
        Test if the XML response returned is valid  - Input through file (sample_data.csv)
        """
        response = client.result(False, 'xml', 'unittest', file = 'test_file.csv')
        root = ET.fromstring(response)
        first_name = root[0][0][0].text
        self.assertEqual(first_name,'John', 'Should print John')
        nationality = '<nationality>' in response
        self.assertFalse(nationality, 'Nationality should not be present')

    def test_json_direct(self):
        """
        Test if the JSON response returned is valid  - Input directly 
        """ 
        response = client.result(True, 'json', 'unittest', test_data = self.test_data)
        response = json.loads(response)
        first_name = response['person'][0]['first_name']
        self.assertEqual(first_name,'John','Should print John')
        length = len(response['person'])
        for count in range(0,length):
          self.assertNotIn('nationality',response['person'][count], 'Nationality should not be present')

    def test_xml_direct(self):
        """
        Test if the XML response returned is valid  - Input directly 
        """ 
        response = client.result(True, 'xml', 'unittest', test_data = self.test_data)
        root = ET.fromstring(response)
        first_name = root[0][0][0].text
        self.assertEqual(first_name,'John', 'Should print John')
        nationality = '<nationality>' in response
        self.assertFalse(nationality, 'Nationality should not be present')

if __name__ == "__main__":
    unittest.main()
