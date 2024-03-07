from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from googlesearch import search
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json  
from requests.exceptions import ReadTimeout

def search_and_similarity(line):
    unique_domains = {}
    report = {}
    distinct_domains = set()
    print("Search started")
    report['query'] = line
    lines_source = []
    report['lines_source'] = []
    line_part = line.split('.')

    for url in search(line, stop=2):
        if url.strip():  # Check if URL is not empty or whitespace
            print(url)
            parsed_url = urlparse(url)
            domain = parsed_url.netloc
            # unique_domains.add(domain)
            # print(domain),
            # report['domains'] = list(unique_domains)
            for line_part in line.split('.'):
                line_source_entry = {"line_part": line_part , "url": url}
                lines_source.append(line_source_entry)
                report['lines_source'].append(line_source_entry)
                
            unique_domains[domain] = unique_domains.get(domain, 0) + 1
            distinct_domains.add(domain) 
            print(domain)
            lines_source.append({"line": line, "url": url})
            report['urls'] = report.get('urls', [])
            report['urls'].append(url)
            report['domains'] = [{'domain': domain, 'count': count} for domain, count in unique_domains.items()]
            try :
                #print(url)
                r = requests.get(url , timeout=30 )  # Search in Google
                soup = BeautifulSoup(r.content, "html.parser")
                paragraphs = soup.find_all("p")
                report['corpus_data'] = ' '.join([paragraph.get_text() for paragraph in paragraphs])
            except ReadTimeout:
                report['corpus_data'] = ""
        else:
            print("No plagiarism found")
            
            # for line_part in line.split('.'):
            #     line_source_entry = {"line_part": line_part, "url": ""}
            #     lines_source.append(line_source_entry)
            #     report['lines_source'].append(line_source_entry)
                
    report['distinct_domain_count'] = len(distinct_domains)
            
    text1 = (report['corpus_data'])
    print("similarity checking")
    text2 = line
    print(text2)
        # Create a TF-IDF vectorizer    
    vectorizer = CountVectorizer()
        # Fit and transform the documents into TF vectors
    tf_matrix = vectorizer.fit_transform([text1, text2])
        # Compute cosine similarity between the TF vectors
    cosine_sim = cosine_similarity(tf_matrix[0], tf_matrix[1])[0][0]
        # Calculating plagiarism percentage
    plag_percent = cosine_sim * 100     
    report['plag_percent'] = plag_percent
    # json_report= json.dumps(report, indent=4,ensure_ascii=False)  
    
    return report 

# def similarity():
    
#     text1 = (corpus['corpus_data'])
#     print("similarity checking")
#     text2 = "I apologize for the confusion. It appears I made an error in my response. The slugify function is not directly available in the django.utils.text module. Instead, you can use the slugify function from the django.utils module."
#     print(text2)
#         # Create a TF-IDF vectorizer    
#     vectorizer = CountVectorizer()
#         # Fit and transform the documents into TF vectors
#     tf_matrix = vectorizer.fit_transform([text1, text2])
#         # Compute cosine similarity between the TF vectors
#     cosine_sim = cosine_similarity(tf_matrix[0], tf_matrix[1])[0][0]
#         # Calculating plagiarism percentage
#     plag_percent = cosine_sim * 100 
        
#     return plag_percent

#print(search_and_similarity(".An attempt to orient the unconverted and the semi-converted on the history and benefits of Free and Open Source Software (FOSS). Created for the PANACeA FOSS training in Bangkok (Feb 2010). ."))
