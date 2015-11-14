__author__ = "Luke Merrett"

import settings
import arguments
import operations

operations.setup_database(settings.sqlite_database_name)

args = arguments.GetArguments()

if args.list_notes:
  operations.print_list_of_notes()

if args.create_note:
  operations.create_new_note(args.create_note[0], args.create_note[1])

if args.update_note:
  operations.update_note(args.update_note[0], args.update_note[1], args.update_note[2])
