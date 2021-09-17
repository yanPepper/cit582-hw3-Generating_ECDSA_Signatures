from fastecdsa.curve import secp256k1
from fastecdsa.keys import export_key, gen_keypair

from fastecdsa import curve, ecdsa, keys, point
from hashlib import sha256

from random import randint

def sign(m):
	#generate public key
	#Your code here
	private_key, public_key = keys.gen_keypair(curve.secp256k1) 

	#generate signature
	#Your code here
	#generator, the base point of the curve
	G = secp256k1.G 

	#order of the base point
	n = secp256k1.q 

	#random number k
	k = randint(1,n) 
	kG = k * G
	x1 = kG.x
	y1 = kG.y
	r = x1 % n

	z = sha256(m.encode('utf-8')).hexdigest()
	k_inv = pow(k,-1,n)
	s = (z + r * private_key) * k_inv % n

	assert isinstance( public_key, point.Point )
	assert isinstance( r, int )
	assert isinstance( s, int )
	return( public_key, [r,s] )


