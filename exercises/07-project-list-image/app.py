import requests

url = "https://assets.breatheco.de/apis/fake/sample/project_list.php"
response = requests.get(url)

   
if response.status_code == 200:
    # Parsing JSON response
    project_list = response.json()
    
    # Extracting the last project
    last_project = project_list[-1]
        
    # Extracting the last image URL
    last_image_url = last_project["images"][-1]
            
    # Printing the last image URL
    print(last_image_url)  
else:
    print("Failed to fetch project list.")