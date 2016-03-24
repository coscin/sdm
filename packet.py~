
import os, logging, logging.config, subprocess, struct, time, json
from scapy.all import *

coscin_config = {}
switch = None

def determine_rtt():
  rtt = []
  for ah in coscin_config["alternate_hosts"][switch]:
    util = 255      # Default to max
    try:
      response = subprocess.check_output("ping -c 5 "+ah, shell=True)
      match = re.search("min/avg/max/mdev = ([\d.]+)/([\d.]+)", response)
      if match:
        util = int(float(match.group(2)))
        if util > 255:
          util = 255
    # If ping bombs out, default to max rtt
    except subprocess.CalledProcessError:
      pass
    except:
      logging.error("Unexpected error")
      raise
    rtt.append(util)
  return rtt 

def gen_report_packet():
  hdr = Ether(type=0x808, dst="ff:ff:ff:ff:ff:ff") 
  rtt = determine_rtt()
  logging.info("Calculated Roundtrip Times: "+str(rtt))
  data = struct.pack("BBB",rtt[0],rtt[1],rtt[2])
  pkt = hdr/Raw(data)
  try:
    sendp(pkt, iface="eth1", verbose=False)
  except:
    # Don't go to ridiculous lengths to send the utilization packet.  Just error.  
    logging.error("Error sending utilization packet")

if __name__ == "__main__":
  logging.config.fileConfig("coscin_log.conf")
  f = open(os.getenv("COSCIN_CFG_FILE", "coscin_gates_testbed.json"), "r")
  coscin_config = json.load(f)  
  switch = os.getenv("COSCIN_SWITCH", "ithaca")
  while True:
    gen_report_packet()
    time.sleep(coscin_config["probe_interval"])
