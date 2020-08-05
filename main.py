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
                    "pullRequestLink":PR["_links"]["html"]["href"],
                    "createdAt": PR["created_at"],
                    "mergedAt": PR["merged_at"]
                }
                PRList.append(PRObj)
    return PRList


def writeReadMe(recentPRs):
    staticText = """
## Howya doing I'm Cathal, a passionate 2nd year CS&IT student in NUIG

I'm currently an [MLH Fellowship](https://fellowship.mlh.io/) intern. It's an internship focused entirely on helping students start their journey in contributing to the world of open source. Not only does this include learning about the best practices and design choices but we are also contributing to real world projects that make an impact. At the moment
I'm mostly devoting my time to work on [Beego](https://github.com/astaxie/beego), a high performance golang web framework


### I use often:
<img align="left" alt="Golang" width="56px" style="padding-top:5px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Go_Logo_Blue.svg/220px-Go_Logo_Blue.svg.png" />

<img align="left" alt="Python" width="36px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/600px-Python-logo-notext.svg.png" />

<img align="left" alt="Javascript" width="32px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/javascript/javascript.png" />

<img align="left" alt="GitHub/git" width="32px" src="https://raw.githubusercontent.com/github/explore/89bdd9644f44d1b12180fd512b95574fe4c54617/topics/github-api/github-api.png" />

<img align="left" alt="Linux" width="32px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Tux.png/220px-Tux.png" />

<br />

### I have used:


<img align="left" alt="Java" width="25px" src="https://upload.wikimedia.org/wikipedia/en/thumb/3/30/Java_programming_language_logo.svg/1200px-Java_programming_language_logo.svg.png" />

<img align="left" alt="NodeJS" width="32px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/nodejs/nodejs.png" />

<img align="left" alt="HTML" width="32px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/html/html.png" />

<img align="left" alt="Docker" width="36px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/docker/docker.png" />

<img align="left" alt="GraphQL" width="32px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/GraphQL_Logo.svg/1200px-GraphQL_Logo.svg.png" />

<img align="left" alt="Amazon web services (AWS)" width="36px" src="https://raw.githubusercontent.com/github/explore/fbceb94436312b6dacde68d122a5b9c7d11f9524/topics/aws/aws.png" />

<img align="left" alt="C" width="36px" src="https://iamcathal.github.io/svgImages/C.svg" />


<img align="left" alt="MongoDB" width="38px" src="https://iamcathal.github.io/svgImages/mongo.svg" />

<img align="left" alt="MySql" width="36px" src="https://iamcathal.github.io/svgImages/mysql.svg" />


<img align="left" alt="Raspberry Pi" width="38px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/raspberry-pi/raspberry-pi.png" />


<br />
<br />

### Heres some recent PRs I've worked on:
| | |
| ------------- |:-------------:|
"""
    for PR in recentPRs:
        staticText += f"| [{PR['title']}]({PR['pullRequestLink']})| {'Merged 🎉' if PR['mergedAt'] else 'Open'} |\n"

    staticText += "##### This readme is auto generated, checkout [the source code](https://github.com/iamcathal/iamcathal/blob/master/main.py)"
    f = open("README.md", "w")
    f.write(staticText)
    f.close()

    print(staticText)


def main():
    repoList = [
        "poychang/github-dark-theme",
        "pallets/click",
        "astaxie/beego"
        ]
    PRList = getPRs(repoList)
    writeReadMe(PRList)


if __name__ == '__main__':
    main()