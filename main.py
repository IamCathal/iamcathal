import requests
import random
import json

BASEURL = "https://api.github.com"

def getPRs(repoList):
    PRList = []
    currentPRsFound = 0
    pageCount = 1

    for repo in repoList:
        currentPRsFound = 0
        URL = f"{BASEURL}/repos/{repo}/pulls?state=all&per_page=100"
        headers = {'Accept': 'application/vnd.github.v3+json'}
        req = requests.get(URL, headers)
        jsonData = json.loads(req.text)
        i = 0
        print(f"Fetching [repo:{repo}][pageCount:{pageCount}]")
        for PR in jsonData:
            if PR['user']['login'] == "IamCathal":
                print(f'[{i}/{len(jsonData)}] - {PR["title"]} - {PR["_links"]["html"]["href"]}')
                PRObj = {
                    "url": PR["html_url"],
                    "title":PR["title"],
                    "repo": PR["base"]["repo"]["html_url"],
                    "pullRequestLink":PR["_links"]["html"]["href"],
                    "createdAt": PR["created_at"],
                    "mergedAt": PR["merged_at"]
                }
                currentPRsFound += 1
                PRList.append(PRObj)
            i += 1
        if (currentPRsFound == 0):
            print(f"No PRs for [Repo:{repo}][pageCount:{pageCount}]")
            pageCount += 1

            while (currentPRsFound == 0) and (pageCount < 6):
                currentPRsFound = 0
                headers = {'Accept': 'application/vnd.github.v3+json'}
                URL = f"{BASEURL}/repos/{repo}/pulls?state=all&per_page=100&page={pageCount}"
                print(f"Getting page {URL}")
                print(f"Fetching [repo:{repo}[pageCount:{pageCount}]")
                req = requests.get(URL, headers)
                jsonData = json.loads(req.text)
                i = 0
                for PR in jsonData:
                    if PR['user']['login'] == "IamCathal":
                        print(f'[{i}/{len(jsonData)}] - {PR["title"]} - {PR["_links"]["html"]["href"]}')
                        PRObj = {
                            "url": PR["html_url"],
                            "title":PR["title"],
                            "repo": PR["base"]["repo"]["html_url"],
                            "pullRequestLink":PR["_links"]["html"]["href"],
                            "createdAt": PR["created_at"],
                            "mergedAt": PR["merged_at"]
                        }
                        currentPRsFound += 1
                        PRList.append(PRObj)
                    i += 1
                pageCount += 1

    print(f"Returning: {PRList}")
    return PRList


def writeReadMe(recentPRs):
    staticText = """
## Howya doing I'm Cathal

* Love working with golang but also use python and javascript for various projects.
* My most recent project is [Neo](https://github.com/NeoSteamFriendGraphing/neo), a distributed system built for my final year project which generates an indepth analysis of your friend network on Steam to see exactly what kind of friends you have or find the shortest distance between two steam users. 
* Mainly into backend development and love writing the underlying infrastructure behind projects such as [Req](https://github.com/ReqApp/Req) or [Fellowship Wrapup](https://github.com/MLH-Fellowship/FellowshipWrapup) (both of which came first place in their respective competitions). My overall grade for Neo was 90%, you can view my exam transcript [here](https://cathaloc.dev/results.html)

### I use often:
<img align="left" alt="Golang" width="56px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Go_Logo_Blue.svg/1200px-Go_Logo_Blue.svg.png" />

<img align="left" alt="Python" width="36px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/600px-Python-logo-notext.svg.png" />

<img align="left" alt="Java" width="25px" src="https://upload.wikimedia.org/wikipedia/en/thumb/3/30/Java_programming_language_logo.svg/1200px-Java_programming_language_logo.svg.png" />

<img align="left" alt="Javascript" width="32px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/javascript/javascript.png" />

<img align="left" alt="GitHub/git" width="32px" src="https://raw.githubusercontent.com/github/explore/89bdd9644f44d1b12180fd512b95574fe4c54617/topics/github-api/github-api.png" />

<img align="left" alt="Linux" width="32px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Tux.png/220px-Tux.png" />

<img align="left" alt="Docker" width="36px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/docker/docker.png" />

<img align="left" alt="Raspberry Pi" width="38px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/raspberry-pi/raspberry-pi.png" />

<br />
<br />
<hr>

<details><summary> Here are some recent PRs I've worked on </summary>

| | |
| ------------- |:-------------:|
"""
    chosenPRs = []
    maxPRs = len(recentPRs) if len(recentPRs) <= 5 else 5
    for x in range(maxPRs):
        pick = random.randint(0, len(recentPRs)-1)
        while pick in chosenPRs:
             pick = random.randint(0, len(recentPRs)-1)

        chosenPRs.append(pick)

        staticText += f"| [{recentPRs[pick]['title']}]({recentPRs[pick]['pullRequestLink']})| {'Merged 🎉' if recentPRs[pick]['mergedAt'] else 'Open'} |\n"

    staticText += "##### This readme is auto generated, checkout [the source code](https://github.com/iamcathal/iamcathal/blob/master/main.py)"
    staticText += "</details>"
    f = open("README.md", "w")
    f.write(staticText)
    f.close()

    print(staticText)


def main():
    repoList = [
        "pallets/click",
        "beego/beego"
        ]
    PRList = getPRs(repoList)
    writeReadMe(PRList)


if __name__ == '__main__':
    main()