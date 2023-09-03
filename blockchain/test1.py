from bitcoin.rpc import RawProxy
p = RawProxy()
info = p.getblockhash(10)
trx1 = p.getrawtrancation(info)
print(info)