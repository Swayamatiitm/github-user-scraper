# grant.py

def set_permission_status(permission_type, status):
    with open('permission_status.txt', 'a') as f:
        f.write(f'{permission_type}:{status}\n')

def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python grant.py <permission_type>")
        return

    permission_type = sys.argv[1]
    print(f"{permission_type.capitalize()} access request received.")
    status = input("Approve access? (1 for Yes, 0 for No): ")
    
    if status not in ['0', '1']:
        print("Invalid input. Please enter 0 or 1.")
        return
    
    set_permission_status(permission_type, status)
    print(f"{permission_type.capitalize()} permission status set to {status}")

if __name__ == '__main__':
    main()
