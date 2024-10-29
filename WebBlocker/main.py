import datetime as dt 
import time

end_date = dt.datetime(2024, 12 , 25)
site_block = ["www.facebook.com", "www.wscubetech.com"]
host_path = "C:/Windows/System32/drivers/etc/hosts"
redirect = "127.0.0.1"

# Code to block the website for a limited time period
while True:
    if dt.datetime.now() < end_date:
        #opening the host file
        with open (host_path, "r+") as host_file:
            content = host_file.read()
            for website in site_block:
                # if website not in the file then write it down in given manner or if it is already there then proceed
                if website not in content:
                    host_file.write(redirect+ " "+ website+ "/n")
                else: 
                    pass
    else:
        with open (host_path, "r+") as host_file:
            #readlines is used because we want everylines of file to be read so that we don't delete important file
            content = host_file.readlines()
            #Start the reading from line 1
            host_file.seek(0)
            for lines in content:
                # This code means in the lines check for the webiste which is written in site block above
                if not any ( website in lines for website in site_block):
                    host_file.write(lines)
            #Convert the file back to original file that's why use the function truncate()
            host_file.truncate()

        time.sleep(5)
