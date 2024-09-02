import time


# print(time.time() ) 
def send_emails():
    for email in range(100000):
        pass
    
print("pausing for 2sec")
time.sleep(2)

print("start again")

start = time.time()
send_emails()
end = time.time()

print(end - start)
