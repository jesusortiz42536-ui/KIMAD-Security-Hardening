# Security Sentinel – KIMAD TECH

A lightweight security monitoring tool for Windows environments, developed by **KIMAD TECH** as part of the KIMAD Security Hardening suite.

## Features

- **Network connection monitoring** – Scans active TCP/UDP connections and raises an alert if the suspicious IP address `72.153.12.208` is detected.
- **Local user auditing** – Enumerates all local Windows user accounts and flags any that are not on the authorized list.
- **Timestamped CLI output** – Every security check is printed to the terminal with a precise timestamp so that events can be correlated with other log sources.

## Requirements

- Windows operating system (uses `netstat` and `net user` built-in commands)
- Python 3.10 or later

## Usage

```cmd
python security_sentinel.py
```

Sample output:

```
============================================================
  Security Sentinel - KIMAD TECH
============================================================
[2026-03-19 00:17:46] Starting security checks...

[2026-03-19 00:17:46] Checking active network connections...
  [OK] No connections to 72.153.12.208 detected.

[2026-03-19 00:17:46] Listing local user accounts...
  Found 3 account(s):
    [OK] Administrator
    [OK] Guest
    [UNAUTHORIZED] hacker_account
  [ALERT] 1 unauthorized account(s) detected: hacker_account

[2026-03-19 00:17:47] Security checks complete.
============================================================
```

## Configuration

To adjust which accounts are considered authorized, edit the `AUTHORIZED_USERS` set near the top of `security_sentinel.py`:

```python
AUTHORIZED_USERS = {
    "administrator",
    "guest",
    "defaultaccount",
    "wdagutilityaccount",
}
```

To change the monitored IP address, update the `SUSPICIOUS_IP` constant:

```python
SUSPICIOUS_IP = "72.153.12.208"
```

## License

See [LICENSE](LICENSE).
