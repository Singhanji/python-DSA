def get_initials(fullname):
     xs = fullname
     name_list = xs.split()
#     print(name_list()

     initials  = ''
     for name in name_list:
         initials += name[0].upper()
     return initials

n = input()
print(get_initials(n))
