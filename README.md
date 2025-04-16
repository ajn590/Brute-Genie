# Brute-Genie 🔐

**Brute-Genie** is an ethical brute-force automation tool built for Linux. It is intended **strictly for educational and ethical cybersecurity research**. This tool generates intelligent wordlists based on user input, performs brute-force attacks (e.g., Instagram), and integrates Tor for anonymized IP rotation.

> ⚠️ This tool is for **educational purposes only**. Unauthorized usage against live targets is **illegal**.

---

## ⚙️ Features

- ✅ **Auto Wordlist Generator** (username + custom hints)
- ✅ **Custom Password Appending**
- ✅ **Tor Integration** (automatically changes IP every 5 attempts)
- ✅ **Progress Visualization** (CLI progress bar)
- ✅ **Headless & Linux-ready**

---

## 📦 Requirements

Install the required Python dependencies and Tor:
```bash
pip install -r requirements.txt
sudo apt install tor
sudo systemctl start tor
```

---

## 🔧 Installation

```bash
git clone https://github.com/ajn590/Brute-Genie.git
cd Brute-Genie
pip install -r requirements.txt
```

---

## 🚀 Usage

```bash
python3 brute_genie.py
```

Follow the prompts:
1. Enter target username.
2. Provide custom hints (e.g., pet names, birth years).
3. Choose to append your own passwords or proceed.
4. Let Brute-Genie do the rest — it rotates IPs via Tor and visualizes progress.

---

## 🧪 Example

```bash
python3 brute_genie.py
```

```
Target username: instatester123
Enter hints (comma-separated): 1234,pass,petname,birthday
Do you want to add custom passwords? (y/n): y
Enter custom passwords (comma-separated): password123,qwerty,admin123
```

---

## 🧠 Notes

- Tor must be installed and running.
- This tool does not guarantee success due to Instagram’s rate-limiting and 2FA.
- You may adapt the script for **other services** if you're doing ethical security testing.

---

## 📜 License

MIT License. See [LICENSE](LICENSE) for more information.

---

## 🧑‍💻 Author

**Abel Varghese Raju**  
GitHub: [@ajn590](https://github.com/ajn590)  
Email: [diprapha0@gmail.com](mailto:diprapha0@gmail.com)

---

## 💡 Disclaimer

This tool is intended **only for ethical hacking, educational research, or personal use** on systems you **own or have explicit permission to test**. Any misuse is strictly prohibited.
