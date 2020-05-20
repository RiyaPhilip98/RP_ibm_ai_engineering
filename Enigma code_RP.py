# small program to create a simple enigma machine
#by Riya Philip

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


class Rotor():
    #when all the variables are set to starting position
    position = 'A'
    def __init__(self, configuration):
        self.initial_config = configuration
        self.connections = configuration
        self.config1 = dict(zip(alphabet, configuration))
        self.config2 = dict(zip(configuration, alphabet))
        self.position = 0
        self.revolutions = 0
        # initial position = self.position
        
        
    def initial_position(self, position):
        self.position = position
        
    def nextStep(self):
        return True if self.nextStep_position == self.position else False
    
    def indent(self):
        nextStep = self.nextStep()
        self.position = alphabet[(alphabet.index(self.position) + 1) % 26]
        if turnover:
            return True
        else:
            return False

    def rotate(self, steps):
        self.connections = self.connections[steps:] + self.connections[:steps]
        self.config1 = dict(zip(alphabet, self.connections))
        self.config2 = dict(zip(self.connections, alphabet))
        self.position += steps
        if self.position >= 26:
            self.revolutions = self.position / 26 #variable
            self.position = self.position % 26

    def reset_rotor(self):
        self.connections = self.initial_config
        self.config1 = dict(zip(alphabet, self.initial_config))
        self.config2 = dict(zip(self.initial_config, alphabet))
        position = 0
        revolutions = 0

    def encrypt(self, character):
        return self.config1[character]

    def decrypt(self, character):
        return self.config2[character]
    
class Reflector():
    def __init__(self, configuration):
        self.config = dict(zip(alphabet, configuration))
        
    def reflect(self, character):
        return self.config[character]
       
class Machine():
    def __init__(self, rotors=None, reflector=None):#, plug_board=None):
        self.rotors = rotors
        self.reflector = reflector
        #for pair in plug_board:
            #self.plug_board[pair[0]], self.plug_board[pair[1]] = pair[1], pair[0]
            
    def set_rotors(self, positions):
        if len(positions) != len(self.rotors):
            print 'Error: rotor settings do not match with number of rotors' 
        else:
         return

    def reset(self):
        for rotor in self.rotors:
            rotor.reset_rotor()
    
    def encipher(self, string):
        answer = ""
        for x in string:
            if x in alphabet: #spaces
                self.rotors[0].rotate(1)
                self.rotors[1].rotate(rotors[0].revolutions) #rotate rotor 2 depending on rotation of rotor 1
                self.rotors[0].revolutions = 0
                self.rotors[2].rotate(rotors[1].revolutions) #rotate rotor 3 depending on rotation of rotor 2
                self.rotors[1].revolutions = 0
                x = self.rotors[0].encrypt(x)
                x = self.rotors[1].encrypt(x)
                x = self.rotors[2].encrypt(x)
                x = self.reflector.reflect(x)
                x = self.rotors[2].decrypt(x)
                x = self.rotors[1].decrypt(x)
                x = self.rotors[0].decrypt(x)
            answer += x
        return answer
            
rotor1 = Rotor('ESOVPZJAYQUIRHXLNFTGKDCMWB')
#print rotor1.encrypt("A") #E
#rotor1.rotate(3)
#print rotor1.encrypt("A") #V
#rotor1.rotate(3)
#print rotor1.encrypt("B") #A
rotor2 = Rotor('AJDKSIRUXBLHWTMCQGZNPYFVOE')
rotor3 = Rotor('VZBRGITYUPSDNHLXAWMJQOFECK')



rotors=[rotor1, rotor2, rotor3] #'J', 'G'), #'E', 'M'),#'Z', 'Y')]

reflector = Reflector('YRUHQSLDPXNGOKMIEBFZCWVJAT')
plug_board = [('D', 'N'), ('G', 'R'), ('I', 'S'), ('K', 'C'), ('Q', 'X'), ('T', 'M'), ('P', 'V'), ('H', 'Y'), ('F', 'W'), ('B', 'J')]

machine = Machine(rotors, reflector)#, plug_board)


print machine.rotors[0].encrypt("A")
print machine.encipher("IBOUGHTFLOWERSFROMTHEFLOWERSHOP")
print machine.rotors[0].encrypt("A")
machine.reset()
print machine.rotors[0].encrypt("A")
print machine.encipher("YAFBUWZWMBQRXTMQEXHPPSPLLPMJOQA")

