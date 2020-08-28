from iterator import CountryURL
from generator import MD5Generator, file

countryURL1 = CountryURL()
#countryURL1.__init__()
countryURL1.__next__()
md5_generator = MD5Generator(file)
hash_gen = md5_generator.md5_gen()

while True:
    print(next(hash_gen))




