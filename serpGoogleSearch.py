from serpapi import GoogleSearch
from urllib.parse import urlparse

def scalable_serp_lookup(query, api_key):

    all_results = []
    parsed_data = []

    for page in range(5):  
        params = {
            "engine": "google",
            "q": query,
            "hl": "en",
            "gl": "us",
            "api_key": api_key,
            "start": page * 10
        }

        search = GoogleSearch(params)
        results = search.get_dict()
        
        # Directly access cleanly structured JSON fields safely
        organic_results = results.get("organic_results", [])
        if not organic_results:
            break
        all_results.extend(organic_results)
        print(organic_results)
    for item in all_results:
        print("length of all_results :", len(all_results))
        print("---------------------")
        link = item.get("link", "")
        parsed = urlparse(link)
        if "linkedin.com" in parsed.netloc and "/in/" in parsed.path:
            parsed_data.append({
                "title": item.get("title"),
                "link": link,
                "snippet": item.get("snippet")
            })
    print("length of parsed_data :", len(parsed_data))   
    return parsed_data

#result = scalable_serp_lookup("site:linkedin.com \"Dentist\"", "75ac323eb184a40538fb99b6b2984e2d0b78b276e527a32b59d2a40b7385465b")
# print(result)

# Example invocation (Requires a valid API token from SerpApi)
# if __name__ == "__main__":
#     data = scalable_serp_lookup("best data orchestration tools", "YOUR_API_KEY_HERE")
#     print(data)
