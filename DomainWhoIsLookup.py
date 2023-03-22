import datetime
import whois  # pip install python-whois
import socket

def is_registered(domain_name):
    """
    Returns a boolean indicating whether a `domain_name` is registered.
    """
    try:
        w = whois.whois(domain_name)
    except Exception:
        return False
    else:
        return bool(w.domain_name)


def get_domain_name():
    """
    Prompts the user to enter a domain name to check.
    """
    while True:
        domain_name = input("Enter the domain name to check: ")
        if domain_name.strip():
            return domain_name.strip()
        else:
            print("Please enter a valid domain name.")


def user_choice():
    """
    Prompts the user to choose whether they want to display the full WHOIS information or look up another domain.
    """
    while True:
        choice = input("Enter '1' to display full WHOIS information or '2' to look up another domain: ").strip()
        if choice in ('1', '2'):
            return choice
        else:
            print("Invalid input. Please choose '1' or '2'.")


def get_ip_address(domain_name):
    try:
        ip_address = socket.gethostbyname(domain_name)
        return ip_address
    except:
        return None


def main():
    while True:
        # Get domain name from user
        domain_name = get_domain_name()

        # Check if the domain is registered
        try:
            if is_registered(domain_name):
                whois_info = whois.whois(domain_name)

                # Print the registrar
                print(f"Domain registrar: {whois_info.registrar}")

                # Print the WHOIS server
                print(f"WHOIS server: {whois_info.whois_server}")

                # Get the creation time
                creation_date = whois_info.creation_date
                if isinstance(creation_date, list):
                    creation_date = creation_date[0]
                print(f"Domain creation date: {creation_date}")

                # Get domain age
                today = datetime.datetime.now()
                age = today - creation_date
                print(f"Domain age: {age.days} days")

                # Get expiration date
                print(f"Expiration date: {whois_info.expiration_date}")

                # Print the IP address
                ip_address = get_ip_address(domain_name)
                if ip_address:
                    print(f"IP address: {ip_address}")
                else:
                    print("Could not retrieve IP address for the domain.")

                # Print the name servers
                if whois_info.name_servers:
                    print("Name servers:")
                    for ns in whois_info.name_servers:
                        print(f" - {ns}")
                else:
                    1print("No name servers found in WHOIS information.")

                # Print all other info
                if user_choice() == '1':
                    print("\nFull WHOIS information:")
                    print(whois_info)

            else:
                print(f"The domain '{domain_name}' is not registered.")

            # Ask user if they want to continue or exit
            choice = input("Press 'q' to quit or any other key to continue: ").strip()
            if choice == 'q':
                break

        except Exception as e:
            print(f"An error occurred while processing the domain '{domain_name}': {e}")


if __name__ == "__main__":
    main()
