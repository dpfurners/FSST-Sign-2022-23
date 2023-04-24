import requests

url = "https://www.lehrer-wuerfelt.at/api?count=3"

# result_json = requests.get(url).json()

result_json = {
    "tries": [
        {
            "index": 1,
            "result": 3,
            "image": "http://www.lehrer-wuerfelt.at/image/drei.png"
        },
        {
            "index": 2,
            "result": 5,
            "image": "http://www.lehrer-wuerfelt.at/image/fuenf.png"
        },
        {
            "index": 3,
            "result": 2,
            "image": "http://www.lehrer-wuerfelt.at/image/zwei.png"
        }
    ]
}

print("\n".join([str(trie["result"]) for trie in result_json["tries"]]))
