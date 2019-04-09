'''

Exercise 3: information about a github user

Create a python program that ask the user for a github username and print on the console the following information about
that username:

-Real name
-The list with the names of all the repos the user has
-The total number of commits to the 2018-19-PNE-repo

'''


import http.client
import json

user_input = input('Enter the name of a github user: ')

HOSTNAME = "api.github.com"
ENDPOINT = "/users/"
GITHUB_ID = user_input
METHOD = "GET"

headers = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection(HOSTNAME)

conn.request(METHOD, ENDPOINT + GITHUB_ID, None, headers)

r1 = conn.getresponse()

print()
print("Response received: ", end='')
print(r1.status, r1.reason)

text_json = r1.read().decode("utf-8")
conn.close()

user = json.loads(text_json)

login = user['login']
name = user['name']
bio = user['bio']
nrepos = user['public_repos']

print()
print("User: {}".format(login))
print("Name: {}".format(name))
print("Repos: {}".format(nrepos))
print("Bio: \n{}".format(bio))

"""

REQUEST 2: 
-NAMES OF THE PUBLIC REPOS

"""

ENDPOINT_2 = "/repos"
METHOD = "GET"


conn.request(METHOD, ENDPOINT + GITHUB_ID + ENDPOINT_2, None, headers)

r2 = conn.getresponse()

print()
print("Response received: ", end='')
print(r2.status, r2.reason)
print()

text_json = r2.read().decode("utf-8")
conn.close()

repos = json.loads(text_json)

# We create a counter startint at 0 to find the number of repos the dictionary has (as elements)
counter = 0
for element in range(len(repos)):
    counter += 1
print("The number of repos is: {}".format(counter))

for element in range(len(repos)):
    print(' -{}.{}'.format(element, repos[element]["name"]))


"""

REQUEST 3: 
-Commits in 2018-19-PNE-practices

"""

ENDPOINT_3 = "/2018-19-PNE-practices/stats/contributors"
METHOD = "GET"


conn.request(METHOD, ENDPOINT_2 + "/" + GITHUB_ID + ENDPOINT_3, None, headers)

r3 = conn.getresponse()

print()
print("Response received: ", end='')
print(r3.status, r3.reason)
print()

text_json = r3.read().decode("utf-8")
conn.close()

commits = json.loads(text_json)

print("The total number of commits in the 2018-19-PNE-practices is: {}".format(commits[0]["total"]))