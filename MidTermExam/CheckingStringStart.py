def checking_prefix(string , prefix):
    string = string.lower()
    if string.startswith(prefix):
        return True
    else:
        return False
string = input("Input string: ")
prefix = input("Input prefix: ")
print(checking_prefix(string, prefix))