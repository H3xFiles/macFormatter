class split:
    filex = None

    def __init__(self, filex):
        self.file = filex

    def __splitter(self):
        fileName = self.file
        with open(fileName, "r") as file:
            output = file.readlines()[1:]
            with open("formated.cvs", "w+") as filex:
                filex.write("MACAddress;EndPointPolicy;IdentityGroup;Description")
                for mac in output:
                    string = mac.split(";;")[0].replace(".", "")
                    '''Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers 
                    which you can get an iterator from.'''
                    interx = iter(string)
                    '''The zip() function returns a zip object, which is an iterator of tuples where the first item in 
                    each passed iterator is paired together'''
                    formatted = ':'.join(a + b for a, b in zip(interx, interx))
                    filex.write(formatted + ";;" + mac.split(";;")[1])

        file.close()


def main():
    split("mac_import_working_doc.csv")
if __name__ == '__main__':
    main()
