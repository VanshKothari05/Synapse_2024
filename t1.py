from itertools import combinations
#  Combination creats combos of required and prints them in tuples in dict

Kevin = {"Halsey", "Taylor Swift", "Mitski", "Joji", "Shawn Mendes", "Sabrina Carpenter", "Nicky Minaj", "Conan Gray", "One Direction", "Justin Bieber"}
Stuart = {"Kendrick Lamar", "Steve Lacy", "Tyler the Creator", "Joji", "The Weeknd", "Coldplay", "Kanye West", "Travis Scott", "Frank Ocean", "Brent Faiyaz"}
Bob = {"Conan Gray", "Joji", "Dove Cameron", "Mitski", "Arctic Monkeys", "Steve Lacy", "Kendrick Lamar", "Isabel LaRosa", "Shawn Mendes", "Coldplay"}
Edith = {"Metallica", "Billie Eilish", "The Weeknd", "Mitski", "NF", "Conan Gray", "Kendrick Lamar", "Nicky Minaj", "Kanye West", "Coldplay"}

djs={
    "Kevin":Kevin,
    "Stuart":Stuart,
    "Bob":Bob,
    "Edith":Edith
}

def calculate_prob(set1,set2):
    common_artists=set1.intersection(set2)
    overlap1 = len(common_artists)/len(set1)
    overlap2=len(common_artists)/len(set2)
    return max(overlap1 ,overlap2) , len(common_artists)

successful_pair =[]

for (dj1, artists1), (dj2, artists2) in combinations(djs.items(), 2):
    overlap, common_count = calculate_prob(artists1, artists2)
    if overlap >= 0.3:
        successful_pair.append(((dj1, dj2), overlap, common_count))


successful_pair.sort(key=lambda x: (-x[1], -x[2]))

for pair in successful_pair:
    print(pair,"\n")


