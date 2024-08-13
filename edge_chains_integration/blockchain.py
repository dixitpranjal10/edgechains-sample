import edgechains
from config.edgechains_config import EDGECHAINS_API_KEY, NETWORK, NODE_URL

def initialize_edgechains():
    edgechains_config = {
        "api_key": EDGECHAINS_API_KEY,
        "network": NETWORK,
        "node_url": NODE_URL,
    }
    edgechains.initialize(edgechains_config)

def store_transaction_on_chain(transaction):
    try:
        tx_hash = edgechains.store(transaction)
        print(f"Transaction successfully stored on the blockchain. TX Hash: {tx_hash}")
        return tx_hash
    except Exception as e:
        print(f"Failed to store transaction: {str(e)}")
        return None
