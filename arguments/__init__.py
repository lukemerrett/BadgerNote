import argparse

def GetArguments():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-ln', '--list-notes',
        dest='list_notes',    # Result stored in a variable of this name
        action='store_true',  # Means we don't expect this flag key to come with a value
        help='Lists the current notes'
    )

    parser.add_argument(
        '-c', '--create-note',
        dest="create_note",
        nargs=2,  # Expect 2 arguments to follow; title and body
        help='Creates a new note',
        metavar=('"Title"', '"Body"')
    )

    return parser.parse_args()
