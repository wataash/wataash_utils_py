# SPDX-License-Identifier: Apache-2.0

import argparse
import logging
import re
import typing as t

import wataash_utils as wu


def opts_exclusive(parser: argparse.ArgumentParser, *args: t.Tuple[str, bool]):
    args = [x[0] for x in args if x[1]]
    if len(args) in [0, 1]:
        return
    message = f'{wu.str.cat_and(args)} are mutually exclusive'
    parser.error(message)


def opts_need_any(parser: argparse.ArgumentParser, *args: t.Tuple[str, bool]):
    if len(args) in [0, 1]:
        raise Exception(f'len(args):{len(args)} must be >= 2')
    if len([True for x in args if x[1]]) != 0:
        return
    message = f'one of following options needed: {wu.str.cat_or([x[0] for x in args])}'
    parser.error(message)


def parse_date_ym_slash(parser: argparse.ArgumentParser, ym, opt: t.Optional[str] = None) -> t.Tuple[int, int]:
    """'2006/01/02' -> (2006, 1)"""
    match = re.search(r'^(\d{4})/(\d\d)$', ym)
    if match is not None:
        return tuple(map(int, match.groups()))
    if opt is None:
        opt = 'argument'
    message = f'invalid {opt}: {ym} (must be form of YYYY/MM)'
    parser.error(message)


def parse_date_ymd_slash(parser: argparse.ArgumentParser, ymd: str, opt: t.Optional[str] = None) -> t.Tuple[int, int, int]:
    """'2006/01/02' -> (2006, 1, 2)"""
    match = re.search(r'^(\d{4})/(\d\d)/(\d\d)$', ymd)
    if match is not None:
        return tuple(map(int, match.groups()))
    if opt is None:
        opt = 'argument'
    message = f'invalid {opt}: {ymd} (must be form of "YYYY/MM/DD")'
    parser.error(message)


def parse_quiet_verbose(parser: argparse.ArgumentParser, quiet: bool, verbose: int) -> int:
    if quiet and verbose:
        message = '--quiet and --verbose are mutually exclusive'
        parser.error(message)
    if quiet:
        return logging.ERROR
    elif verbose == 0:
        return logging.WARNING
    elif verbose == 1:
        return logging.INFO
    elif verbose >= 2:
        return logging.DEBUG
