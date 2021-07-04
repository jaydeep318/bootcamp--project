import hashlib

m = hashlib.md5()
text = 'jaydeep peshwa'
m.update(text.encode('utf-8'))

print(m.hexdigest())