from tkinter import *
from tkinter.ttk import *
import time


action = input('to login,type "login" to crete an account, type "Create",and to delete an account type delte: ')
def create_account(file='usernames + passwords.txt'):
	username = input('username: ')
	password = input('password: ')

	with open(file, 'a') as File:
		File.write('\n' + encrypt(username)+ ',' + encrypt(password))


def delete_account(file='usernames + passwords.txt'):
	username = input('username to delete: ')
	password = input('verify your password: ')

	with open(file, 'r')as File:
		text = File.read()

	text = text.replace(encrypt(username)+ ',' + encrypt(password), '')

	with open(file, 'w') as File:
		File.write(text)

def login(file='usernames + passwords.txt'):
	username = input('username: ')
	password = input('password: ')

	with open(file,'r')as File:
		text = File.read()

	find_account = text.find(encrypt(username)+ ',' + encrypt(password))

	if find_account:
		print('Welcome, '+ username)

	else:
		print('incorrect username and or password')

def encrypt(str):
	encrypted= ''
	for char in str:
		encrypted += chr(ord(char)+17)

	return(encrypted)

if action == 'create':
	create_account()
if action == 'delete':
	delete_account()
if action == 'login':
	login()



#username: cschellenger1
#password: monk122
