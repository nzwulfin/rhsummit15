#!/usr/bin/python
import xmlrpclib, subprocess, getpass, hashlib
from xml.dom import minidom
import yaml
import sys

if len(sys.argv) > 1:
	config = open(sys.argv[1], "r")
else:
	# Read config file YAML for cron operations
	config = open("/root/.scan_config", "r")

options = yaml.safe_load(config)

# Satellite host options
SATELLITE_URL = "https://ep-sat01.lab.dlt.com/rpc/api"
# To interactively set login/pass uncomment the following
# SATELLITE_LOGIN = raw_input("Enter the org admin username: ")
# SATELLITE_PASSWORD = getpass.getpass(prompt='Enter the org admin password: ')
SATELLITE_LOGIN = options["login"]
SATELLITE_PASSWORD = options["pass"]

# Set system name to be scanned, will discover ID from Satellite
# systemList = raw_input("Enter the name of the system to scan: ")
systemList = options["hostname"]

# Set the XCCDF checklist and additional options for scanner
# xccdf = "/usr/share/xml/scap/ssg/content/ssg-rhel6-ds.xml"
xccdf = options["xccdf"]

# oscap_opts = "--profile xccdf_org.ssgproject.content_profile_CS2"
oscap_opts = options["oscap_opts"] or ""

# Set up initial XMLRPC handle
client=xmlrpclib.Server(SATELLITE_URL, verbose=0)

# Login to Satellite and create session or raise API error
try:
	key = client.auth.login(SATELLITE_LOGIN, SATELLITE_PASSWORD)
	print 'Logged into Satellite'
except Exception, detail:
	print 'Got API login error: ', detail
	exit()

# This is the try that does the heavy lifting.
# All work to be done on Satellite should be done here
# Any errors are trapped and raised and the Satellite session is closed

system = None
try:
	for hostname in systemList:
		system = client.system.getId(key, hostname)
		try:
			client.system.scap.scheduleXccdfScan(key, system[0]["id"], xccdf, oscap_opts)
			print 'Scan scheduled for ', system[0]["name"]
		except Exception, detail:
			print 'Got API error: ', detail
			exit()
finally:
	client.auth.logout(key)

