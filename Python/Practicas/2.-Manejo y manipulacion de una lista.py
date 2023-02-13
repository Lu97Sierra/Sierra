abc = ['a','b','c','d','e','f','g','h','i','j',
       'k','l','m','n','ñ','o','p','q','r','s',
       't','u','v','w','x','y','z']
r = [abc[i-1] for i in range(1, len(abc)) if i % 3 != 0]
print(''.join(r))