import os
from datetime import datetime

def view_security_logs():
    """Display the security log file contents"""
    log_file = 'security.log'

    if not os.path.exists(log_file):
        print("Security log file not found. No security events have been logged yet.")
        return

    print("=" * 80)
    print("SECURE CHAT SECURITY LOG")
    print("=" * 80)

    try:
        with open(log_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        if not lines:
            print("Security log is empty.")
            return

        # Display last 50 entries (most recent first)
        recent_lines = lines[-50:][::-1] if len(lines) > 50 else lines[::-1]

        for line in recent_lines:
            print(line.strip())

        print("\n" + "=" * 80)
        print(f"Total security events logged: {len(lines)}")
        print(f"Log file: {os.path.abspath(log_file)}")

    except Exception as e:
        print(f"Error reading security log: {e}")

def get_security_stats():
    """Display security statistics"""
    log_file = 'security.log'

    if not os.path.exists(log_file):
        print("No security log file found.")
        return

    stats = {
        'total_events': 0,
        'login_success': 0,
        'login_failed': 0,
        'register_success': 0,
        'register_failed': 0,
        'connections_failed': 0,
        'auth_errors': 0
    }

    try:
        with open(log_file, 'r', encoding='utf-8') as f:
            for line in f:
                stats['total_events'] += 1

                if 'LOGIN_SUCCESS' in line:
                    stats['login_success'] += 1
                elif 'LOGIN_FAILED' in line:
                    stats['login_failed'] += 1
                elif 'REGISTER_SUCCESS' in line:
                    stats['register_success'] += 1
                elif 'REGISTER_FAILED' in line:
                    stats['register_failed'] += 1
                elif 'CONNECTION_FAILED' in line:
                    stats['connections_failed'] += 1
                elif 'AUTH_ERROR' in line:
                    stats['auth_errors'] += 1

        print("\nSECURITY STATISTICS:")
        print("-" * 40)
        print(f"Total Events: {stats['total_events']}")
        print(f"Successful Logins: {stats['login_success']}")
        print(f"Failed Logins: {stats['login_failed']}")
        print(f"Successful Registrations: {stats['register_success']}")
        print(f"Failed Registrations: {stats['register_failed']}")
        print(f"Failed Connections: {stats['connections_failed']}")
        print(f"Authentication Errors: {stats['auth_errors']}")

        # Calculate security ratios
        if stats['login_success'] + stats['login_failed'] > 0:
            login_success_rate = (stats['login_success'] / (stats['login_success'] + stats['login_failed'])) * 100
            print(".1f")

    except Exception as e:
        print(f"Error calculating statistics: {e}")

if __name__ == "__main__":
    print("Secure Chat Security Log Viewer")
    print("1. View recent security logs")
    print("2. View security statistics")
    print("3. Exit")

    while True:
        try:
            choice = input("\nEnter your choice (1-3): ").strip()

            if choice == '1':
                view_security_logs()
            elif choice == '2':
                get_security_stats()
            elif choice == '3':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")