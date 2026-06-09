# Lab 6 — TCP Port Skener

Python program za skeniranje TCP portova koristeći ugrađeni `socket` modul.

## Kako pokrenuti
python port_scanner.py

## Primjer izlaza
C:\Users\korisnik\Desktop>python port_scanner.py 127.0.0.1 80
=============================================
       TCP PORT SKENER
=============================================

Odaberi mod:
  1 - Jedan host, raspon portova
  2 - Više hostova (Zadatak 3)

Unesi izbor (1 ili 2): 1
Početni port: 20
Završni port: 100
Unesi host (IP ili hostname): scanme.nmap.org

Skeniranje: scanme.nmap.org (45.33.32.156), portovi 20-100
---------------------------------------------
  [+] Port 22 (ssh) - OTVOREN
  [+] Port 80 (http) - OTVOREN
  Testiram port 100...
Otvoreni portovi na scanme.nmap.org:
  - 22 (SSH)
  - 80 (HTTP)
