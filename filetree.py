import os


def print_decorline(chars, length, keep_whole=True):
    decorline = ""
    while True:
        decorline += chars
        if len(decorline) >= length:
            if keep_whole:
                side = length % len(chars)
                decorline = decorline[0:length-side]
            break
    print(decorline)


""" def filetree2(root, path="", exep=[".py", ".md"]):

    # Stop if this is not a folder:
    if not os.path.isdir(root):
        return

    # Get files in current folder:
    files_and_dirs = sorted(os.listdir(root))
    files_and_dirs_filtered = [item for item in files_and_dirs if (not item.startswith(".") and
                                                 not os.path.splitext(item)[1] in exep)]
    nfiles = len(files_and_dirs_filtered)
    files_filtered = [elem for elem in files_and_dirs_filtered if os.path.isfile(os.path.join(path, elem))]
    dirs_filtered = [elem for elem in files_and_dirs_filtered if os.path.isdir(os.path.join(path, elem))]

    # Print the content of the current folder:
    newpath = path + "|   "
    arrow = "|-- "
    for i in range(nfiles):
        if i == nfiles - 1:
            newpath = path + "    "
            arrow = "`---- "
        print("{:s}{:s}{:s}".format(path, arrow, files_and_dirs_filtered[i]))
        # Recursive call to print the content of sub-folders:
        filetree2("{:s}/{:s}".format(root, files_and_dirs_filtered[i-1]), newpath, exep) """


def filetree(root, path="", exep=[".py", ".md"]):

    # Stop if this is not a folder:
    if not os.path.isdir(root):
        return

    # Get files in current folder:
    files_and_dirs = sorted(os.listdir(root))
    files_and_dirs_filtered = [item for item in files_and_dirs if (not item.startswith(".") and
                                                 not os.path.splitext(item)[1] in exep)]
    length_of_files_and_dirs_filtered = len(files_and_dirs_filtered)

    # Print the content of the current folder:
    newpath = path + "|   "
    arrow = "|-- "
    for i in range(length_of_files_and_dirs_filtered):
        if i == length_of_files_and_dirs_filtered - 1:
            newpath = path + "    "
            arrow = "`-- "
        print("{:s}{:s}{:s}".format(path, arrow, files_and_dirs_filtered[i]))
        filetree("{:s}/{:s}".format(root, files_and_dirs_filtered[i]), newpath, exep)


def main():
    print("The contents of the current folder are:")
    print_decorline("*--*", 32)
    filetree(".")
    print_decorline("*--*", 32)


if __name__ == '__main__':
    main()
