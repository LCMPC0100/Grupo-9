class MiniCPU:
    def __init__(self):
        self.memoria = [0] * 256
        self.registradores = [0] * 4
        self.pc = 0
        self.zf = 0
        self.esta_executando = True
        self.ciclo_atual = 0

    def fetch(self):
        if self.pc + 2 >= 256:
            self.esta_executando = False
            return 0, 0, 0
        
        opcode = self.memoria[self.pc]
        operando_a = self.memoria[self.pc + 1]
        operando_b = self.memoria[self.pc + 2]
        self.pc += 3
        
        return opcode, operando_a, operando_b



   