# dictionaries
>>> # DICT[KEY]--> VALUE {KEY1: VALUE1 , KEY2: VALUE2...}
>>>  phone_book = {'aeshna' : '123-456-7890',
		  'tanya'  : '234-456-7890',
		  'rishabh': '345-678-9012'}
		  
>>> print(phone_book['aeshna'])
123-456-7890


>>> # to get the list of things given under one contact

phone_book = {'aeshna' : ['123-456-7890','aeshna@aeshna.com'],
		  'tanya'  : ['234-456-7890','tannya@tanya.com'],
		  'rishabh': ['345-678-9012','rishabh@rishabh.com']}
		  
>>> print(phone_book['aeshna'][1])
aeshna@aeshna.com



>>>print(phone_book['rishabh'][0])
		  
345-678-9012
>>> print(phone_book['aeshna'][0])
		  
123-456-7890
>>> print(phone_book['tanya'][0])
		  
234-456-7890
>>> 
