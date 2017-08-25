from bs4 import BeautifulSoup
import requests, time, sys, os, mechanize

#dress id
dressID = '318036'
#dress size
size = "M"
#language
lng = "AR"
#your country ID (you can find it from the home page source code)
country = "47" #Jordan

#Setting up the browser
br = mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-agent', 'Chrome')]

#Filling up the welcome form that asks for your lang and country
br.open('https://www.modanisa.com/ar/')
br.select_form(nr=0)
br.form['lang'] = [lng,]
br.form['country'] = [country,]
br.submit()

try:
	while 1:

		html = br.open('https://www.modanisa.com/search/?q='+dressID).read()
		bsobj = BeautifulSoup(html, 'html.parser')
		sizeboxes = bsobj.find("div", {"class":"productSizeBoxes"},recursive=True).findAll("a", {"class":"size"})
		sizevals = [i.text for i in sizeboxes ]
		classes = sizeboxes[sizevals.index(size)]["class"]

		if 'disabled' not in classes:
			print "Available!"
			#system alert when the dress is available, you can stop teh sound and close the script by pressing ctrl+c
			while 1:
				os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % ( 0.5, 500))
				time.sleep(0.5)
		print "Still Unavailable."
		#refresh the page every 1 minute
		time.sleep(60)

except KeyboardInterrupt:
	sys.exit()