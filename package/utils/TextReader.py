from .RegexWrapper import RegexWrapper
from ..Prompts import Prompts


class TextReader:
    """Support for reading old Java SKM file format"""

    @staticmethod
    def read(input_file, delimiter=None):
        """Read the input file line by line and try to extract key/game/notes info"""

        # Here's the interesting part: since the pre-QSKM text storage format is chaotic at best,
        # there is no way to guarantee if the lines are properly segregated, nor the positions of
        # tokens. Here we assume that the lines are delimited by semicolons (;) (or the user-supplied
        # delimiter).
        if delimiter is None:
            delimiter = ';'

        # Read line by line and
        with open(input_file, encoding='utf-8-sig') as fp:
            file_content = fp.read().splitlines()

            # Read a few lines and determine if (1) the delimiter is valid, and (2) the arrangement
            # of the elements.
            for i in range(0, len(file_content)):
                # Skip empty lines
                if len(file_content[i].strip()) != 0:
                    tokens = file_content[i].split(delimiter)

                    # Parse the file if it finds a line containing 2 or 3 entries
                    if len(tokens) == 2 or len(tokens) == 3:
                        col_key = TextReader.__determine_column_arrangement(file_content, delimiter, i)
                        return TextReader.__parse_file(file_content, delimiter, i, col_key)
                    # If it's smaller than 2 or greater than three, definitely it's not the right separator...
                    else:
                        continue
        # TODO: ask user what to do if none of the line seems to be working
        return []

    @staticmethod
    def __determine_column_arrangement(content, delimiter, first_row):
        """Here we a line and figure out which column are the key/game on"""
        # Only col 1 and 2 will be tested. Col 3 (if exists) will always be regarded as comments
        tokens = content[first_row].split(delimiter)
        col_key = -1

        # Check each cols against predefined regex
        if RegexWrapper.is_key(tokens[0]):
            col_key = 0
        elif RegexWrapper.is_key(tokens[1]):
            col_key = 1
        # TODO If none matches, ask user which col is the key resided

        return col_key

    @staticmethod
    def __parse_file(content, delimiter, start, col_key):
        """Here we do actual file parsing."""
        # Set up an list to store results
        game_key_list = []
        lines_parsed = 0

        # Set the game column
        if col_key == 1:
            col_game = 0
        else:
            col_game = 1

        for i in range(start, len(content)):
            tokens = content[i].split(delimiter)

            if len(tokens) >= 2:
                game_entry = {'game': tokens[col_game],
                              'key': tokens[col_key],
                              'notes': ''}
                if len(tokens) == 3:
                    game_entry['notes'] = tokens[2]

                game_key_list.append(game_entry)
                lines_parsed += 1
        Prompts.show_lines_parsed(lines_parsed)
        return game_key_list
