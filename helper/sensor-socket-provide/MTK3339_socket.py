import gps
from IoT_Hackathon import DataProvider
import sys
import threading

session = None #seting the global variable

class GPSPoller(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)

    global session #bring it in scope
    session = gps.gps("localhost", "2947")
    session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

    self.running = True #setting the thread running to true

  def run(self):
    global session
    while self.running:
      session.next() #this will continue to loop and grab EACH set of gpsd info to clear the buffer


def mtk3339Read():
    global session

    mtk3339Data = {'latitude'  : session.fix.latitude,
                   'longitude' : session.fix.longitude,
                   'utc'       : session.utc,
                   'altitude'  : session.fix.altitude,
                   'eps'       : session.fix.eps,
                   'epx'       : session.fix.epx,
                   'epv'       : session.fix.epv,
                   'ept'       : session.fix.ept,
                   'speed'     : session.fix.speed,
                   'climb'     : session.fix.climb,
                   'track'     : session.fix.track,
                   'mode'      : session.fix.mode}

    return mtk3339Data


if __name__ == '__main__':


    socket_address = '/tmp/mtk3339'

    if len(sys.argv) == 2:
        socket_address = sys.argv[1]

    gpsp = GPSPoller()
    gpsp.start()
    DataProvider.start(mtk3339Read, socket_address)

    gpsp.running = False
    gpsp.join()
    session.close()
    session = None
