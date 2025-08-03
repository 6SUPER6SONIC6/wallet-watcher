# Wallet Watcher

A command-line tool for checking Ethereum wallet balances and token holdings with spam filtering and search history tracking.

## Features

- Check Ethereum wallet balances and ERC-20 token holdings
- Automatic spam token filtering
- Beautiful terminal output with formatted tables
- Search history logging to CSV
- Input validation for Ethereum addresses
- Real-time USD value calculations

## Installation

1. Clone the repository:
```bash
git clone https://github.com/6SUPER6SONIC6/wallet-watcher.git
cd wallet-watcher
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Check a wallet
```bash
python wallet_watcher.py -w 0x1234567890123456789012345678901234567890
```

### View search history
```bash
python wallet_watcher.py -H
```

### Get help
```bash
python wallet_watcher.py --help
```

## Example Output

```
 _       __      ____     __     _       __      __       __             
| |     / /___ _/ / /__  / /_   | |     / /___ _/ /______/ /_  ___  _____
| | /| / / __ `/ / / _ \/ __/   | | /| / / __ `/ __/ ___/ __ \/ _ \/ ___/
| |/ |/ / /_/ / / /  __/ /_     | |/ |/ / /_/ / /_/ /__/ / / /  __/ /    
|__/|__/\__,_/_/_/\___/\__/     |__/|__/\__,_/\__/\___/_/ /_/\___/_/     
                                                                         

                   0x112532b200980ddee8226023bebbe2e6884c31e2                   
┌─────────────────────────────────────┬──────────────────────┬─────────────────┐
│ Token                               │               Amount │           Value │
├─────────────────────────────────────┼──────────────────────┼─────────────────┤
│ Ethereum(ETH)                       │             0.003184 │          $11.02 │
├─────────────────────────────────────┼──────────────────────┼─────────────────┤
│ Resolv USR(USR)                     │                18.72 │          $18.72 │
└─────────────────────────────────────┴──────────────────────┴─────────────────┘
```
```
    __  ___      __                  
   / / / (_)____/ /_____  _______  __
  / /_/ / / ___/ __/ __ \/ ___/ / / /
 / __  / (__  ) /_/ /_/ / /  / /_/ / 
/_/ /_/_/____/\__/\____/_/   \__, /  
                            /____/   

┌─────────────────────────────────────────────────────┬────────────────────────┐
│ Address                                             │                   Date │
├─────────────────────────────────────────────────────┼────────────────────────┤
│ 0x4838b106fce9647bdf1e7877bf73ce8b0bad5f97          │     01 Aug 2025, 23:33 │
├─────────────────────────────────────────────────────┼────────────────────────┤
│ 0x112532b200980ddee8226023bebbe2e6884c31e2          │     02 Aug 2025, 19:11 │
└─────────────────────────────────────────────────────┴────────────────────────┘
```


## Dependencies

- `requests` - HTTP requests to Ethplorer API
- `rich` - Terminal formatting and tables
- `pyfiglet` - ASCII art headers
- `argparse` - Command-line argument parsing

## Project Structure

```
wallet-watcher/
├── wallet_watcher.py    # Main application entry point
├── wallet_checker.py    # API interaction and data parsing
├── history.py          # CSV history management
├── utils.py            # Utility functions and validation
├── data/               # Generated history files
└── requirements.txt    # Project dependencies
```

## How It Works

1. **Input Validation**: Validates Ethereum addresses using regex patterns
2. **API Request**: Fetches wallet data from Ethplorer API
3. **Data Processing**: Parses JSON response and converts raw token balances using decimal precision
4. **Spam Filtering**: Filters out spam tokens based on price, supply, and keyword detection
5. **Output Formatting**: Displays results in formatted tables with USD values
6. **History Tracking**: Logs searched addresses with timestamps to CSV file

## Technical Highlights

- Clean modular architecture with separation of concerns
- Comprehensive error handling for network and file operations
- Type hints for better code documentation
- Context managers for safe file operations
- Professional CLI interface with rich formatting

## API

This project uses the [Ethplorer API](https://github.com/EverexIO/Ethplorer/wiki/ethplorer-api) with a free API key for fetching Ethereum blockchain data.
