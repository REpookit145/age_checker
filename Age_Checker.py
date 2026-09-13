import subprocess
import sys
 
# Installiert pyfiglet automatisch, falls es noch nicht da ist
try:
    import pyfiglet
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyfiglet"])
    import pyfiglet
 
def rainbow_text(text):
    # ANSI 256-color codes that go through the rainbow
    colors = [196, 202, 208, 220, 226, 118, 46, 51, 21, 93, 165]
    colored = ""
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        colored += f"\033[38;5;{color}m{char}"
    colored += "\033[0m"  # Farbe am Ende zuruecksetzen
    return colored
 
# Cooler ASCII-Art Titel
banner = pyfiglet.figlet_format("AGE CHECK")
for line in banner.split("\n"):
    print(rainbow_text(line))
 
age = int(input("Please enter your age: "))
 
if age < 10:
    print("Kiddo")
elif age < 18:
    print("Underage")
else:
    print("Adult")

input("\nDruecke Enter zum Beenden...")
