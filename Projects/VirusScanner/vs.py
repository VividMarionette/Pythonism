
virus_files = [ "wannacry.exe", "lockbit.exe", "mirai", "payload.exe", "trojan.exe", "virus.exe", "trojan.bat", "malware.py"]

file = input("Enter file name source: ")

if file in virus_files:
  print("Threat Detected")

else:
  print("File safe")
