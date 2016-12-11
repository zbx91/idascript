# idascript
some useful python script for ida 

##1.add_xref_for_macho.py
		  When you deal with macho file with ida, you'll find out that it's not easy to find Objc-Class 
		member function's caller and callee, (because it use msgSend instead of direct calling 
		convention), so we need to make some connection between the selector names and member function 
		pointers, it's what my script just do ^_^
>Usage: just load script from ida, after some output then you can got what you want
>Feature:	
>>1. connect seletors with member function pointer 
>>2. get current member function's caller
	![image](https://github.com/lichao890427/idascript/blob/master/screenshots/add_xref_for_macho_1.png)
>>3. get member function where current 'msgSend' lead to
	![image](https://github.com/lichao890427/idascript/blob/master/screenshots/add_xref_for_macho_2.png)
##2.read_unicode.py
		  When there is chinese unicode character in programe, due to python's shortage, ida could not 
		recongnized them correctly, it's what my script just do ^_^, apply to many circumstance
>Usage: When deal with macho file, you only need to run the script, and it will automatically find unicode
string in segment named "__ustring"; and if deal with other type, you need to addtionally call function
'find_utf16_string(addr)' to find them
	![image](https://github.com/lichao890427/idascript/blob/master/screenshots/read_unicode.png)
>Notie: Due to the disadvantable of python2 itself, there still many characters could not be shown
