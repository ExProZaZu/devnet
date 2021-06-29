import socket
ips = ["10.145.81.100", "10.145.92.100", "10.145.81.101", "8.8.8.8"]
for i in range(4):
    nslookuptest = socket.getfqdn(ips[i])
    print(nslookuptest)












# url = "https://192.168.0.151:9060/ers/config/endpointgroup"
# listnames = list(names.names2)
# listdesc = list(names.names2.values())
# for i in range(34):
#     payload1 = {
#     "EndPointGroup": {
#         "name": listnames[i],
#         "description": listdesc[i]
#     }}
#     headers = {
#     'content-type': "application/json",
#     'accept': "application/json",
#     'authorization': "Basic ZXJzdXNlcjpXYWx0ZXIxOA==",
#     'cache-control': "no-cache",}
#     response = requests.request(
#     "POST",
#     url,
#     data=json.dumps(payload1),
#     headers=headers,
#     verify=False)
#     print(response.text)