import requests
from urllib.parse import urlparse

def scalable_serp_lookup(query, api_key):

    all_results = []
    parsed_data = []

    headers = {
        "X-API-KEY": api_key,
        "Content-Type": "application/json"
    }

    for page in range(1, 6):

        payload = {
            "q": query,
            "page": page,
            "gl": "us",
            "hl": "en"
        }

        response = requests.post(
            "https://google.serper.dev/search",
            headers=headers,
            json=payload,
            timeout=30
        )

        response.raise_for_status()

        results = response.json()

        organic_results = results.get("organic", [])

        if not organic_results:
            break

        all_results.extend(organic_results)

        print(f"Page {page}: {len(organic_results)} results")

    print("length of all_results :", len(all_results))

    for item in all_results:

        # Serper field names
        link = item.get("link", "")

        parsed = urlparse(link)

        if "linkedin.com" in parsed.netloc and "/in/" in parsed.path:

            parsed_data.append({
                "title": item.get("title"),
                "link": link,
                "snippet": item.get("snippet", "")
            })

    print("length of parsed_data :", len(parsed_data))

    return parsed_data


# Example
if __name__ == "__main__":

    result = scalable_serp_lookup(
        'site:linkedin.com/in "Dentist"',
        "YOUR_SERPER_API_KEY"
    )

    for item in result:
        print(item)