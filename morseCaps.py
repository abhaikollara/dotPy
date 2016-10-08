#Program to blink morse code on Caps Lock LED for a given text

import sys
import time
import os

morseCodes = {'A':"01",'B':"1000",'C':"1010",'D':"100",'E':"0",'F':"0010",'G':"110",'H':"0000",'I':"00",'J':"0111",'K':"101",'L':"0100",'M':"11",'N':"10",'O':"111",'P':"0110",'Q':"1101",'R':"010",'S':"000",'T':"1",'U':"001",'V':"0001",'W':"011",'X':"1001",'Y':"1011",'Z':"1100"}

def morseOfchar(ch):
	ch=str(ch)
	for x in morseCodes[ch]:
		if x=='0':
			# sys.stdout.write(u"\u30FB")
			os.system("setleds +caps")
			time.sleep(0.1)
			os.system("setleds -caps")
			time.sleep(0.1)
		else:
			# sys.stdout.write(u"\u30FC")
			os.system("setleds +caps")
			time.sleep(0.3)
			os.system("setleds -caps")
			time.sleep(0.1)


def morseOfWord(word):
	word=str(word).upper()
	for x in word:
		morseOfchar(x)
		time.sleep(0.3)
		# sys.stdout.write("  ")
	print

def morseOfString(string):
	string=str(string).split()
	for x in string:
		morseOfWord(x)
		time.sleep(0.7)
# morseOfWord("sos")

message=raw_input("Enter msg : ")


morseOfString(str(message))