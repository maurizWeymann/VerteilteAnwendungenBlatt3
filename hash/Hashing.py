import hashlib
import itertools
import string
import sys
import timeit

start = timeit.default_timer()

def crackHash():
    arr = ["656ac31bcca3e16bb8d7f864659edceabc5b7de905899052dd9fab980ff33c61a32336ec54f0213515c794fa7352fa3bb0527e32cd659d2dd564847546055501",
    "7d7764888dc13da6436666cd97043a5ead014596cd9aef6d12f95a5602d15993beebd44b92014732c340239e7cd1f07c5ed4035d1a02151916e94d43ffa55cfa",
    "bbccdf2efb33b52e6c9d0a14dd70b2d415fbea6e",
    "d6904cf515fa8e8921c2aab7c9aaafe2232dd065387e17f48da712ec0a25e69ca329453bb545ac4a8ed06d2bce141b96",
    "0ebb429fa86d481c2630fac53db1c91cffed5d4d41d1021c179444eb67e7ee0b"]
    
    for hash in arr:
        
        try: 
            passFile = open("test.txt", "r")
        except:
            print("Could not find the file!")
        for word in passFile:
            encWord = word.encode("utf-8")
            digest = hashlib.sha256(encWord.strip()).hexdigest()
            digest2 = hashlib.sha3_512(encWord.strip()).hexdigest()
            digest3 = hashlib.sha512(encWord.strip()).hexdigest()
            digest4 = hashlib.sha1(encWord.strip()).hexdigest()
            digest5 = hashlib.sha3_384(encWord.strip()).hexdigest()
            
            if digest == hash: 
                print(word)
                
            elif digest2 == hash:
                print(word)
                
            elif digest3 == hash:
                print(word)
                
            elif digest4 == hash: 
                print(word)
            elif digest5 == hash:
                print(word)
                     
crackHash()

stop = timeit.default_timer()
print('Time: ', stop - start)