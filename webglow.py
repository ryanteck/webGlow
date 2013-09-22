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
	#top leg
	if(count >=1):
		piglow.led(6,127)
	if(count >=2):
		piglow.led(5,127)
	if(count >=3):
		piglow.led(4,127)
	if(count >=4):
		piglow.led(3,127)
	if(count >=5):
		piglow.led(2,127)
	if(count >=6):
		piglow.led(1,127)
	#bottom leg
	if(count >=7):
		piglow.led(12,127)
	if(count >=8):
		piglow.led(11,127)
	if(count >=9):
		piglow.led(10,127)
	if(count >=10):
		piglow.led(9,127)
	if(count >=11):
		piglow.led(8,127)
	if(count >=12):
		piglow.led(7,127)
	#rightleg
	if(count >=13):
		piglow.led(18,127)
	if(count >=14):
		piglow.led(17,127)
	if(count >=15):
		piglow.led(16,127)
	if(count >=16):
		piglow.led(15,127)
	if(count >=17):
		piglow.led(14,127)
	if(count >=18):
		piglow.led(13,127)



	for x in range(count, 18):
		#top leg
		if(x ==1):
			piglow.led(6,0)
		if(x ==2):
			piglow.led(5,0)
		if(x ==3):
			piglow.led(4,0)
		if(x ==4):
			piglow.led(3,0)
		if(x ==5):
			piglow.led(2,0)
		if(x ==6):
			piglow.led(1,0)
		#bottom leg
		if(x ==7):
			piglow.led(12,0)
		if(x ==8):
			piglow.led(11,0)
		if(x ==9):
			piglow.led(10,0)
		if(x ==10):
			piglow.led(9,0)
		if(x ==11):
			piglow.led(8,0)
		if(x ==12):
			piglow.led(7,0)
		#rightleg
		if(x ==13):
			piglow.led(18,0)
		if(x ==14):
			piglow.led(17,0)
		if(x ==15):
			piglow.led(16,0)
		if(x ==16):
			piglow.led(15,0)
		if(x ==17):
			piglow.led(14,0)
		if(x ==18):
			piglow.led(13,0)

	
