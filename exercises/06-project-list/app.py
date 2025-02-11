import requests

url = "https://assets.breatheco.de/apis/fake/sample/project_list.php"
response = requests.get(url)

if response.status_code == 200:
    # Parsing JSON response
    second_project = response.json()[1]
    
    # Extracting second project name
    project_name = second_project["name"]

    print(project_name)
else:
    print("Failed to fetch project data.")