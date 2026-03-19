"""
Security Sentinel - KIMAD TECH
A security monitoring tool for Windows environments.
"""

import re
import subprocess
from datetime import datetime


# Set of suspicious IP addresses to monitor. Extend this list as needed.
SUSPICIOUS_IPS: set[str] = {"72.153.12.208"}

# Accounts considered authorized on this system. 'guest' is intentionally
# omitted because the Guest account should be disabled in secure environments.
AUTHORIZED_USERS = {
    "administrator",
    "defaultaccount",
    "wdagutilityaccount",
}


def timestamp() -> str:
    return datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")


def check_network_connections() -> None:
    print(f"\n{timestamp()} Checking active network connections...")
    alert_triggered = False
    # Pre-compile patterns that match each suspicious IP at a word boundary so
    # that, e.g., 172.153.12.208 does not trigger a false positive.
    patterns = {ip: re.compile(r"(?<!\d)" + re.escape(ip) + r"(?!\d)") for ip in SUSPICIOUS_IPS}
    try:
        result = subprocess.run(
            ["netstat", "-n"],
            capture_output=True,
            text=True,
            timeout=10,
        )
        lines = result.stdout.splitlines()
        for line in lines:
            for ip, pattern in patterns.items():
                if pattern.search(line):
                    print(f"  [ALERT] Suspicious IP detected: {ip}")
                    print(f"          Connection details: {line.strip()}")
                    alert_triggered = True
        if not alert_triggered:
            print(f"  [OK] No connections to monitored IPs {sorted(SUSPICIOUS_IPS)} detected.")
    except FileNotFoundError:
        print("  [ERROR] 'netstat' command not found. Ensure this script runs on Windows.")
    except subprocess.TimeoutExpired:
        print("  [ERROR] Network check timed out.")


def list_local_users() -> None:
    print(f"\n{timestamp()} Listing local user accounts...")
    try:
        result = subprocess.run(
            ["net", "user"],
            capture_output=True,
            text=True,
            timeout=10,
        )
        users: list[str] = []
        # Parse 'net user' output: account names appear after the header separator line
        lines = result.stdout.splitlines()
        in_accounts = False
        for line in lines:
            stripped = line.strip()
            if stripped.startswith("---"):
                in_accounts = True
                continue
            if in_accounts:
                if stripped.startswith("The command completed") or stripped == "":
                    continue
                # Each line may contain up to three space-separated usernames
                parts = stripped.split()
                users.extend(parts)

        unauthorized: list[str] = []
        for user in users:
            if user.lower() not in AUTHORIZED_USERS:
                unauthorized.append(user)

        if users:
            print(f"  Found {len(users)} account(s):")
            for user in users:
                status = "[UNAUTHORIZED]" if user in unauthorized else "[OK]"
                print(f"    {status} {user}")
        else:
            print("  [INFO] No user accounts found or could not parse output.")

        if unauthorized:
            print(
                f"\n  [ALERT] {len(unauthorized)} unauthorized account(s) detected:"
                f" {', '.join(unauthorized)}"
            )
        else:
            print("  [OK] All accounts are authorized.")

    except FileNotFoundError:
        print("  [ERROR] 'net' command not found. Ensure this script runs on Windows.")
    except subprocess.TimeoutExpired:
        print("  [ERROR] User listing timed out.")


def run_security_checks() -> None:
    print("=" * 60)
    print("  Security Sentinel - KIMAD TECH")
    print("=" * 60)
    print(f"{timestamp()} Starting security checks...")

    check_network_connections()
    list_local_users()

    print(f"\n{timestamp()} Security checks complete.")
    print("=" * 60)


if __name__ == "__main__":
    run_security_checks()
