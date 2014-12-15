import random
count = 0
random_num_list = []
"""
write_file = open("upper_word",'w')
with open ('words') as File:
    for line in File:
        count += 1
for i in range(0, 80000):
    random_num_list.append(random.randint(0, count))
no_duplicate_list = list(set(random_num_list))
no_duplicate_list.sort()
count = 0
index = 0
with open ('words') as File:
    for line in File:
        if count == no_duplicate_list[index]:
            write_file.write(line.upper())
            index += 1
            if index == len(no_duplicate_list):
                break
        count += 1

"""
write_file = open("common",'w')
with open ('common_words') as File:
    for line in File:
        write_file.write(line.upper())
print "Done"

