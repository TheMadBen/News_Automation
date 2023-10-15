import requests
import json
import itertools

# using newsdata api
# Documentation: https://newsdata.io/documentation
def grab(query):
    base_url = 'https://newsdata.io/api/1/news'
    api_key = 'pub_30526a73b938d4de4161ba12b1ad67583b1cf'

    params = {
        'apikey': api_key,
        'q': query,
        'language': 'en',
        'timeframe': 48
    }
    
    response = requests.get(base_url, params=params)
    # print(response.status_code) # 200 means operation successful
    
    # convert output into json format
    json_response = response.json()
    
    # get number of results to tell how many links should appear at the end
    total_results = json_response.get('totalResults')
    # print('Total results: ' + str(total_results), end='\n\n')
    
    # write the response to output.txt since it's easier to view
    # Serializing json
    # json_object = json.dumps(json_response, indent=4)
 
    # Writing to output.json
    # with open("output.json", "w") as outfile:
    #     outfile.write(json_object)
    
    return json_response

def get_title(json_response):
    total_results = json_response.get('totalResults')
    
    title_list = []
    
    i = 0
    
    if total_results < 10:
        while i < total_results:
            title_list.append(json_response['results'][i]['title'])
            i+=1
    else:  
        while i < 10:
            title_list.append(str((json_response['results'][i]['title'])))
            i+=1
    
    # for title in title_list:
    #     print(title, end='\n\n')
    
    return title_list

def get_url(json_response):
    total_results = json_response.get('totalResults')
    
    url_list = []
    
    i = 0
    
    if total_results < 10:
        while i < total_results:
            url_list.append(json_response['results'][i]['link'])
            i+=1
    else:  
        while i < 10:
            url_list.append(json_response['results'][i]['link'])
            i+=1
    
    # for url in url_list:
    #     print(url, end='\n\n')
    
    return url_list

def get_description(json_response):
    total_results = json_response.get('totalResults')
    
    description_list = []
    
    i = 0
    
    if total_results < 10:
        while i < total_results:
            description_list.append(json_response['results'][i]['description'])
            i+=1
    else:  
        while i < 10:
            description_list.append(str(json_response['results'][i]['description']))
            i+=1
    
    # for description in description_list:
    #     print(description, end='\n\n')
    
    return description_list

def get_date(json_response):
    total_results = json_response.get('totalResults')
    
    date_list = []
    
    i = 0
    
    if total_results < 10:
        while i < total_results:
            date_list.append(json_response['results'][i]['pubDate'])
            i+=1
    else:  
        while i < 10:
            date_list.append(str(json_response['results'][i]['pubDate']))
            i+=1
    
    # for description in description_list:
    #     print(description, end='\n\n')
    
    return date_list
    
# this will allow URL_Grabber to be used as a module
def main():
    query = input('Enter search keyword: ')
    url_Encoded = query.replace(" ", "%20") # q for API is required to be url encoded
    json_response = grab(url_Encoded)
    title_list = get_title(json_response)
    description_list = get_description(json_response)
    url_list = get_url(json_response)
    date_list = get_date(json_response)
        
    combined_str = ''
    for (title, desc, url, date) in zip(title_list, description_list, url_list, date_list):
        combined_str = title+'\n'+desc+'\n'+url+'\n'+date+'\n\n'
        print(combined_str)

# this block allows the code to be run as a script but we want to import this as a module
if __name__ == "__main__":
    main()
