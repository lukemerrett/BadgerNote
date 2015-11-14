# BadgerNote

Lightweight command line note taking program using Python and Sqlite

## Setup

Requires Python 3.4

To install the dependencies ready for use run

    sudo python setup.py develop

## Running the tests

To run all tests for the project; run the following from the root foldeer

    python -m unittest

## Usage

```
usage: python BadgerNote.py [-h] [-ln] [-c "Title" "Body"]
                            [-u "Note ID" "Title" "Body"]

optional arguments:
  -h, --help            show this help message and exit
  -ln, --list-notes     Lists the current notes
  -c "Title" "Body", --create-note "Title" "Body"
                        Creates a new note
  -u "Note ID" "Title" "Body", --update-note "Note ID" "Title" "Body"
                        Updates an existing note
```

