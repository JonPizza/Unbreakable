import sys

def encrypt(s, key):
	enc = []
	for c, k in zip(s, key):
		enc.append(ord(k) + ord(c))
	return enc

def decrypt(s, key):
	pass
	# not currently implemented

if __name__ == '__main__':
	print('[*] Doing the encryption...')
	with open('out.txt', 'w') as f:
		f.write(encrypt(argv[1], argv[2]))
	print('[+] Encrypted! Wrote data to out.txt')
