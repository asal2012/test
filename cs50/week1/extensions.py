extensions = {"gif":"image/gif", "jpg":"image/jpeg", "jpeg":"image/jpeg",
              "png":"image/png", "zip":"application/zip",
              "pdf":"application/pdf","txt":"text/plain"}

file = input("file name: ").strip().lower()
if file[-3:] in extensions:
    print(extensions[file[-3:]])
elif file[-4:] in extensions:
    print(extensions[file[-4:]])
else:
    print("application/octet-stream")