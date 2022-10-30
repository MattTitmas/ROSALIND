class ReadFasta:
    def __init__(self, file_location: str) -> None:
        """
        Initialse the class
        :param file_location: Location of fasta file
        :return: None
        """
        with open(file_location, 'r') as f:
            data = [i.removesuffix('\n') for i in f.readlines()]

        for i in range(len(data) - 1, 0, -1):
            if not data[i].startswith('>') and not data[i - 1].startswith('>'):
                data[i - 1] += data[i]
                del data[i]

        self.data = data

    def get_dictionary(self):
        return {
            self.data[i]: self.data[i+1] for i in range(0, len(self.data), 2)
        }

    def get_list(self):
        return [self.data[i] for i in range(1, len(self.data), 2)]