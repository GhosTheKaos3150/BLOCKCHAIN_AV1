from blockchain.Blockchain import Blockchain

if __name__ == '__main__':
    blockchain = Blockchain()

    blockchain.genesis()

    blockchain.add_block("TESTE 1")
    blockchain.add_block("TESTE 2")
    blockchain.add_block("TESTE 3")
    blockchain.add_block("TESTE 4")

    blockchain.ledge[2].transaction = "ALTERADO"

    blockchain.add_block("TESTE 5")

    print("<<<INICIO TESTE>>")
    blockchain.is_chain_valid()
    print("<<<FIM TESTE>>\n")

    blockchain.get_all_hash()

