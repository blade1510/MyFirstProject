# -*- coding: iso-8859-1 -*-

import datetime

if __name__ == "__main__":
	retry = 'y'
	while retry == 'y' or retry == 'Y':
		print "\n\n1: Arbeitszeit berechnen"
		print u"2: Wie lange muss ich noch arbeiten für Sollzeit = 8h bei Pause = 45min"
		wahl = int(raw_input("Wahl: "),10)
		
		if wahl == 1:
			anf = 	int(raw_input("\nStart at: "),10)
			end = 	int(raw_input("End at:   "),10)
			pause = int(raw_input("Break:    "),10)
			
			erg = ((end/100*60 + end%100)*60 - (anf/100*60 + anf%100)*60 - (pause/100*60 + pause%100)*60) / 60.0/60.0
			print "Reine Arbeitszeit: %.2f" % erg
		
		if wahl == 2:
			anf = 	int(raw_input("\nStart at: "),10)
			anfInSec = (anf/100*60 + anf%100)*60
			pause = 45
			pauseInSec = (pause/100*60 + pause%100)*60
			sollInH = 8			
			sollInSec = sollInH * 60 * 60
			endInSec = anfInSec + sollInSec + pauseInSec
			
			ans = endInSec / 60.0
			SecInH = ans / 60			
			SecInMin = ans % 60
			print "Heutiges Arbeitsende: %d:%d Uhr" % (SecInH, SecInMin)
	
		retry = raw_input("Press 'y' or 'Y' to retry: ")