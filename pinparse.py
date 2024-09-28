import requests, json, re

def search_pinterest(query, num_pins=10):
    url = f"https://www.pinterest.com/resource/BaseSearchResource/get/?source_url=%2Fsearch%2Fpins%2F%3Fq%3D{query}&data=%7B%22options%22%3A%7B%22query%22%3A%22{query}%22%2C%22scope%22%3A%22pins%22%2C%22auto_correction_disabled%22%3Afalse%7D%2C%22context%22%3A%7B%7D%7D"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Error: THIS SHIET DOSNT WORK AGAIN AAHH >~<. Status code: {response.status_code}")
        return []

    data = json.loads(response.text)
    results = data["resource_response"]["data"]["results"]

    pins = []
    for result in results[:num_pins]:
        pin = {
            "id": result["id"],
            "title": result.get("title", ""),
            "description": result.get("description", ""),
            "link": result.get("link", ""),
            "image_url": result["images"]["orig"]["url"] if "images" in result else "",
            "pin_url": f"https://www.pinterest.com/pin/{result['id']}/",
        }
        pins.append(pin)

    return pins

def debug():
    query = input("search query o.o: ")
    pins = search_pinterest(query)

    print(f"\nfirst 10 pins for search query >w< '{query}':\n")
    for i, pin in enumerate(pins, 1):
        print(f"pin {i}:")
        print(f"title: {pin['title']}")
        print(f"description: {pin['description']}")
        print(f"link: {pin['link']}")
        print(f"img URL: {pin['image_url']}")
        print(f"pin URL: {pin['pin_url']}")
        print()

if __name__ == "__main__":
    debug()