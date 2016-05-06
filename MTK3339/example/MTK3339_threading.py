#! /usr/bin/python
# Written by Dan Mandle http://dan.mandle.me September 2012
# License: GPL 2.0

import os
import gps
import time
import threading

session = None #seting the global variable

os.system('clear') #clear the terminal (optional)

class GpsPoller(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    global session #bring it in scope

    session = gps.gps("localhost", "2947")
    session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

    self.current_value = None
    self.running = True #setting the thread running to true

  def run(self):
    global session
    while self.running:
      session.next() #this will continue to loop and grab EACH set of gpsd info to clear the buffer

if __name__ == '__main__':
  gpsp = GpsPoller() # create the thread
  try:
    gpsp.start() # start it up
    while True:
      #It may take a second or two to get good data
      #print gpsd.fix.latitude,', ',gpsd.fix.longitude,'  Time: ',gpsd.utc

      os.system('clear')

      print
      print ' GPS reading'
      print '----------------------------------------'
      print 'latitude    ' , session.fix.latitude
      print 'longitude   ' , session.fix.longitude
      print 'time utc    ' , session.utc,' + ', session.fix.time
      print 'altitude (m)' , session.fix.altitude
      print 'eps         ' , session.fix.eps
      print 'epx         ' , session.fix.epx
      print 'epv         ' , session.fix.epv
      print 'ept         ' , session.fix.ept
      print 'speed (m/s) ' , session.fix.speed
      print 'climb       ' , session.fix.climb
      print 'track       ' , session.fix.track
      print 'mode        ' , session.fix.mode
      print
      print 'sats        ' , session.satellites

      time.sleep(0.2) #set to whatever

  except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
    print "\nKilling Thread..."
    gpsp.running = False
    gpsp.join() # wait for the thread to finish what it's doing
  print "Done.\nExiting."
