# Content for Summit talk

This repo contains the various examples from the Summit
presentation.

* API scanning scripts
* RPM spec file
* XCCDF from POODLE OVAL

## API scanning scripts
These use the Satellite API to schedule a scan via cron or
some other automation tool using a config file.  This config
file will contain a user / pass combo for your Satellite
server, so be sure to limit the perms.

## RPM spec file
This file will build a RPM suitable for deploying the RHSA
[OVAL] (http://www.redhat.com/security/data/oval/ )and [XCCDF] (http://www.redhat.com/security/data/metrics/com.redhat.rhsa-all.xccdf.xml)
content published by Red Hat

## XCCDF from POODLE and Shellshock OVAL
Generated using eSCAPe from the published
Red Hat OVAL file for RHSA-2014:1653-00 and RHSA-2014:1293-00.  eSCAPe can read the
published OVAL file and create an appropriate XCCDF file that
can be used by Satellite for individual vulnerability scans.
