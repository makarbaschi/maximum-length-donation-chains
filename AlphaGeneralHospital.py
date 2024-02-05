print('')
print('-'*5, 'Test', '-'*5)
print('')
print('')

print('input number of patients:')


N = int(input())
Alpha_Hospital = {}
for i in range (1,N+1) :
    Alpha_Hospital[i] = []

print('')
print('input blood groups:')

for i in range (1,N+1):
    patient_data = input().split()
    patient = int(patient_data[0])
    organ_donor = int(patient_data[1])
    Alpha_Hospital[i].append(patient)
    Alpha_Hospital[i].append(organ_donor)

def Can_Donate (donor , recipient) :
    """This function checks whether person A can donate
    to person B or not and returns the answer as a boolean 
    value true or false."""

    if donor == 100 :
        return True
    if donor == 101 :
        if recipient == 101 or recipient == 201 or recipient == 301 or recipient == 231 :
            return True 
        else : return False 
    if donor == 200 :
        if recipient == 200 or recipient == 201 or recipient == 230 or recipient == 231 :
            return True 
        else : return False 
    if donor == 201 :
        if recipient == 201 or recipient == 231 :
            return True 
        else : return False 
    if donor == 300 :
        if recipient == 300 or recipient == 301 or recipient == 230 or recipient == 231 :
            return True
        else : return False
    if donor == 301 :
        if recipient == 301 or recipient == 231 :
            return True 
        else : return False
    if donor == 230 :
        if recipient == 230 or recipient == 231 :
            return True 
        else : return False 
    if donor == 231 :
        if recipient == 231 :
            return True
        else : return False

def Generator (patients, id_donator) :
    PDL = [] # possible donation list
    for i in range (1,len(patients)+1) :
        donator = Alpha_Hospital[id_donator][1]
        giver = Alpha_Hospital[i][0]
        if Can_Donate (donator, giver) :
            if id_donator != i :
                generative = [id_donator, i]
                PDL.append(generative)
    return PDL

Alpha = {}
for i in range (1,N+1) :
    Alpha[i] = Generator(Alpha_Hospital, i)

def Validation (SomePatients):
    All_Pat = []
    for i in range (1, N+1):
        All_Pat.append(i)
    Valid_Patients = All_Pat
    Q = len (SomePatients)
    for i in range (Q):
        SomePatient = SomePatients[i]
        Valid_Patients.remove(SomePatient)
    return Valid_Patients

def next (chain) :
    new_chains = []
    new_chains.append(chain)

    Valid_Patients = Validation(chain)

    Donator_Index = len(chain) - 1
    Donator_ID = chain[Donator_Index]
    Donator = Alpha_Hospital[Donator_ID][1]

    for Giver_ID in Valid_Patients :
        thischain = chain
        Giver = Alpha_Hospital[Giver_ID][0]
        if Can_Donate(Donator, Giver):
            new = [Giver_ID]
            thischain = thischain + new
            new_chains.append(thischain)

    if len(new_chains) > 1 :
        new_chains.pop(0)

    return new_chains


def Create_Tree (chains):
    new_chains = []
    for chain in chains:
        new_chains = new_chains + next(chain)
    
    if new_chains == chains :
        return chains
    
    else :
        return Create_Tree(new_chains)

All_Chains = []
for i in range(1,N+1):
    All_Chains = All_Chains + Create_Tree(Alpha[i])

def Final_Checking (chain):
    Don_IND = len(chain) - 1
    Don_ID = chain[Don_IND]
    Giv_ID = chain[0]
    Don = Alpha_Hospital[Don_ID][1]
    Giv = Alpha_Hospital[Giv_ID][0]
    if Can_Donate(Don, Giv):
        new = [Giv_ID]
        chain = chain + new 
    return chain 

Modified_All_Chains = []
for chain in All_Chains:
    Modified_All_Chains.append(Final_Checking(chain))

Max_Length = 0 
for chain in Modified_All_Chains:
    if len(chain) > Max_Length :
        Max_Length = len(chain)

All_Max_Chains = []
for chain in Modified_All_Chains:
    if len(chain) == Max_Length:
        All_Max_Chains.append(chain)
Max_Chain_Example = All_Max_Chains[0]

def Show(L):
    txt = ''
    feix = len(L) - 1
    for i in range(len(L)):
        if i != feix :
            txt = txt + str(L[i]) + ' -> '
        else:
            txt = txt + str(L[i])
    return txt

print('')
print('')
print('-'*15)
print('length of longest chain:')
print(Max_Length)
print('')
print('')
print('-'*15)
print('longest chains:')
print('')
for chain in All_Max_Chains:
    print(Show(chain))