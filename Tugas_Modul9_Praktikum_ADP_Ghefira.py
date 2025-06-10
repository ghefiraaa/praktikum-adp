from termcolor import colored
import time
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")  #os.name: bawaan jika "nt" berarti untuk Windows

cake = [
    "      i  i  i     ",
    "   -------------",
    "   | H A P P Y |  ",
    " __|___________|__",
    "|                 |",
    "| B I R T H D A Y |",
    "|                 |",
    "~~~~~~~~~~~~~~~~~~~"
]

colors = ["red", "yellow", "green", "cyan", "magenta"]

for i in range(10):
    clear()
    for j in range(len(cake)):
        color = colors[(j+i) % len(colors)]
        print(colored(cake[j], color, attrs=["bold"]))  #attrs: atribut tambahan pada termcolor (seperti bold teks, garis bawah pada teks)
    time.sleep(1)

print(colored("\nHAPPY BIRTHDAY TO U!, Enjoy the new episodes in your season!", "magenta", attrs=["bold", "underline"]))