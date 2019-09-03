from pathlib import Path

from submission import my_submission

class Submission(object):
    def run(self, test_file, out_file):
        """This is boilerplate. Delete the contents of this method and put your
        own code here. Please do not change the class name (Submission),
        the method name (run), or the arguments.
        """
        my_submission(test_file, out_file)


# Please do not change anything below
if __name__ == "__main__":
    # These are the default file paths (names) for input and output
    test_file = Path('/')/'data'/'input'/'test_data'
    out_file = Path('/')/'data'/'output'

    Submission().run(test_file, out_file)

