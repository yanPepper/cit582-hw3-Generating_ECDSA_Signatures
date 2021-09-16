from fastecdsa.curve import secp256k1
from fastecdsa.keys import export_key, gen_keypair

from fastecdsa import curve, ecdsa, keys, point
from hashlib import sha256

from random import randint

def sign(m):
	#generate public key
	#Your code here
	# this is your sign (private key)
	private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1) 
	public_key = private_key.get_verifying_key()

	#generate signature
	#Your code 
	G = ecdsa.secp256k1 #generator
	n = G.order() # order of G
	k = randint(1,n)
	p1 = k * G
	x1 = p1.x.value
	r = x1 % n
	z = sha256(m.encode('utf-8')).hexdigest()
	k_inv = pow(k,-1,n)
	s = (z + r * private_key) * k_inv % n

	assert isinstance( public_key, point.Point )
	assert isinstance( r, int )
	assert isinstance( s, int )
	return( public_key, [r,s] )


