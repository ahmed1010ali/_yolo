import requests


url  = "http://127.0.0.1:8000/process_image/"
file_path = r"D:\Ahmed ali\AI Project\Yolo\attack-on-titan.jpeg"
with open (file_path, "rb") as file:
    response = requests.post (url, files = {"file":file})


if response.status_code == 200:
    path = "localServerOutput"
    with open (f"{path}/output_image.jpg", "wb")as output_files:
        output_files.write((response.content))
    print(f"Porcessed image saved as {path} output.jpg")
else:
    print (f"Error {response.status_code} - {response.text}")
