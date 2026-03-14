document_type = input("Type: ")

if document_type.endswith(".pdf" or ".docx" or ".txt"):
    print(True)
else:
    print(False) 