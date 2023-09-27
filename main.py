# Szilágyi Bence
#1.
print("1.")

def Beolvas(fileName):
    return list(open(fileName))
lorem = Beolvas("lorem.txt")


# megszámuljuk soronként hány 'a' betű van és vesszük a szummáját
aBetu_db = sum(line.count('a') for line in lorem)
print(f"1.3 Ennyi 'a' betű van a szövegben {aBetu_db}")

# összes sort ' '-enként tördeljük és az ujbol kepzett listaknak a hosszát szummázzuk
szavak_db = sum(len(line.split(' ')) for line in lorem)
print(f"1.4 Ennyi szóbol áll: {szavak_db}")

mondat_db = sum(line.count('.') for line in lorem)# feltételezzük hogy pontokat csak a mondat végén használunk akkor megszámoljuk minden beolvasott sor '.' db szamat
print(f"1.4 Ennyi mondatból áll: {mondat_db}")

xSzavak = []# végigmegyünk az összes sornak a szaván és ha x-et tartalmaz hozzáadjuk a listánkhoz
for line in lorem:
    for word in line.split(' '):
        if 'x' in word:
            xSzavak.append(word)
# xSzavak2 =[word for word in [x.split(' ') for x in lorem] if 'x' in word] # nem mukodik csak probalkoztam
print(f"1.5 'x' karaktert tartalmazó szavak: '{', '.join(xSzavak)}'")

print(f"1.6 'x' karaktert tartalmazó szavak száma: {len(xSzavak)}")

count_words = 0 #végigmegyünk az összes sor szavain ha megtalaljuk az 'x'-et tartalmazó szavunkat kiírjuk, illetve minden szónál megnöveljük a számláló változónkat
stop_loop = False
for line in lorem:
    for word in line.split(' '):
        count_words += 1
        if 'x' in word:
            print(f"1.7 első 'x' karaktert tartalmazó szó, db-ik szó: {word}, {count_words}-ik")
            stop_loop = True
            break
    if stop_loop:
        break


#2.
print("\n2.")

class Dante:# 2.1
    def __init__(self, year, month, day):# 2.2
        self.year = year
        self.month = month
        self.day = day

    def szokoEv(self):# 2.3
        #ha 00-ra végződik vagyis osztható 100-al vagy oszthato 400-al akkor szökőév
        if (self.year % 400 == 0) and (self.year % 100 == 0):
            return ("2.3 {0} szökőév".format(self.year))

        # ha nem oszthato 100-al de 4-el igen akkor is szökőév
        elif (self.year % 4 == 0) and (self.year % 100 != 0):
            return ("2.3 {0} szökőév".format(self.year))

        # ha egyikkel sem
        else:
            return ("2.3 {0} nem szökőév".format(self.year))


today = Dante(2000,1,1) #2.2
print(today.szokoEv())
