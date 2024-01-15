from netmiko_test import ConnectHandler

# Define the router details
router = {
    'device_type': 'autodetect',
    'ip': '192.168.1.1',
    'username': 'root',
    'password': ''  # Only if there is an enable password
}

# Establish SSH connection to the router
try:
    net_connect = ConnectHandler(**router)
    print("Connected successfully!")

    # Example: Run a command on the router
    output = net_connect.send_command("show interfaces")

    print("Command output:")
    print(output)

except Exception as e:
    print(f"Failed to connect: {str(e)}")

finally:
    # Disconnect from the router
    if net_connect:
        net_connect.disconnect()
        print("Disconnected.")
