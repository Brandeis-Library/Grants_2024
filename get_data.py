import requests
import json

class get_data_openAlex:
#Brandeis institution id: i6902469

#this url is for Brandeis 2024
#api for get only 2024 grants: https://api.openalex.org/works?filter=institutions.id:https://openalex.org/I6902469,publication_year:2024&sort=publication_date:desc

    def __init__(self, year, file_name):
        self.year= year
        self.file_name = file_name


#base_url = 'https://api.openalex.org/works?filter=institutions.id:https://openalex.org/I6902469,publication_year:2023&sort=publication_date:desc'
    def get_data_openAlex(self):
        all_results = []
        api_url = f'https://api.openalex.org/works?filter=institutions.id:https://openalex.org/I6902469,publication_year:{self.year}&sort=publication_date:desc'
        print(api_url)
        response = requests.get(api_url)
    
        if response.status_code == 200:
            data = response.json()
            all_results.extend(data.get('results', []))
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")

        with open(self.file_name, 'w') as json_file:
            json.dump(all_results, json_file, indent=4)

