from argparse import ArgumentParser

from my_module import HelloClass, __version__, say_hello_lots


def main(args=None):
    parser = ArgumentParser()
    parser.add_argument("--version", action="version", version=__version__)
    parser.add_argument("name", help="Name of the person to greet")
    parser.add_argument("--times", type=int, default=5, help="Number of times to greet")
    args = parser.parse_args(args)
    say_hello_lots(HelloClass(args.name), args.times)


if __name__ == "__main__":
    # test with:
    #     pipenv run python -m my_module.cli
    main()
