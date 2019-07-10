class TextReader:
    """Support for reading old Java SKM file format"""

    @staticmethod
    def read(input_file, delimiter):
        """Read the input file line by line and try to extract key/game/notes info"""

        # Set up an list to store results
        game_key_list = []

        # Now comes the interesting part: since the pre-QSKM text storage format is chaotic at best,
        # there is no way to guarantee if the lines are properly segregated, nor the positions of
        # tokens. Here we assume that the lines are delimited by semicolons (;) (or the user-supplied
        # delimiter).
        if delimiter is None:
            delimiter = ';'

        # Read line by line and
        with open(input_file) as fp:
            file_content = fp.readlines()

            # Read a few lines and determine if (1) the delimiter is valid, and (2) the arrangement
            # of the elements.
            for i in range(0, 9):
                # Skip empty lines
                if not file_content[i].strip():
                    tokens = file_content[i].split(delimiter)
                    # If it's smaller than 2, definitely it's not the right separator...
                    if len(tokens) < 2:
                        continue
                    if len(tokens) == 2:
                        TextReader.parse_two_cols(file_content)
                        break
                    if len(tokens) == 3:
                        TextReader.parse_three_cols(file_content)
                        break
                    else:
                        continue

    @staticmethod
    def parse_two_cols(content):
        pass

    @staticmethod
    def parse_three_cols(content):
        pass
