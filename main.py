import tools

def main(file_name):
    counter = tools.Counter(file_name)
    counter.paragraph_counter()
    # counter.results()


if __name__ == '__main__':

    fname = 'sample.txt'
    main(file_name=fname)
