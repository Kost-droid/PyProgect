import http.client

direct_url = 'kost-droid.github.io'
direct_path = '/Inet_test'

proxy_host = 'localhost'
proxy_port = 12345

conn = http.client.HTTPConnection (proxy_host, proxy_port)

conn.set_tunnel(direct_url)
conn.request('GET', direct_path)
response = conn.getresponse()

print (response.status, response.reason)
print (response.read().decode())

conn.close()
