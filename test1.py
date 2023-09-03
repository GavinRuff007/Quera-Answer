from bitcoin.rpc import RawProxy

# Create a connection to local Bitcoin Core node
p = RawProxy()

# Run the getblockchaininfo command, store the resulting data in info
info = p.getblockchaininfo()

# Retrieve the 'blocks' element from the info
print(info['blocks'])


print("------------------------------------------------------------------------------------------------------------------------------------")





# The block height where Alice's transaction was recorded
blockheight = 264873

# Get the block hash of block with height 264873
blockhash = p.getblockhash(blockheight)

# Retrieve the block by its hash
block = p.getblock(blockhash)

# Element tx contains the list of all transaction IDs in the block
transactions = block['tx']
print(transactions)
block_value = 0

# Iterate through each transaction ID in the block
for txid in transactions:
    print(txid)
    block_value += 1
print("Total value in block: ", block_value)



print("------------------------------------------------------------------------------------------------------------------------------------")

