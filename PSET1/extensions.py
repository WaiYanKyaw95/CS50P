# MIME file types
val = input("File name: ").strip().lower()

num = len(val.split("."))

# print(num)

if num == 1:
    print("application/octet-stream")
else:
    ext = val.split(".")[num-1]
    match ext:
        case "gif" | "png":
            print(f"image/{ext}")
        case "jpg" | "jpeg":
            print("image/jpeg")
        case "pdf" | "zip":
            print(f"application/{ext}")
        case "txt":
            print(f"text/plain")
        case _:
            print("application/octet-stream")

"""
ext = val.split(".")[1]

match ext:
    case "gif" | "jpg" | "jpeg" | "png" | "pdf" | "txt" | "zip":
        print(f"image/{ext}")
    case _:
        print("application/octet-stream")
"""
