class Cpf:
    def __init__(self, documento):
        documento = str(documento)
        if self.cpf_Valido(documento):
            self.cpf = documento
        else:
            raise ValueError
        
    def __str__(self):
        return self.formatado_cpf()

    def cpf_Valido(self, documento):
        if len(documento) == 11:
            return True
        else:
            return False

    def formatado_cpf(self):
        fatia1 = self.cpf[:3]
        fatia2 = self.cpf[3:6]
        fatia3 = self.cpf[6:9]
        fatia4 = self.cpf[9:]
        return f"{fatia1}.{fatia2}.{fatia3}-{fatia4}"
