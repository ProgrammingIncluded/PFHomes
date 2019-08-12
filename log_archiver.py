import os

MAX_LOGS = 4
FILE_NAME = "RESULTS"
EXT = ".log"

# Counter will be updated based off current iteration.
COUNTER = 0

files = [f for f in os.listdir() if os.path.isfile(os.path.join(".", f))]

def gen_f_name():
    return FILE_NAME + "_" + str(COUNTER) + EXT

# If don't exist, create it
if not os.path.isfile("record.dat"):
    f = open("record.dat", "a") 
    f.write("0")
    f.close()

# If at max, keep a mental note
with open("record.dat", "r+") as f:
    data = f.read()
    try:
        COUNTER = int(data)
        COUNTER += 1
    except:
        COUNTER = 0

# Write to our dat save
with open("record.dat", "w+") as f:
    if COUNTER - 1 >= MAX_LOGS:
        COUNTER = 0
    f.write(str(COUNTER))


# Check if there is a recent log file, if there is
# add a new file.
if FILE_NAME + EXT in files:
    name = gen_f_name()

    # Overwrite file if applicable
    if os.path.isfile(name):
        os.remove(name)
    # Create from renaming.
    os.rename(FILE_NAME + EXT, name)
    print("ARCHIVED LOGS TO: " +  name)
else:
    print("NO LOGS TO ARCHIVE, SKIPPING....")

