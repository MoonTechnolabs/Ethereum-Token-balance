from web3 import Web3


def get_eth_balance(eth_address):
    """
    Fetches the balance of an Ethereum address in Ether.

    Parameters:
    eth_address (str): The Ethereum address to query.

    Returns:
    float: The balance of the address in Ether.

    Raises:
    Exception: If the connection to the Ethereum node fails or Invalid Ethereum address.
    """
    # Infura mainnet URL
    infura_url = "https://mainnet.infura.io/v3/b782ea6b08de41b484f2ae766eacdee0"
    
    # Initialize a Web3 instance
    web3 = Web3(Web3.HTTPProvider(infura_url))

    # Ensure the connection is successful
    if not web3.is_connected():
        raise Exception("Failed to connect to the Ethereum node.")

    # Check if the Ethereum address is valid
    if not web3.is_address(eth_address):
        raise ValueError("Invalid Ethereum address.")

    # Fetch the balance in Wei
    balance_wei = web3.eth.get_balance(eth_address)
    
    # Convert the balance from Wei to Ether
    balance_eth = web3.from_wei(balance_wei, 'ether')

    return balance_eth