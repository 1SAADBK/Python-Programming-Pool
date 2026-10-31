def secure_archive(filename: str,
                   action: str = "read", content: str = "") -> tuple:
    if action == "write":
        try:
            with open(filename, 'w') as fileobj:
                fileobj.write(content)
                return (True, 'Content successfully written to file')
        except Exception as e:
            return (False, str(e))
    else:
        try:
            with open(filename, 'r') as fileobj:
                data = fileobj.read()
                return (True, data)
        except Exception as e:
            return (False, str(e))


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")
    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(secure_archive('/not/existing/file', "read"))
    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive('/etc/master.passwd', "read"))
    print("\nUsing 'secure_archive' to read from a regular file:")
    print(secure_archive('test.txt', "read"))
    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive('test2.txt', "write"))
