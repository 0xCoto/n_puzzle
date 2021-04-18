# Trexe me Python 3 (oxi v2)

# Fortosi tou built-in module random
import random
# Fortosi sleep gia delays
from time import sleep

# Taxi katastasisn_megethos
class State:
    # Vasiki sinartisi
    def __init__(self, n_megethos):
        # Orise to provlima n-puzzle, me n-size timi, t_megethos to sinoliko plithos ton komvon kai initial to stoxos state apo n

        self.n_megethos = n_megethos
        self.t_megethos = pow(self.n_megethos, 2)
        self.stoxos = list(range(1, self.t_megethos))
        self.stoxos.append(0)

    def ektiposi_vima(self, st):
        # Ektipose ti lista se morfi mitras

        # Trexe gia kathe dikti kai timi
        for (index, value) in enumerate(st):
            print(" %s " % value, end=" ")
            sleep(0.1)
            
            # An o diktis vriskete se afto to range
            if index in [x for x in range(self.n_megethos - 1, self.t_megethos, self.n_megethos)]:
                print()
        print() 

    def fetch_times(self, key):
        # Voithitiki sinartisi gia na pernis tis eleftheres kinisis se diafores thesis klidia sti mitra

        values = [1, -1, self.n_megethos, -self.n_megethos]
        egiro = []
        for x in values:
            if 0 <= key + x < self.t_megethos:
                if x == 1 and key in range(self.n_megethos - 1, self.t_megethos, 
                        self.n_megethos):
                    continue
                if x == -1 and key in range(0, self.t_megethos, self.n_megethos):
                    continue
                egiro.append(x)
        return egiro

    def expand(self, st):
        # Paroxi tis listas ton epomenon dinaton katastaseon apo tin torini katastasi

        pexpands = {}
        for key in range(self.t_megethos):
            pexpands[key] = self.fetch_times(key)
        pos = st.index(0)
        kinisis = pexpands[pos]
        expstates = []
        for mv in kinisis:
            n_katastasi = st[:]
            (n_katastasi[pos + mv], n_katastasi[pos]) = (n_katastasi[pos], n_katastasi[pos + mv])
            expstates.append(n_katastasi)
        return expstates

    def one_of_poss(self, st):
        # Epelekse mia apo tis dinates katastasis

        exp_sts = self.expand(st)
        rand_st = random.choice(exp_sts)
        return rand_st

    def start_vimaate(self, seed=1000):
        # Kathorise tin arxiki katastasi tou provlimatos

        start_vima = (self.stoxos)[:]
        for sts in range(seed):
            start_vima = self.one_of_poss(start_vima)
        return start_vima

    def stoxos_reached(self, st):
        # Elenxos ean o stoxos epitefxthike i oxi

        return st == self.stoxos # epistrofi alithis i psevdis

    def manhattan_distance(self, st):
        # Ipologise tin apostasi Manhattan tis ekastote katastasis

        manhattan_apostasi = 0
        
        # Gia kathe komvo
        for node in st:
            # An o komvos den ine 0
            if node != 0:
                gdist = abs(self.stoxos.index(node) - st.index(node))
                (jumps, steps) = (gdist // self.n_megethos, gdist % self.n_megethos)
                manhattan_apostasi += jumps + steps

        # Epestrepse tin apostasi manhattan
        return manhattan_apostasi

    def huristic_next_state(self, st):
        # Huristic function (kathorismos tis epomenis katastasis pou erxete kai xrisimopii tin methodo apostasis Manhattan os ta huristics). I methodos anazitisis ine AST (A* search, me Manhattan distance heuristic) 
        
        exp_sts = self.expand(st)
        manhattan_apostasis = []
        for st in exp_sts:
            manhattan_apostasis.append(self.manhattan_distance(st))

        # Taksinomise kata afksousa sira
        manhattan_apostasis.sort()
        short_path = manhattan_apostasis[0]
        if manhattan_apostasis.count(short_path) > 1:
            elaxista_monopatia = [st for st in exp_sts if self.manhattan_distance(st) == short_path]
            return random.choice(elaxista_monopatia)
        else:
            for st in exp_sts:
                if self.manhattan_distance(st) == short_path:
                    return st

    def epilisi(self, st):
        # Epilisi
        
        # Ean den exi epitefxthi o stoxos
        while not self.stoxos_reached(st):
            st = self.huristic_next_state(st)
            self.ektiposi_vima(st) # ektiposi

# -------------------
# Kalesma sinartiseon
print("[+] EPILITIS N-PUZZLE [+]\n")
sleep(2)
state = State(3)
print("[*] ARXIKI KATASTASI: ")
sleep(1)
start = state.start_vimaate(5)
state.ektiposi_vima(start)
sleep(2)
print("[*] KATASTASI STOXOU: ")
sleep(1)
state.ektiposi_vima(state.stoxos)
sleep(2)
print("\n---------------")
sleep(1)
print("[!] Ekkinisi..."+"\n")
sleep(2)
state.ektiposi_vima(start)
state.epilisi(start)
