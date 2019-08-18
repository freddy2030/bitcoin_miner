import httplib2 as hp
import base64
import json

def outrequest(r):
    print(str(r))

host = "127.0.0.1"
port = 8332

conn = hp.HTTPConnectionWithTimeout(host, port)

obj = { 'jsonrpc' : '1.0',
		'method' : "getwork",
		'id' : "1" }
authpair = 'freddy:fd123qweqwe'  
authhdr = "Basic %s" % (base64.b64encode(str.encode(authpair)))
print(authhdr)
print(json.dumps(obj))
res = conn.request('POST', '/', json.dumps(obj),
			{ 'Authorization' : authhdr,
			  'Content-type' : 'application/json' })
print(res)
# print("11"+str(dir(hp)))

