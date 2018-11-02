import json
from pprint import pprint

people_string = '''
{
  "people": [
    {
      "name": "saksham maxwell",
      "phone": "9939739177",
      "email": "sakshammaxwell396@gmail.com",
      "licence": false
    },
    {
      "name": "john",
      "phone": "8935996445",
      "email": null,
      "licence": "true"

    }
  ]
}

'''

data = json.loads(people_string)
#print(data)

for person in data["people"]:
    print(person["name"])
    print(person["email"])


