import os


def print_decorline(chars, length, keep_whole=True):
    decorline = ""
    while True:
        decorline += chars
        if len(decorline) >= length:
            if keep_whole:
                decorline = decorline[1:length]
            break
    print(decorline)


""" def filetree2(root, path="", exep=[".py", ".md"]):

    # Stop if this is not a folder:
    if not os.path.isdir(root):
        return

    # Get files in current folder:
    files = sorted(os.listdir(root))
    files_filtered = [item for item in files if (not item.startswith(".") and
                                                 not os.path.splitext(item)[1] in path)]
    nfiles = len(files_filtered)

    # Print the content of the current folder:
    newpath = path + "|   "
    arrow = "|-- "
    for i in range(nfiles):
        if i == nfiles - 1:
            newpath = path + "    "
            arrow = "`---- "
        print("{:s}{:s}{:s}".format(path, arrow, files_filtered[i]))
        # Recursive call to print the content of sub-folders:
        filetree2("{:s}/{:s}".format(root, files_filtered[i-1]), newpath, exep) """


def filetree(path="", prefix_spaces=""):
    dir_marker = "|-- "
    file_marker = "`-- "

    # Get items in the current dir
    entries = os.listdir(path)
    #remove unwanted entries '.git' and '*.py'
    filter_list = ['.git', '.py', '.md', '.vscode']
    # Filtering out every filter list item from the original entries list with this for loop
    for elem in filter_list:
        #Create a new entries list based on old one
        entries = [ item for item in entries if elem not in item ]

    # Stop:if the current dir does not contain newer entries
    """ if len(entries) == 0:
        return """
    # Get files in current folder:
    files = [ entry for entry in entries if os.path.isfile(os.path.join(path, entry)) ]
    files = sorted(files)

    for file in files:
        print(f"{prefix_spaces}{file_marker}{file}")

    # Get dirs in current folder:
    dirs = [ entry for entry in entries if os.path.isdir(os.path.join(path, entry)) ]
    dirs = sorted(dirs)
    for dir in dirs:
        print(f"{prefix_spaces}{dir_marker}{dir}")
        new_path = os.path.join(path, dir)
        filetree(path=new_path, prefix_spaces=prefix_spaces+4*' ')


def main():
    print("The contents of the current folder are:")
    print_decorline("*--*", 30)
    filetree(".")
    print_decorline("*--*", 30)


if __name__ == '__main__':
    main()
