import requests

base_url = "https://192.168.56.101/restconf/data/Cisco-IOS-XE-native:native/logging/monitor/severity"
headers = {'Accept': 'application/yang-data+json'}
auth = ('cisco', 'cisco123!')

#OPTIONS
options_response = requests.options(base_url, headers=headers, auth=auth)
print(f"OPTIONS Response: {options_response.status_code}")
print(options_response.text)
print("")

#POST
post_data = {'severity': 'alerts'}
post_response = requests.post(base_url + "/monitor", json=post_data, headers=headers, auth=auth)
print(f"POST Response: {post_response.status_code}")
print(post_response.text)
print("")

#PUT
put_data = {'severity': 'warnings'}
put_response = requests.put(base_url, json=put_data, headers=headers, auth=auth)
print(f"PUT Response: {put_response.status_code}")
print(put_response.text)
print("")

#PATCH
patch_data = {
    "native": {
        "logging": {
            "monitor": {
                "severity": "informational"
            }
        }
    }
}
patch_response = requests.patch(base_url + "/native", json=patch_data, headers=headers, auth=auth)
print(f"PATCH Response: {patch_response.status_code}")
print(patch_response.text)
print("")

#GET
get_response = requests.get(base_url, headers=headers, auth=auth)
print(f"GET Response: {get_response.status_code}")
print(get_response.text)
print("")

#DELETE
delete_response = requests.delete(base_url, headers=headers, auth=auth)
print(f"DELETE Response: {delete_response.status_code}")
print(delete_response.text)