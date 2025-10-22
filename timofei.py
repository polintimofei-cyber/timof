# while menüü ja tekstitöötlus
# A)
text = ""
while True:
    print("1. Sisesta tekst")
    print("2. Kärbi servad (strip)")
    print("3. Eemalda topeltvahed kuni ühekordseks")
    print("4. Näita pikkust ilma tühikuteta")
    print("5. Välju")
    sisesta = int(input("Hello, this is a menu to remove spaces. Choose what you want to do(Kirjuta ainult number): "))
    if sisesta == 1:
        tekst = str(input("Sisesta tekst: "))
        text = tekst
        continue
    elif sisesta == 2:
        if text:
            strip = text.strip()
            text = strip
            print("Done, new text: ", text)
        else:
            print("Esmalt, sisestage tekst")
            continue
    elif sisesta == 3:
        if text:
            while "  " in text:
                text = text.replace("  ", " ")
                print("Sinu text: ", text)
        else:
            print("Esmalt, sisestage tekst")
            continue
    elif sisesta == 4:
        if text:
            print("Sinu text: ", text)
            continue
        else:
            print("Esmalt, sisestage tekst")
            continue
    elif sisesta == 5:
        print("Good bye!")
        break
    else:
        print(" INCORRECT NUMBER ")
        continue
#B)
while True:
    nimi = input("Sisesta nimi: ")
    if len(nimi) > 12:
        print("Too long nimi")
        continue
    elif len(nimi) < 4:
        print("Too small nimi")
        continue
    elif not nimi.isalnum():
        print("There's symbols in nimi")
        continue
    if " " in nimi:
        print("There's spaces in nimi")
    else:
        print("Correct nimi")
        break
   
#C)
def normaliseeri_nimi():
    while True:
        sisend = input("Sisesta nimi (ees-/perekonnanimi või ees-/keskmine-/perekonnanimi): ")
        puhastatud = " ".join(sisend.strip().split())
        osad = [osa.title() for osa in puhastatud.split()]
 
        if len(osad) < 2:
            print("Palun sisesta vähemalt ees- ja perekonnanimi.")
        else:
            normaliseeritud_nimi = " ".join(osad)
            print(normaliseeritud_nimi)
            return normaliseeritud_nimi
normaliseeri_nimi()


#for ja while tekstianalüüs
#A
text = input("Sisesta tekst: ")

text = text.strip()

cleaned = ""
prev_space = False

for ch in text:
    if ch.isalpha() or ch.isdigit():
        cleaned += ch
        prev_space = False
    elif ch in [' ', '\t', '\n']:
        if not prev_space:
            cleaned += ' '
            prev_space = True

print("Algne tekst:")
print(text)
print("Puhastatud tekst:")
print(cleaned)

#B
kokku_ridu = 0
tuhjad = 0
luhikesi = 0

while True:
    rida = input()
    if rida == "":
        break
    kokku_ridu += 1
    rida_stripped = rida.strip()
    if rida_stripped == "":
        tuhj = True
        tuhj_ridu += 1
    if len(rida_stripped) < 5:
        luhikesi += 1
    if rida_stripped == "":
        tuhj_ridu += 1

print("Kokku ridu:", kokku_ridu)
print("Tühje ridu:", tuhj_ridu)
print("Lühikesi ridu (<5 märki):", luhikesi)

#C
rida = input("Sisesta nimed komadega: ")

rida = rida.strip()

nimed = []
nimi = ""
i = 0
while i < len(rida):
    ch = rida[i]
    if ch == ",":
        nimi_stripped = nimi.strip()
        if nimi_stripped != "":
            nimed.append(nimi_stripped.title())
        nimi = ""
    else:
        nimi += ch
    i += 1

nimi_stripped = nimi.strip()
if nimi_stripped != "":
    nimed.append(nimi_stripped.title())

for n in nimed:
    print(f"Hello, {n}!")