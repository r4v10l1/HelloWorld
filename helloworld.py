import time, sys, random
characters = ["q", "_\x9e", "©", "_®", "2", "_º", "³", "\x9d", "_3"]
orders = ["0", "1", "2", "2", "3", "4", "5", "3", "6", "2", "7", "8"]

def decode(text):
    if "_" in text:
        text = text.replace("_","")
        return chr(int(ord(text)/3.14159)*2+1)
    else:
        return chr(int(ord(text)/3.14159)*2+2)

def main():
    for x in orders:
        sys.stdout.write(decode(characters[int(x)]))
        sys.stdout.flush()
        time.sleep(float(f"0.{random.choice([3,4,5])}"))

main()
