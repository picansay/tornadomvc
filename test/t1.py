
m = __import__("t2")
print m
print m.add(1)


m = __import__("apps.demo")
print m
print m.demo
print m.demo.urls
urls = m.demo.urls.urls_suffix
print urls,type(urls)
