# search in a file that contains data with email senders and prints the
# prolific committer

file_name = 'tf.txt'

with open(file_name) as fh:

    senders = list() # list to store senders email

    # search in every line in the file if the line starts with 'From '
    # it splits the line and gets the secound word in the line which is
    # the email and adds it to senders list
    for line in fh:
        if not line.startswith('From '): continue

        words = line.split()
        senders.append(words[1])

    # dictionary stores emails as keys and the count of the email as value
    counts = dict()

    # checks if there is no key == email it creats a key and assign value to it
    for email in senders:
        if email not in counts:
            counts[email] = senders.count(email)

    # vars stores most repeated email and how many times did it repeat
    bigemail = None
    bigcount = None

    # it assign the first email (key = email) to the var bigemail and
    # assign the first value tothe var bigcount then it keeps searching for 
    # greater value to assign etc
    for key, value in counts.items():
        if bigemail == None or value > bigcount:
            bigcount = value
            bigemail = key

print(bigemail,bigcount)