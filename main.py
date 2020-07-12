import requests
import json

BASEURL = "https://api.github.com"

def getPRs(repoList):
    PRList = []

    for repo in repoList:
        URL = f"{BASEURL}/repos/{repo}/pulls?state=all"
        headers = {'Accept': 'application/vnd.github.sailor-v-preview+json'}
        req = requests.get(URL, headers)

        jsonData = json.loads(req.text)
        for PR in jsonData:
            if PR['user']['login'] == "IamCathal":
                PRObj = {
                    "url": PR["html_url"],
                    "title":PR["title"],
                    "repo": PR["base"]["repo"]["html_url"],
                    "createdAt": PR["created_at"],
                    "mergedAt": PR["merged_at"]
                }
                PRList.append(PRObj)

    for PR in PRList:
        print(PR)

    return PRList

def writeReadMe(recentPRs):
    staticText = """
## Howya doing I'm Cathal, a passionate 2nd year CS&IT student in NUIG

I'm by no means an expert but I love working with golang and like to use python and javascript. I'm currently an [MLH Fellowship](https://fellowship.mlh.io/) intern which is amazing. It's an internship focused entirely on helping students start their journey in contributing to the world of open source. Not only are we learning about the best practices and design choices but we are also contributing to real world projects that make an impact

### Heres are some recent PRs I've worked on:
##### This readme is auto generated, checkout the [the source code](https://github.com/iamcathal/iamcathal/blob/master/main.py)
| Title        | Repo         | Status |
| ------------- |:-------------:| -----:|
"""
    for PR in recentPRs:
        staticText += f"| {PR['title']} | [link]({PR['repo']}) | {'Merged 🎉' if PR['mergedAt'] else 'Open'} |\n"

    f = open("README.md", "w")
    f.write(staticText)
    f.close()

    print(staticText)


def main():
    repoList = [
        "poychang/github-dark-theme",
        "pallets/click"
        ]
    PRList = getPRs(repoList)
    writeReadMe(PRList)


if __name__ == '__main__':
    main()