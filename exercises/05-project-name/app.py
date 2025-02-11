import requests

url = "https://assets.breatheco.de/apis/fake/sample/project1.php"
response = requests.get(url)

if response.status_code == 200:
    # Parsing JSON response
    project_data = response.json()
    
    # Extracting project name
    project_name = project_data["name"]

    print(project_name)
else:
    print("Failed to fetch project data.")