import requests

def get_permission_status(permission_type):
    try:
        with open('permission_status.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith(f"{permission_type}:"):
                    return int(line.split(':')[1].strip())
    except FileNotFoundError:
        print("Permission status file not found.")
    return 0  # Default to 0 if file is not found or permission type is not in the file

def get_permission_response(permission_type):
    url = 'http://127.0.0.1:5000/request-permission'
    data = {
        'app_name': 'MyApp',
        'permission_type': permission_type
    }
    try:
        print(f"Sending request for {permission_type} permission...")
        response = requests.post(url, json=data)
        response.raise_for_status()  # Raise an error if the request failed
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error while making request: {e}")
        return None

def main():
    print("Select the type of permission needed:")
    print("1. Call Logs")
    print("2. Messages")
    print("3. File Access")
    
    choice = input("Enter your choice (1/2/3): ")
    permission_types = {
        '1': 'call_logs',
        '2': 'messages',
        '3': 'file_access'
    }

    if choice in permission_types:
        permission_type = permission_types[choice]
        status = get_permission_status(permission_type)
        
        if status == 0:
            print("Permission not granted")
            necessary = input("Is it necessary? (1 for Yes, 0 for No): ")
            if necessary == '1':
                print("Providing dummy data to the app.")
                dummy_response = get_permission_response(permission_type)
                if dummy_response:
                    print("Dummy data provided:", dummy_response)
                    print("Real data is safe and not accessed.")
            else:
                print("Process ended.")
        elif status == 1:
            response = get_permission_response(permission_type)
            if response:
                print("Response:", response)
        else:
            print("Permission status unknown or not set.")
    else:
        print("Invalid choice")

if __name__ == '__main__':
    main()
