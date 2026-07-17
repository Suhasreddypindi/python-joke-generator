import requests
url = "https://official-joke-api.appspot.com/random_joke"
print("=" * 40)
print("Joke of the Day")
print("="*40)
while True:
    response = requests.get(url)
    if response.status_code != 200:
        print("Request failed")
        break
    data = response.json()  
    print()
    print(data['setup'])
    input("\nPress Enter for the punchline...")
    print(data['punchline'])
    yolo = input("Would you like another joke? (y/n): ")
    if yolo.lower() == "n":
        print("Goodbye!")
        break