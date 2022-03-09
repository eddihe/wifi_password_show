#! python3
import subprocess
import re
import sys

wifi_profiles = subprocess.run(['netsh','wlan','show','profiles'], capture_output=True)
#print(wifi_profiles.stdout.strip())
for n in wifi_profiles.stdout.decode().strip().split('Profile'):
    search = re.search(r':\s([a-zA-Z0-9_-]+)',n)
    if search:
        wifi_wir = subprocess.run(['netsh','wlan','show','profiles',search[1],'key=clear'], capture_output=True)
        text = wifi_wir.stdout.decode().strip()
        search2 = re.search(r'Key Content\s*:\s(\w+)', text)
        search3 = re.search(r"""SSID name\s*:\s\"(\w+)\"""", text)
        print(f"This is SSID:{str(search3[1])}\nThis is password of the SSID: {str(search2[1])}")



