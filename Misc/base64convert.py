import base64
encoded = base64.b64encode('user:pass'.encode('UTF-8')).decode('ASCII')
print(encoded)