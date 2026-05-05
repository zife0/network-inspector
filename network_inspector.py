import socket

def get_hostname():
    return socket.gethostname()

def get_ip():
    try:
        return socket.gethostbyname(socket.gethostname())
    except:
        return "Unable to get IP"

def check_connection(host="8.8.8.8", port=53):
    try:
        socket.setdefaulttimeout(3)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except:
        return False

def main():
    print("=== Network Inspector ===")
    print("Hostname:", get_hostname())
    print("IP Address:", get_ip())

    if check_connection():
        print("Connection: Active")
    else:
        print("Connection: Failed")

if __name__ == "__main__":
    main()
