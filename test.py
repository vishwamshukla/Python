# # # # # # z = set('abc')
# # # # # # z.add('san')
# # # # # # z.update(set(['p','q']))
# # # # # # print(z)

# # # # # alphabet = 'abc'
# # # # # for i in range(len(alphabet)):
# # # # #     alphabet[i].upper()
# # # # # print(alphabet)

# # # # x = 'abcdef'
# # # # i='a'
# # # # while i in x[:-1]:
# # # #     print(i,end=" ")
    
    
# # # array1 = [1,2,3,4,5]
# # # array2 = array1
# # # array2[0] = 0
# # # print(arr)

# # print("Welcomme to TURING".capitalize())

# import ipywidgets as widgets

# w = widgets.IntSlider()

# from IPython.display import display
# display(w)


import smtplib

obj = smtplib.SMTP("smtp.gmail.com", 587)

obj.ehlo()

obj.starttls()

import getpass

password = getpass.getpass("Password please: ")