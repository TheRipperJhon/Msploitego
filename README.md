**msploitego - The Pentesting suite for Maltego**
=================================================

![maltegosnapshot01](https://user-images.githubusercontent.com/9602322/40849078-f941f302-658e-11e8-83b1-62aea49c5b65.png)

![maltegosnapshot02a](https://user-images.githubusercontent.com/9602322/40849101-0abae328-658f-11e8-976a-25a9c70498e6.png)

![maltegosnapshot03a](https://user-images.githubusercontent.com/9602322/40849110-109aa79c-658f-11e8-92fc-75631c49c2a6.png)

THIS IS A BETA RELEASE, please be nice and report any issues

msploitego leverages the data gathered in a Metasploit database by enumerating and creating specific entities for services.  Services like samba, smtp, snmp, http have transforms to enumerate even further.  Entities can either be loaded from a Metasploit XML file or taken directly from the Postgres msf database

**I am open to hearing suggestions for new transforms and enhancements!!!**

Requirements
============
- Python 2.7
- Has only been tested on Kali Linux
- software installations
  - Metasploit Framework
  - nmap
  - enum4linux
  - snmp-check
  - nikto
  - exploitdb

Installation
============
- In Maltego import config from msploitego/src/msploitego/resources/maltego/msploitego.mtz
- checkout and update the transform path inside Maltego
    - easiest way would be to create a symbolic link to the transforms directory in /root/)
    - ln -s /path/to/your/msploitego/src/msploitego/transforms /root/

General Use
===========
Using exported Metasploit xml file
----------------------------------
- run a db_nmap scan in metatasploit, or import a previous scan
  - msf> db_nmap -vvvv -T5 -A -sS -ST -Pn <target>
  - msf> db_import /path/to/your/nmapfile.xml
  
  - export the database to an xml file
  - msf> db_export -f xml /path/to/your/output.xml

  - In Maltego drag a MetasploitDBXML entity onto the graph.
  - Update the entity with the path to your metasploit database file.
  - run the MetasploitDB transform to enumerate hosts.
  - from there several transforms are available to enumerate services, vulnerabilities stored in the metasploit DB
- This method is not recommended due to performance constraints.  If the XML file is large then running transforms will consume a lot of memory

Using Postgres(recommended!)
--------------
- drag and drop a Postgresql DB entity onto the canvas, enter DB details.
- run the Postgresql transforms directly against a running DB

Recommendations
===============
- Start by beefing up your Metasploit DB
    - look at msploitstarter.sh in the scripts directory.  It's run nmap and then tons of auxiliary modules to fatten up your Metasploit DB.
    - run a detailed nmap scan.  i.e. db_nmap -vvvv -sS -sV -sU -A -T5 1.1.1.1/24
    - Import results from Nessus or OpenVAS into Metasploit and use the Enum Vulnerabilities transform. 
    - Run the auxiliary/crawler/msfcrawler on all http/https ports.  This will gather useful data.
- Run **nikto** scan with xml output then enter the full path filename in the 'Nikto File' field. Run the Nikto parser to enumerate.

TODO's
======
- Connect directly to the postgres database - **BETA**
- Much, much, much more tranforms for actions on generated entities.


