import os
# if you will try to run this script as is, it will fail,
# try to import gitmodules and run it again
# import gitmodules
from gitmodules_example_c import c


def main():
    print("This is git submodule 'b' called from " +
          os.path.abspath(".") +
          " and it is going to call main function from its git submodule 'c':")
    c.main()


if __name__ == "__main__":
    main()
