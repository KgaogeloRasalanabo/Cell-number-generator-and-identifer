# run unique_million_cell_number_generator.py first if file not available 
# open cell number file, identify number of subscribers for each network provider and give sum of cell numbers

vod = []
cel = []
mtn = []
tel = []

# read from file
with open("unique_million_cell_numbers.txt", "r") as file:
    cell_numbers = file.read().splitlines()

# assign network provider
for item in cell_numbers:

    # Cell C identifier
    if item.startswith('074') or item.startswith('0610') or item.startswith('0611') or item.startswith('0612') or \
            item.startswith('0613'):
        cel.append(item)

    # Vodacom identifier
    elif item.startswith('0711') or item.startswith('0712') or item.startswith('0713') or item.startswith('0714') or \
            item.startswith('0715') or item.startswith('0716') or item.startswith('072') or item.startswith('076') or \
            item.startswith('079') or item.startswith('061') or item.startswith('062') or item.startswith('066') or \
            item.startswith('069'):
        vod.append(item)

    # MTN identifier
    elif item.startswith('0710') or item.startswith('0717') or item.startswith('0718') or item.startswith('0719') or \
            item.startswith('073') or item.startswith('078') or item.startswith('063') or item.startswith('068'):
        mtn.append(item)

    # TELKOM identifier
    else:
        tel.append(item)

# sum of each network provider and total cell numbers
print("Cell C numbers: ", len(cel))
print("Vodacom numbers: ", len(vod))
print("Telkom number: ", len(tel))
print("MTN numbers: ", len(mtn))
print("Total cell numbers: ", len(cel) + len(mtn) + len(vod) + len(tel))
