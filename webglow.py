#Google Analytics to PiGlow LEDS
from piglow import PiGlow
import time
import urllib2
piglow = PiGlow()
#Test
i = 0
while (i < 2):
	piglow.arm1(127)
	time.sleep(0.1)
	piglow.arm1(0)
	piglow.arm2(127)
	time.sleep(0.1)
	piglow.arm2(000)
	piglow.arm3(127)
	time.sleep(0.1)
	piglow.arm3(0)
	#Test Completed
	i = i+1

while True:
	response = urllib2.urlopen('http://ryanteck.org.uk/nginx_status')
	html = response.read()
	data = html.split('\n')
	active = data[0].split(":")
	count = active[1]
	count = int(count) -1;
	print(count)
	
	if(count ==0):
		piglow.all(0)

