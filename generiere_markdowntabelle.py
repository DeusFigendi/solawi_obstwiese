import json
import subprocess

def osmid2osmurl(i):
	return("https://www.openstreetmap.org/node/"+str(i)+"#map=19/52.00231/8.79719")
	
def osmid2qrurl(i):
	osm_url = osmid2osmurl(i)
	qr_filename = './qrcodes/'+str(i)+'.png'
	subprocess.run(["qrencode", "-o", qr_filename, osm_url])
	base64_process = subprocess.run(["base64", qr_filename], capture_output=True)
	base64string = 'data:image/png;base64,'+str(base64_process.stdout, 'utf-8').replace("\n","")
	return(qr_filename)


with open('./baumdaten.json','r') as baumdatei:
	baumdaten = json.load(baumdatei)
	
output_string =    "| URL         | Nummer | Gattung | Spezies | Notiz |"
output_string += "\n|-------------|--------|---------|---------|-------|"
for baum in baumdaten:
	output_string += "\n"+"| [![QR-Code zu OSM]("+osmid2qrurl(baum['osm_id'])+")]("+osmid2osmurl(baum['osm_id'])+") | "+str(baum['solawi_id'])+" | "+str(baum['genus'])+" | "+str(baum['species'])+" | "+str(baum['notiz'])+" | "
	
with open('./baumdaten.md','w') as baumdatei:
	baumdatei.write(output_string)
	
	
	

#	data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHsAAAB7AQMAAABuCW08AAAABlBMVEUAAAD///+l2Z/dAAAAAnRSTlP//8i138cAAAAJcEhZcwAACxIAAAsSAdLdfvwAAAF1SURBVEiJ1dW9jcUgDABgRxTpXhZAYg06VkoWyM8CYSU6rxGJBaCjQPE5L+/uSdfgK06nQynQVxDHNg7QtwX/GRLAgibjMQToZJCpTkgbGkLeyyDohdTulEeYxDD2eii1+wnMLp599HKgOlqTwxVvlgHnY0J9Pe8ENYDXCXXuYXiXoQEJNNhru9roZXBa8qgfzmxYOxlQOCasD+BE3me0IQeVyfjCn1gXGRC/81mo2SqSwenU6mi3tPe0ySDBMVrluY8KeRmcoPgAH2KCO9I25HJM5RhIj854GXCkGWF2Zu/jJoPkNDjynA++EDIgimtvtgAL6UUIyGfoIVSwd6RtyKQ2jBzmZ6QCKNynZrUwFeWFgNzUXFVFCIsQOEbgqtYRVJYBr+RUusK8h0Ebnjf7mOjo8FWGJvD84BLxNeroa+S0IFzDgydBgvs2iGB0V7deWRTDFAxP3C1EEgLP9VAHVKd7Zb0JVz4KUYmri14Gv/Kf+xP4AMJRXK7oXC4zAAAAAElFTkSuQmCC
#						  iVBORw0KGgoAAAANSUhEUgAAAHsAAAB7AQMAAABuCW08AAAABlBMVEUAAAD///+l2Z/dAAAAAnRS
#						  TlP//8i138cAAAAJcEhZcwAACxIAAAsSAdLdfvwAAAF1SURBVEiJ1dW9jcUgDABgRxTpXhZAYg06
#						  VkoWyM8CYSU6rxGJBaCjQPE5L+/uSdfgK06nQynQVxDHNg7QtwX/GRLAgibjMQToZJCpTkgbGkLe
#						  yyDohdTulEeYxDD2eii1+wnMLp599HKgOlqTwxVvlgHnY0J9Pe8ENYDXCXXuYXiXoQEJNNhru9ro
#						  ZXBa8qgfzmxYOxlQOCasD+BE3me0IQeVyfjCn1gXGRC/81mo2SqSwenU6mi3tPe0ySDBMVrluY8K
#						  eRmcoPgAH2KCO9I25HJM5RhIj854GXCkGWF2Zu/jJoPkNDjynA++EDIgimtvtgAL6UUIyGfoIVSw
#						  d6RtyKQ2jBzmZ6QCKNynZrUwFeWFgNzUXFVFCIsQOEbgqtYRVJYBr+RUusK8h0Ebnjf7mOjo8FWG
#						  JvD84BLxNeroa+S0IFzDgydBgvs2iGB0V7deWRTDFAxP3C1EEgLP9VAHVKd7Zb0JVz4KUYmri14G
#						  v/Kf+xP4AMJRXK7oXC4zAAAAAElFTkSuQmCC

# https://www.openstreetmap.org/?minlon=-0.489&minlat=51.28&maxlon=0.236&maxlat=51.686#map=9/51.4835/-0.1265
