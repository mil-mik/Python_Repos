import requests

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
# wykonanie wywołania API i zachowanie otrzymanej odpowiedzi
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)

print(f"Kod stanu: {r.status_code}")

# umieszczenie odpowiedzi API w zmiennej
response_dict = r.json()
print(f"Calkowita liczba repozytoriow: {response_dict['total_count']}")

# przetwarzanie informacji o repozytoriach
repo_dicts = response_dict['items']
print(f"Liczba zwróconych repozytoriów: {len(repo_dicts)}")

# przetwarzania pierwszego repozytorium
# repo_dict = repo_dicts[0]
# print(f"\nKlucze: {len(repo_dict)}")
# for key in sorted(repo_dict.keys()):
#     print(key)

print("\nWybrane informajce o każdym repozytorium:")
for repo_dict in repo_dicts:
    print(f"\nNazwa: {repo_dict['name']}")
    print(f"Właściciel: {repo_dict['owner']['login']}")
    print(f"Gwiazdki: {repo_dict['stargazers_count']}")
    print(f"Repozytorium: {repo_dict['html_url']}")
    print(f"Utworzone: {repo_dict['created_at']}")
    print(f"Uaktualnione: {repo_dict['updated_at']}")
    print(f"Opis: {repo_dict['description']}")
