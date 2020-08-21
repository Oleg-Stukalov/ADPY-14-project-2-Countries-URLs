from iterator import CountryURL
from generator import MD5Generator, file

countryURL1 = CountryURL()
countryURL1.get_country()
md5_generator = MD5Generator(file)
md5_generator.md5_gen()

