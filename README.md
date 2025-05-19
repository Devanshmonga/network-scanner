# network-scanner
Its a basic network scanner working with arp packages 

Below is a GitHub-ready README description for your ARP network scanner project:

---

# ARP Network Scanner

**ARP Network Scanner** is a lightweight Python script built with Scapy that scans a target IP or IP range by sending crafted ARP requests and listening for responses. It quickly identifies active hosts on a network and displays their corresponding IP and MAC addresses.

## Features

- **Network Discovery:** Uses ARP requests to identify devices connected to a specified network.
- **Clear Output:** Displays a formatted list of discovered IP addresses alongside their MAC addresses.
- **Simple Command-Line Interface:** Leverages `optparse` for parsing command-line arguments, ensuring you provide the necessary target range.
- **Built for Education & Testing:** Ideal for learning about network protocols, penetration testing in authorized environments, and troubleshooting network issues.

## Requirements

- **Python 3.x**  
- **Scapy Library:** Install via pip if not already installed:
  
  ```bash
  pip install scapy
  ```
  
- **Linux/Mac Environment:** The script is designed to work in Unix-based environments. (It can work on Windows if Scapy is properly configured, but this is less common.)
- **Administrative Privileges:** Running the script may require root privileges (e.g., using `sudo`) to properly send ARP requests.

## Getting Started

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/<yourusername>/arp-network-scanner.git
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd arp-network-scanner
   ```

3. **Run the Script:**

   Pass the target IP or IP range using the `-t` or `--target` flag. For example:

   ```bash
   sudo python scan.py -t 192.168.1.1/24
   ```

   This command initiates a scan on the `192.168.1.1/24` network range.

## How It Works

- **Crafting ARP Requests:**  
  The script builds an ARP packet (`scapy.ARP`) with the target IP range and combines it with an Ethernet frame (`scapy.Ether`) with a broadcast destination (`ff:ff:ff:ff:ff:ff`), ensuring that every device in the network receives the request.

- **Sending and Receiving:**  
  The combined packet is sent using Scapy's `srp` function, which waits for responses for a specified timeout period.

- **Data Parsing:**  
  The responses are parsed to extract the source IP (`psrc`) and hardware (MAC) address (`hwsrc`) from each reply, then stored in a list of dictionaries.

- **Displaying the Results:**  
  Finally, a neatly formatted table listing active device IPs along with their corresponding MAC addresses is printed on the terminal.

## Code Considerations

There are a couple of points to consider for a smooth experience:
- **Command-Line Argument Parsing:**  
  Verify the `get_arguments` function returns the options properly. For example, ensure the return variable is correctly named and that you call the function with parentheses (`options = get_arguments()`).

- **Network Authorization:**  
  Always make sure you have permission to scan the network before running this script, as unauthorized scanning may be against policies or law.

## Contributing

Contributions, bug fixes, and suggestions are warmly welcome. If you want to improve the script, fork the repository, make your changes, and submit a pull request. For major changes, please open an issue first to discuss your proposed improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for specific terms and conditions.

## Disclaimer

This tool is intended for educational purposes and authorized network testing only. Scanning networks without permission is illegal and unethical. Use this script responsibly.

---

*To enhance the project further, consider adding features such as multi-threading for faster scans or support for exporting the scan results to a file, such as CSV or JSON.*
