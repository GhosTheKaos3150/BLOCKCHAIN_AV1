from hashlib import sha256
from datetime import datetime


def validate_hash(block_hash):
    # Valida se o HASH está correto
    return block_hash.startswith('000')


class Block:

    block_hash = ""

    def __init__(self, index, transaction, prev_hash, nonce = 1, supress=False):

        self.index = index
        self.prev_hash = prev_hash
        self.timestamp = datetime.now().timestamp()
        self.transaction = transaction
        self.nonce = nonce  

        while not validate_hash(self.block_hash):

            encript = f"{self.index}:{self.transaction}:{self.timestamp}:{self.prev_hash}:{self.nonce}"   
            self.block_hash = sha256(encript.encode()).hexdigest()
            self.nonce += 1

        if not supress:

            print('construtor = ' + encript)
            print("- BLOCO CRIADO -\n")
            print(f"ID = {self.index}")
            print(f"NONCE = {self.nonce-1}")
            print(f"Transaction = {self.transaction}")
            print(f"TIME_STAMP = {self.timestamp}")
            print(f"PREV_HASH = {self.prev_hash}\n")
            print(f"HASH = {self.block_hash}\n")

    def calculate_hash(self):

        encript = f"{self.index}:{self.transaction}:{self.timestamp}:{self.prev_hash}:{self.nonce-1}"
        hash = sha256(encript.encode()).hexdigest()

        return hash   


class Blockchain:

    ledge = []

    def genesis(self):
        # Realiza a criação do Bloco Genesis
        try:
            blockgenesis = Block(0, "GENESIS", "0", True)

            print("----\nBLOCO GENESIS CRIADO - BLOCKCHAIN INICIADA\n----\n")
            self.ledge.append(blockgenesis)

        except Exception as e:
            print("ERRO AO INICIAR BLOCKCHAIN")
            print(e)

    def add_block(self, transaction):
        # Adiciona Bloco a Ledge
        try:
            index = len(self.ledge)
            prev_hash = self.get_last_hash()

            new_block = Block(index, transaction, prev_hash)
            self.ledge.append(new_block)

        except Exception as e:
            print("ERRO AO INICIAR BLOCKCHAIN")
            print(e)

    def get_last_hash(self):
        # Retorna o ultimo Hash
        block = self.ledge[-1]
        return block.block_hash

    def is_chain_valid(self):

        i = 1
        while(i != len(self.ledge)-1):

            cur_block = self.ledge[i]
            prev_block = self.ledge[i-1]

            if(cur_block.prev_hash != prev_block.block_hash):
                print(f"Bloco {i}: Inválido")
                i += 1
                continue

            if(cur_block.block_hash != cur_block.calculate_hash()):
                print(f"Bloco {i}: Inválido")
                i += 1
                continue

            print(f"Bloco {i}: Válido")    
            i += 1

        return True

    def get_all_hash(self):
        # Exibir todas as hashes
        for i, block in enumerate(self.ledge):
            print(f"{i}: {block.block_hash}")

