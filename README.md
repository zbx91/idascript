# idascript
some useful python script for ida 

1.  add_xref_for_macho.py
	When you deal with macho file with ida, you'll find out that it's not easy to find Objc-Class member function's caller and callee, (because it use msgSend instead of direct calling convention), so we need to make some connection between the selector names and member function pointers, it's what my script jus do
  Usage:  just load script from ida, after some output then you can got what you want
  Feature:	
	1. connect seletors with member function pointer 
	2. get current member function's caller
	![image](https://github.com/lichao890427/idascript/blob/master/screenshots/add_xref_for_macho_1.png)
	3. get member function where current 'msgSend' lead to
	![image](https://github.com/lichao890427/idascript/blob/master/screenshots/add_xref_for_macho_2.png)
