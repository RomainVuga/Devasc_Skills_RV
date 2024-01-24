import requests 
import json 
### Access Token 12 hours: https://developer.webex.com/docs/api/getting-started (login required)
access_token = "ZGU0Yzg3OWQtYjIyMy00MDM4LWJkYmItZTNkMjM0MTczZDkwZmU0NWQ0ZGItNWNj_PF84_4e1d5c08-564b-48e5-9d8f-c4e20787cdbf"

groups_struc = {
 "groups": [
      { "group": { "group_id": "G_1" , "group_name": "devasc_skills_RV" ,    
                   "members": [   
                     {"person_id": "P-1" , "person_name": "Romain", "email": "romain.vuga@student.odisee.be"}, 
                     {"person_id": "P-2" , "person_name": "Yvan", "email": "yvan.rooseleer@biasc.be"}
                   ]
                 }
      },
   ]
}

url = 'https://api.ciscospark.com/v1/rooms'

headers = {'Authorization': 'Bearer {}'.format(access_token),'Content-Type': 'application/json' }
for rec in groups_struc["groups"]:
    create_group_name = rec["group"]["group_name"]
    print("Creating ... " + create_group_name)
    payload_space={"title": create_group_name}
    res_space = requests.post(url, headers=headers, json=payload_space)

    NEW_SPACE_ID = res_space.json()["id"]
    for mbr in rec["group"]["members"]:
        room_id = NEW_SPACE_ID
        person_email = mbr["email"] 
        url2 = 'https://api.ciscospark.com/v1/memberships'
        payload_member = {'roomId': room_id, 'personEmail': person_email}
        res_member = requests.post(url2, headers=headers, json=payload_member)