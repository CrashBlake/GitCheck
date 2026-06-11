### This module is responsible for parsing command-line arguments and invoking the appropriate functions based on the user's input. It uses the argparse library to handle command-line arguments and provides a clean interface for users to interact with the GitCheck tool.

import argparse
from core.logic import event_process

def build_parser():
    parser = argparse.ArgumentParser(description="GitCheck - A tool to check if a GitHub user has made any commits in the last 24 hours.")
    parser.add_argument("Username", default=None, help="The GitHub username to check.")
    parser.set_defaults(func=handle)
    return parser

def handle(args):
    event_process(args.Username)