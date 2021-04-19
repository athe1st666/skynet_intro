from typing import Tuple

from Crypto.Hash import SHA256
from Crypto.Random import random

from lib.helpers import read_hex

# Project TODO: Is this the best choice of prime? Why? Why not? Feel free to replacasddsae!

# 1536 bit safe prime for Diffie-Hellman key exchange
# obtained from RFC 3526
raw_prime = """FFFFFFFF FFFFFFFF C90FDAA2 2168C234 C4C6628B 80DC1CD1
29024E08 8A67CC74 020BBEA6 3B139B22 514A0879 8E3404DD
EF9519B3 CD3A431B 302B0A6D F25F1437 4FE1356D 6D51C245
E485B576 625E7EC6 F44C42E9 A637ED6B 0BFF5CB6 F406B7ED
EE386BFB 5A899FA5 AE9F2411 7C4B1FE6 49286651 ECE45B3D
C2007CB8 A163BF05 98DA4836 1C55D39A 69163FA8 FD24CF5F
83655D23 DCA3AD96 1C62F356 208552BB 9ED52907 7096966D
670C354E 4ABC9804 F1746C08 CA237327 FFFFFFFF FFFFFFFF"""
# Convert from the value supplied in the RFC to an integer
prime = read_hex(raw_prime)

# Project TODO: write the appropriate code to perform DH key exchange

#def create_dh_key() -> Tuple[int, int]:
    # Creates a Diffie-Hellman key
    # Returns (public, private)
   # a = random.randint(0, int(2**8))
    #return (a, a)


#implementation of password exchange process
#server fetching p (code specific to how to do it on the server)
#Large prime number i.e. pprime
#Given that the example code lacks the process of interaction between the server and the individual bots, it is better to write it as you understand it
#examples point to mostly summary algorithms, not complete DH implementation, so re-represented in the process, but may combine with problems
# As I understand it, the DH process is performed before all communication, and only after the DH verification is completed does the later communication begin

p = prime

# for bot1 Get calculated numbers
def get_calculation（ p ,a , X ):
	Y = pow( a , X , p )
	return Y

#ExchangeSecretKey
def exchange_key( X , Y , p ):
	key = pow( Y , X , p )
	return key

#Obtain the original roots a,b
#a,b is a positive integer less than p and is required to be large, here, only a larger number is left
#In practice you can do a test, e.g. greater than 100 bits to be retained for security, e.g. test greater than 2**20
def get_generator(p):
	a = 2
	list = []
	while a < p:		
		flag = 1
		while flag != p:
			if (a ** flag) % p == 1:
				break
			flag += 1
		if flag == (p - 1):
			list.append(a)	
		a += 1
	return list

def get_calculation(p,a,X):
	Y = pow(a,X,p)
	return Y

def get_key(X,Y,p):
	key = pow(Y,X,p)
	return key

list = get_generator(p)
	print(str(p) + ' 的一个原根为：', end = '')
	print(list[-1])
	print('------------------------------------------------------------------------------')
	
#A's private key
	XA = random.randint(0, p-1)

#B's private key
	XB = random.randint(0, p-1)

#Number of calculations for A
	YA = get_calculation(p, int(list[-1]), XA)
	
#Number of calculations for B
	YB = get_calculation(p, int(list[-1]), XB)


#A and B's private keys
key_B = get_key(XB, YA,p)
key_A = get_key(XA, YB,p)
	
# Communication conditions, server confirms key
def judge_key():
	if key_A == key_B return True


#def calculate_dh_secret(their_public: int, my_private: int) -> bytes:
    # Calculate the shared secret
    #shared_secret = their_public * my_private

    # Hash the value so that:
    # (a) There's no bias in the bits of the output
    #     (there may be bias if the shared secret is used raw)
    # (b) We can convert to raw bytes easily
    # (c) We could add additional information if we wanted
    # Feel free to change SHA256 to a different value if more appropriate
    #shared_hash = SHA256.new(str(shared_secret).encode()).digest()
    #return shared_hash
