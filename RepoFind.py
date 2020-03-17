import requests

url = "https://api.github.com/search/repositories?q=org:{organization}&sort=forks&order=desc&per_page={per_page}"
user = "https://api.github.com/repos/{organization}/{repo_name}/stats/contributors"

def get_query(org, n, m):

    repo = requests.get(url.format(organization = org, per_page = n), headers={'Authorization': 'cc690ebb5f399d119c60398f7864dd47d3d6d553'}).json()

    store = []
    for i in repo["items"]:
        if (("forks_count" in i) and ("html_url" in i) and ("name" in i)):
            store.append((i["forks_count"], i["html_url"], i["name"]))

    repos = []

    for i in range(len(store)):

        cmt = requests.get(user.format(organization = org, repo_name = store[i][2]), headers={'Authorization': 'cc690ebb5f399d119c60398f7864dd47d3d6d553'}).json()
        newstore = []
        for j in cmt:
            if (("total" in j) and ("html_url" in j["author"]) and ("login" in j["author"])):
                newstore.append((j["total"], j["author"]["html_url"], j["author"]["login"]))

        newstore.sort(reverse=True)
        taken = newstore
        if (len(newstore) > m):
            taken = newstore[:m]

        repos.append((store[i][0], store[i][1], store[i][2], taken))

    return  repos



def get(org, n, m):
    if(n <= 0 or m <= 0):
        return "404"
    repos = get_query(org, int(n), int(m))
    return repos

