FILENAME = "count.txt"

def read_number():
    with open(FILENAME) as f:
        number = int(f.read())
        return number
    
def write_number(number):
        with open(FILENAME, "wt") as f:
             f.write(str(number))


num = read_number()
num += 1
print(f"We have run this program {num} times")
write_number(num)