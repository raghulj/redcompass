from xml.dom import minidom
from xml.dom.minidom import parseString
from urllib.parse import urlencode
import urllib

# make a string with the request type in it:
method = "POST"
url = "http://www.opencellid.org/cell/getMeasures?key=b33b3a39-a4ba-40f5-9ce0-8ba6e34dbba2"
# create a handler. you can specify different handlers here (file uploads etc)
# but we go for the default
handler = urllib.request.HTTPHandler()
# create an openerdirector instance
opener = urllib.request.build_opener(handler)
# build a request
user_agent = 'Mozilla/5.0 (compatible; Chrome/22.0.1229.94; Windows NT)'
# &mcc=260&mnc=2&lac=10250&cellid=26511&limit=10&offset=1


def get_coordinates(mcc, mnc,lac, cellid):
    data_params = urllib.parse.urlencode({'mcc' : mcc, 'mnc'  : mnc, 'lac':lac, 'cellid':cellid, 'limit' :'10'})
    binary_data = data_params.encode('utf-8')
    request = urllib.request.Request(url, data=binary_data )
    request.get_method = lambda: method
    # try it; don't forget to catch the result
    #try:
    connection = opener.open(request)
    #except urllib2.HTTPError,e:
    #connection = e

    # check. Substitute with appropriate HTTP code.
    if connection.code == 200:
       data = connection.read()
       if data:
           xmldoc = parseString(data)
           itemlist = xmldoc.getElementsByTagName('cell') 
           lat = itemlist[0].attributes['lat'].value
           lon = itemlist[0].attributes['lon'].value
           return [lat, lon]
    else:
        # handle the error case. connection.read() will still contain data
        # if any was returned, but it probably won't be of any use
        d= "error"


if __name__ == '__main__':
    get_coordinates(260, 2,10250,26511)
    

