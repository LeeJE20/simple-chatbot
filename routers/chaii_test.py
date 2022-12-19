from khaiii import KhaiiiApi
api = KhaiiiApi()

try:
    for word in api.analyze('안녕, 세상.'):
        print(word)
except Exception:
    print(Exception)
