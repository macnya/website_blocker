
#import libraries
import time
import os

#create a function to block unwanted websites
def block_websites():
    # Path of the Host File
    host_path = r"C:\Windows\System32\drivers\etc\hosts"

    # List of Websites to be blocked
    websites = ["www.facebook.com", "www.instagram.com","www.whatsapp.com", "www.tiktok.com"]

    #Redirect to localhost
    redirect = "127.0.0.1"
    
    with open(host_path, 'a') as file:
        for website in websites:
            file.write(redirect + " " + website + "\n")

#create a loop to keep the program running
while True:
    block_websites()
    time.sleep(5)
