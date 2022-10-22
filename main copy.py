# Getting the dictionaries and tally ready to receive.
senders = {}
senders_addresses = {}
count = 0
# First off, the code needs to open the file to read. Using with/as to avoid opening/closing
# errors. Using "r" access mode to avoid unintended edits.
with open("mbox-short.txt", "r") as input_file:
    # Making each line of the document a manipulable string.
    email_line = input_file.readline()
    # Then setting the loop to go through each line of the document. I tried setting
    # this as a while-loop but maybe the EOF character is missing? It went infinite on me.
    for email_line in input_file:
        # Your notes say that the "From " contains the sender, not "From:", but I see no
        # difference between the information in line 01 and line 38, or line 66 and line 103.
        # Is the issue supposed to be which line populates the "From" field in the user
        # interface? Is it that apache is setting the sender at the latter line as part
        # of the authentication process?
        if email_line[0:5] == "From ":
            # Let's take care of the tally first
            count += 1
            # We know the index value of the beginning of the email prefix, and we know the
            # domain is marked with a special character, so index that character and use it
            # as the cutoff for the prefix.
            find_at = email_line.find("@")
            sender = email_line[5:find_at]
            # I thought I could be clever with the assignment statement here and just += 1
            # the dictionary key but that broke the code. Happy to find a use for try/except. PyCharm
            # disapproves.
            try:
                senders[sender] = senders[sender] + 1
            except:
                senders[sender] = 1
            # And now to capture the full address in a separate dictionary using split method.
            # Split separates the words in the string. Index of 1 indicates the second word.
            full_sender = email_line.split()
            address = full_sender[1]
            try:
                senders_addresses[address] = senders_addresses[address] + 1
            except:
                senders_addresses[address] = 1
        # Wanted to make sure there was a fall-through since I'd already run into the infinite
        # loop issue. PyCharm recommended this.
        else:
            pass
# At this point the text file should have closed automatically, leaving me with the dictionaries.
# Now to show the dictionaries.
for key in senders:
    print("Name, count:", key + ",", senders[key])
print("\n")
for key in senders_addresses:
    print("Address, count:", key + ",", senders_addresses[key])
print("\n")
# Now we check the tally, and confirm by summing across the sender counts.
print("Total emails received= ", count)
truing_sum = 0
for key in senders:
    truing_sum += senders[key]
print("And summing across the sender totals= ", truing_sum)
# Which key has the highest value?
most_prolific_sender = None
most_num_emails = 0
for (sender, count) in senders.items():
    if most_num_emails < count:
        most_prolific_sender = sender
        most_num_emails = count
print(most_prolific_sender, "sent the most missives, with a total of", most_num_emails, "emails.")
print("\n")
# Now we'll look at ways to comb through our trove.
print("The sender dictionary, sorted by key:", sorted(senders.keys()))
print("The sender address dictionary, reverse-sorted by value:", sorted(senders_addresses.values(), reverse=True))
print("The sender dictionary, sorted by kv pairs:")
for key, value in sorted(senders.items()):
    print(key, value)

# I'm not exactly sure what you were asking for here, so I'm just gonna write my best understanding of the distinction. Dictionaries
# are not indexed by position, they're indexed by keys. Once the key has been created, its paired value can be adjusted. The get() 
# method accesses the dictionary the same way an index acesses a list, looking for the specified key and retrieving the paired value.
# If we use the item() method though, the dictionary can get transformed into a tuple which is indexed like a list but is hard set- 
# there's no appending additional elements or editing values. I'm guessing the immutability is nice when you need to share a dictionary
# while still maintaining a source of truth. Hope that's what you meant.

print("Tuples in a dictionary:")
print("Key-value pairs are:")
for key, value in senders.items():
    print(key, value)
print("and printed as tuples")
sender_tuples = senders.items()
print(sender_tuples)


