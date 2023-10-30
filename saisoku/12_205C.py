A,B,C=map(int,input().split())
if C%2==0:
	if A>=0:
		if B>=0:
			if abs(A)>abs(B):
				print('>')
			elif abs(A)==abs(B):
				print('=')
			elif abs(A)<abs(B):
				print('<')
		elif B<0:
			if abs(A)>abs(B):
				print('>')
			elif abs(A)==abs(B):
				print('=')
			elif abs(A)<abs(B):
				print('<')
	elif A<0:
		if B>=0:
			if abs(A)>abs(B):
				print('>')
			elif abs(A)==abs(B):
				print('=')
			elif abs(A)<abs(B):
				print('<')
		elif B<0:
			if abs(A)>abs(B):
				print('>')
			elif abs(A)==abs(B):
				print('=')
			elif abs(A)<abs(B):
				print('<')
elif C%2!=0:
	if A>=0:
		if B>=0:
			if abs(A)>abs(B):
				print('>')
			elif abs(A)==abs(B):
				print('=')
			elif abs(A)<abs(B):
				print('<')
		elif B<0:
			if abs(A)>abs(B):
				print('>')
			elif abs(A)==abs(B):
				print('>')
			elif abs(A)<abs(B):
				print('>')
	elif A<0:
		if B>=0:
			if abs(A)>abs(B):
				print('<')
			elif abs(A)==abs(B):
				print('<')
			elif abs(A)<abs(B):
				print('<')
		elif B<0:
			if abs(A)>abs(B):
				print('<')
			elif abs(A)==abs(B):
				print('=')
			elif abs(A)<abs(B):
				print('>')

