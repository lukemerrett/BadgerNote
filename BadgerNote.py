__author__ = "Luke Merrett"

import arguments
import operations

args = arguments.GetArguments()

if args.list_notes:
    operations.print_list_of_notes()

if args.create_note:
    operations.create_new_note(args.create_note[0], args.create_note[1])