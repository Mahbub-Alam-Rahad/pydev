'''name=input("Enter your name :")
print("Good Afternoon , " + name)'''

#detect double spaces.
ds = "This is the string of double  spaces."
ds = ds.find("  ")
print(ds)  # Prints the index of the first occurrence of double spaces

ds = ds.replace("  ", " ")
print(ds)  # Replaces double spaces with a single space


#letter template
letter='''Dear, <name> 

Iam very happy and glad to tell you are selected !

Manager of ABC Company
Tom Jhones

<date>'''
name=input("Enter your name :")
date=input("Enter Date :")
letter=letter.replace("<name>",name)
letter=letter.replace("<date>",date)
print(letter)