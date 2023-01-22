from operator import itemgetter

import requests

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url=url)
print(f"Status code: {r.status_code}")

# przetwarzanie informacji o każdym artykule
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # utworzenie słownika dla każdego artykułu
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': '',
        'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTytuł artykułu: {submission_dict['title']}")
    print(f"Łącze do dyskusji: {submission_dict['hn_link']}")
    print(f"Liczba komentarzy: {submission_dict['comments']}")