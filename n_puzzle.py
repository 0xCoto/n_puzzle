# Fortosi tou built-in module random
import random

# Taxi katastasis
class State:
    # Vasiki sinartisi
    def __init__(self, nsize):
        # Orise to provlima n-puzzle, me n-size timi, tsize to sinoliko plithos ton komvon kai initial to goal state apo n

        self.nsize = nsize
        self.tsize = pow(self.nsize, 2)
        self.goal = list(range(1, self.tsize))
        self.goal.append(0)

    def printst(self, st):
        # Ektipose ti lista se morfi mitras

        # Trexe gia kathe dikti kai timi
        for (index, value) in enumerate(st):
            print(' %s ' % value, end=' ')
            
            # An o diktis vriskete se afto to range
            if index in [x for x in range(self.nsize - 1, self.tsize, self.nsize)]:
                print() #do nothing/break?
        print() 

    def getvalues(self, key):
        # Voithitiki sinartisi gia na pernis tis eleftheres kinisis se diafores thesis klidia sti mitra

        values = [1, -1, self.nsize, -self.nsize]
        valid = []
        for x in values:
            if 0 <= key + x < self.tsize:
                if x == 1 and key in range(self.nsize - 1, self.tsize, 
                        self.nsize):
                    continue
                if x == -1 and key in range(0, self.tsize, self.nsize):
                    continue
                valid.append(x)
        return valid

    def expand(self, st):
        # Paroxi tis listas ton epomenon dinaton katastaseon apo tin torini katastasi

        pexpands = {}
        for key in range(self.tsize):
            pexpands[key] = self.getvalues(key)
        pos = st.index(0)
        moves = pexpands[pos]
        expstates = []
        for mv in moves:
            nstate = st[:]
            (nstate[pos + mv], nstate[pos]) = (nstate[pos], nstate[pos + 
                    mv])
            expstates.append(nstate)
        return expstates

    def one_of_poss(self, st):
        # Epelekse mia apo tis dinates katastasis

        exp_sts = self.expand(st)
        rand_st = random.choice(exp_sts)
        return rand_st

    def start_state(self, seed=1000):
        # Kathorise tin arxiki katastasi tou provlimatos

        start_st = (self.goal)[:]
        for sts in range(seed):
            start_st = self.one_of_poss(start_st)
        return start_st

    def goal_reached(self, st):
        # Elenxos ean o stoxos epitefxthike i oxi

        return st == self.goal # epistrofi alithis i psevdis

    def manhattan_distance(self, st):
        # Ipologise tin apostasi manhattan tis ekastote katastasis

        mdist = 0
        
        # Gia kathe komvo
        for node in st:
            # An o komvos den ine 0
            if node != 0:
                gdist = abs(self.goal.index(node) - st.index(node))
                (jumps, steps) = (gdist // self.nsize, gdist % self.nsize)
                mdist += jumps + steps

        # Epestrepse tin apostasi manhattan
        return mdist

    def huristic_next_state(self, st):
        # Huristic function (kathorismos tis epomenis katastasis pou erxete kai xrisimopii tin methodo apostasis manhattan san ta huristics
        
        exp_sts = self.expand(st)
        mdists = []
        for st in exp_sts:
            mdists.append(self.manhattan_distance(st))

        # Taksinomise kata afksousa sira
        mdists.sort()
        short_path = mdists[0]
        if mdists.count(short_path) > 1:
            least_paths = [st for st in exp_sts if self.manhattan_distance(st) == short_path]
            return random.choice(least_paths)
        else:
            for st in exp_sts:
                if self.manhattan_distance(st) == short_path:
                    return st

    def solve_it(self, st):
        # Epilisi
        
        # Ean den exi epitefxthi o stoxos
        while not self.goal_reached(st):
            st = self.huristic_next_state(st)
            self.printst(st) # ektiposi

# An to trexis katefthian apo command-line
if __name__ == '__main__':
    print("[+] EPILITIS N-PUZZLE [+]\n")
    state = State(3)
    print("[*] ARXIKI KATASTASI: ")
    start = state.start_state(5)
    state.printst(start)
    print("[*] KATASTASI STOXOU: ")
    state.printst(state.goal)
    print("\n-----" )
    print("[!] Ekkinisi..."+"\n")
    state.printst(start)
    state.solve_it(start)
