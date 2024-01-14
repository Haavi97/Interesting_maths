combs = '2**256'
bits = eval(combs)*256
Bs = bits/8
GBs = Bs/1024**3
TBs = GBs/1024**3
# In 2017 https://www.quora.com/How-many-servers-can-the-largest-data-center-contain-How-much-TB-in-size-is-that
max_TB = 1560000000  # 1,560,000,000
data_centers = TBs/max_TB
square_foot_to_meters = 0.09290304
square_meters = 6.3e6*square_foot_to_meters
km2 = square_meters/1e6
dc_km2 = data_centers*km2
world_km2 = 510.1e6

print("""
sha-256 hashing function i 256 bits long
That means it has {0} different combinations.
To store all those combinations would occupy:
({0})*256 = {1} bits
{1}/8 = {2} bytes
{2}/1024**3 = {3} gigaBytes
{3}/1024 = {4} teraBytes
If the biggest data center in 2017 had
{5} teraBytes capacity
it would take:
{6} such data centers to store all the possible sha-256 hashes
If each data center is {7} km^2
Having that many data centers would take {8} km^2
If the worlds land area is {9} km^2, 
then hose data centers would take the size of {10} times the world.
Hackers need to conquer planets before storing all possible hashes.
      
-----
      SO NOW YOU HAVE A BETTER IDEA OF HOW BIG THE HASH SPACE IS AND THEREFORE THE 
      AMOUNT OF POSSIBLE ADDRESES IN BLOCKCHAINS, SO DON'T WORRY ABOUT HOW MANY ADDRESSES YOU HAVE
""".format(combs, bits, Bs, GBs, TBs, max_TB, data_centers, km2, dc_km2, world_km2, dc_km2/world_km2))

# Calculate the amount of address that each person could theoretically have
# 2**256 is the amount of possible addresses in ethereum
# There are 7.6 billion people in the world
number_of_people = 7.6e9
addresses_per_person = 2**256/number_of_people
print("""
If there are {0} people in the world, then each person could have {1} addresses
""".format(number_of_people, addresses_per_person))
