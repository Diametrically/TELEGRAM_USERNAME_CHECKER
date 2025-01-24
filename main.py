import requests
from colorama import Fore, Back, Style
import urllib3
urllib3.disable_warnings()

def check_usernames(usernames):
    available_users = []
    for username in usernames:
        try:
            url = 'https://fragment.com/?query='
            uri = f"https://t.me/{username}"
            ur = f"{url}{username}"
            response = requests.post(f"{ur}", verify=False, ).text
            if 'status-unavail">Unavailable' in response:
                print(Fore.GREEN + f"\n @{username} | {uri} | AVAILABLE")
                available_users.append(username)
            elif 'status-avail">Available' in response:
                print( Fore.BLUE + f"\n @{username} | {ur} | USERNAME IS ON AUCTION FOR SALE.")

            elif 'status-taken">Taken' in response:
                print(Fore.RED + f"\n @{username} | {ur} | USERNAME IS TAKEN")

            elif 'status-unavail">Sold' in response:
                print(Fore.RED + f"\n @{username} | {ur} | USERNAME IS TAKEN")

            else:
                print(Fore.RED + "\n Something Went Wrong..")
        except Exception as e:
            print(f"Error checking {username}: {e}")
            
    return available_users

if __name__ == "__main__":
    usernames_to_check = []
    with open("usernames.txt", "r") as file:
        for line in file:
            username = line.strip()
            if username:
                usernames_to_check.append(username)
    available = check_usernames(usernames_to_check)



