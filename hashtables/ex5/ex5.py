# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    files_found = []

    directory = dict()

    for file in files:

        # filename is last part of path
        parts = file.split("/")
        filename = parts[-1]
        
        # create a new entry in the dictionary if needed
        if filename not in directory:
            directory[filename] = []
        
        # add current path to dictionary with the filename as the key
        directory[filename].append(file)

    # go through each query
    for query in queries:

        # if the file was found, add all the paths to the result to return
        if query in directory:
            files_found.extend(directory[query])

    return files_found


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
