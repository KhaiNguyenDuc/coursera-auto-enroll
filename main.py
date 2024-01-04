import json
from functools import partial
import requests
from concurrent.futures import ThreadPoolExecutor


def enroll(count, cookies):

    url = "https://www.coursera.org/graphql-gateway?opname=Search"

    headers = {
        'content-type': 'application/json',
    }

    data = [{"operationName": "Search", "variables": {"requests": [
        {"entityType": "PRODUCTS", "searchContext": {"searchInPrograms": {"programIds": ["05YO7hGnEeyagxIonhTetw"]}},
         "limit": 100, "facetFilters": [["productTypeDescription:-Short Form Content Video"],
                                      ["productTypeDescription:-Short Form Content Lesson"],
                                      ["productTypeDescription:-Short Form Content Video"],
                                      ["productTypeDescription:-Short Form Content Lesson"]], "maxValuesPerFacet": 1000,
         "cursor": str(count), "query": ""},
        {"entityType": "PRODUCTS", "searchContext": {"searchInPrograms": {"programIds": ["05YO7hGnEeyagxIonhTetw"]}},
         "limit": 100, "facetFilters": [["productTypeDescription:-Specializations"],
                                       ["productTypeDescription:-Professional Certificates"],
                                       ["productTypeDescription:-Guided Projects"],
                                       ["productTypeDescription:-Projects"], ["productTypeDescription:-Courses"],
                                       ["productTypeDescription:-Specializations"],
                                       ["productTypeDescription:-Professional Certificates"],
                                       ["productTypeDescription:-Guided Projects"],
                                       ["productTypeDescription:-Projects"], ["productTypeDescription:-Courses"]],
         "maxValuesPerFacet": 1000, "cursor": str(count), "query": ""}]},
             "query": "query Search($requests: [Search_Request!]!) {\n  SearchResult {\n    search(requests: $requests) {\n      elements {\n        ... on Search_ArticleHit {\n          aeName\n          careerField\n          category\n          createdByName\n          firstPublishedAt\n          id\n          internalContentEpic\n          internalProductLine\n          internalTargetKw\n          introduction\n          islocalized\n          lastPublishedAt\n          localizedCountryCd\n          localizedLanguageCd\n          name\n          subcategory\n          topics\n          url\n          skill: skills\n          __typename\n        }\n        ... on Search_ProductHit {\n          avgProductRating\n          cobrandingEnabled\n          completions\n          duration\n          id\n          imageUrl\n          isCourseFree\n          isCreditEligible\n          isNewContent\n          isPartOfCourseraPlus\n          name\n          numProductRatings\n          parentCourseName\n          parentLessonName\n          partnerLogos\n          partners\n          productDifficultyLevel\n          productDuration\n          productType\n          skills\n          url\n          videosInLesson\n          translatedName\n          translatedSkills\n          translatedParentCourseName\n          translatedParentLessonName\n          __typename\n        }\n        ... on Search_SuggestionHit {\n          id\n          name\n          score\n          __typename\n        }\n        __typename\n      }\n      facets {\n        name\n        valuesAndCounts {\n          count\n          value\n          __typename\n        }\n        __typename\n      }\n      pagination {\n        cursor\n        totalElements\n        __typename\n      }\n      totalPages\n      source {\n        indexName\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"}]

    response = requests.post(url, headers=headers, json=data)
    result_values = [{}]

    if response.status_code == 200:
        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
        }

        json_response = response.json()

        search_results = json_response[0].get('data', {}).get('SearchResult', {}).get('search', [])
        for search_result in search_results:
            elements = search_result.get('elements', [])
            for element in elements:
                if 'id' in element:
                    full_id = element['id']
                    name = element['name']

                    extracted_id = full_id.split('~')[1] if '~' in full_id else full_id
                    if '-' in full_id[-12:] or '-' in full_id[-1:]:
                        extracted_id = extracted_id.rsplit('-', 1)[0]
                    json_value = {
                        "name": name,
                        "id": extracted_id
                    }
                    result_values.append(json_value)

        print(f"Page {count}")
        print(result_values)
    else:
        print("Failed to fetch data.")

    data = {
        # your data fields here
    }

    json_data = json.dumps(data)
    for result in result_values:
        enroll_url = f"https://www.coursera.org/api/programEnrollments.v2?programId=05YO7hGnEeyagxIonhTetw&userId=113671522&s12nId={result.get('id')}&action=enrollInS12n"
        response = requests.post(url=enroll_url, headers=headers, cookies=cookies, data=json_data)
        if response.status_code == 200:
            print(f"{result.get('name')} - response: Enroll specialization success")
        elif response.status_code == 400:
            json_response = response.json()
            if json_response.get("errorCode") == "ALREADY_ENROLLED_ERROR":
                print(f"{result.get('name')} ({result.get('id')}) - response: {json.loads(response.content).get('errorCode')}")
                pass
            if json_response.get("errorCode") == "PRODUCT_NOT_IN_PROGRAM":
                enroll_url = f"https://www.coursera.org/api/programEnrollments.v2?programId=05YO7hGnEeyagxIonhTetw&courseId={result.get('id')}&action=enrollInCourse"
                response = requests.post(url=enroll_url, headers=headers, cookies=cookies, data=json_data)
                json_response = response.json()
                if response.status_code == 200:
                    print(f"{result.get('name')} ({result.get('id')}) - response: Enroll course success")
                elif json_response.get("errorCode") == "ALREADY_ENROLLED_ERROR":
                    print(
                        f"{result.get('name')} ({result.get('id')}) - response: {json.loads(response.content).get('errorCode')}")
                    pass
                else:
                    print(f"{result.get('name')} ({result.get('id')}) - response: {json.loads(response.content).get('msg')}")
        elif response.status_code == 403:
            print(f"{result.get('name')} ({result.get('id')}) - response: Check your cookie again or active your account to business!")




if __name__ == "__main__":
    cookies = {}
    with open('cookies.txt', 'rb') as rawdata:
        cookie_string = rawdata.read().decode('utf-8')  # Read the content of the file and decode it to a string

        cookie_pairs = cookie_string.split('; ')  # Split the cookie string into key-value pairs

        for pair in cookie_pairs:
            key, value = pair.split('=', 1)  # Split each pair into key and value, using the first '=' occurrence
            cookies[key] = value

    print(cookies)
    thread_count = 5
    with open('thread.txt', 'r') as rawdata:
        thread_count = int(rawdata.read().split("=")[1])

    # Create a partially-applied function with fixed arguments (cookies)
    partial_enroll = partial(enroll, cookies=cookies)

    with ThreadPoolExecutor(max_workers=thread_count) as executor:
        # Execute the requests in parallel
        executor.map(partial_enroll, range(1, 50))
