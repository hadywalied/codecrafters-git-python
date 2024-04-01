import sys
import os
import zlib, re


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    # print("Logs from your program will appear here!")

    # Uncomment this block to pass the first stage
    #
    command = sys.argv[1]
    if command == "init":
        os.mkdir(".git")
        os.mkdir(".git/objects")
        os.mkdir(".git/refs")
        with open(".git/HEAD", "w") as f:
            f.write("ref: refs/heads/main\n")
        print("Initialized git directory")

    elif command == "cat-file":
        option = sys.argv[2]
        file = sys.argv[3]
        if option == "-p":
            with open(f".git/objects/{file[:2]}/{file[2:]}", "rb") as file:
                content = file.read()
            decompressed_content = zlib.decompress(content)
            text_data = decompressed_content.decode("utf-8")
            filtered_data = re.sub(r"^.*?\x00", "", text_data)
            print(filtered_data, end="")
    else:
        raise RuntimeError(f"Unknown command #{command}")


if __name__ == "__main__":
    main()
