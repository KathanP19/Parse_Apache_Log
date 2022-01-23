# Parse_Apache_Log
Simple Python Script to Parse Apache Log, Get all Unique IPs and Urls visited by that IP. It will create 3 different files.

- `allIP.txt` - Contains all the IPs in raw
- `uniqueIP.txt` - Contains all unique IP's
- `ipAndUrl.txt` - Contains list of Urls visited by that particular IP.

# Installation:
`git clone https://github.com/KathanP19/Parse_Apache_Log`

`cd Parse_Apache_Log`

# Usage:
```
Usage: parse_log.py [options]

Options:
  -h, --help            show this help message and exit
  -f FILE, --file=FILE  Path of you apache log file.
  -v, --verbose         Verbose Mode.
```

- `python3 parse_log.py -f apache_logs.txt`

For Verbose Mode use option `-v`:
- `python3 parse_log.py -f apache_logs.txt -v`
