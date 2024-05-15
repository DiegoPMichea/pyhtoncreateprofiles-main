import unittest
import csv
import json
import os

class TestCsvToJson(unittest.TestCase):

    def setUp(self):
        self.csv_file = 'profiles1.csv'
        self.json_file = 'data.json'

    def test_csv_file(self):
        with open(self.csv_file, 'r', encoding='utf-8-sig') as file:
            csv_data = csv.reader(file)
            header = next(csv_data)
            self.assertEqual(len(header), 12)  # Check if CSV file has 12 columns
            rows = list(csv_data)
            self.assertTrue(len(rows) >= 900)  # Check if CSV file has 900+ rows

    def test_json_file(self):
        with open(self.json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            self.assertTrue(len(data) >= 900)  # Check if JSON file has 900+ rows
            # Check if all properties are present in the first dictionary
            self.assertEqual(len(data[0]), 12)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()