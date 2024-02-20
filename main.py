# This is a sample Python script.
import requests

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


url = "https://currency-converter5.p.rapidapi.com/currency/convert"

querystring = {"format": "json", "from": "AUD", "to": "CAD", "amount": "1"}

headers = {
    "X-RapidAPI-Key": "5f494f4ab5msh1cb5cae5f817f1ap130291jsn5e213ba6595d",
    "X-RapidAPI-Host": "currency-converter5.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Hello, World!")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
