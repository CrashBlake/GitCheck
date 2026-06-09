import argparse
from core.logic import event_print

def build_parser():
    parser = argparse.ArgumentParser(description="GitCheck - A tool to check if a GitHub user has made any commits in the last 24 hours.")
    parser.add_argument("--GitCheck", default=None, help="The GitHub username to check.")
    parser.set_defaults(func=handle)
    return parser

def handle(args):
    event_print(args.GitCheck)