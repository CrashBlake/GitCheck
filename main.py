### This is the main entry point for the GitCheck application. It initializes the command-line interface, parses user input, and invokes the appropriate functions based on the commands provided by the user. The main function serves as the central hub for coordinating the various components of the application, ensuring that user interactions are handled smoothly and efficiently.

from cli.parser import build_parser

def main():
    parser = build_parser()
    args = parser.parse_args()

    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()