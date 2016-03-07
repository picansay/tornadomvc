
import glob
app_urls_list = glob.glob("apps/*/urls.py")
print app_urls_list


for urls in app_urls_list:
    print urls
    urls = urls.replace('/','.')[0:-3]
    print urls
    m = __import__(urls)
    print m
