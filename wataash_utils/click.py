# SPDX-License-Identifier: Apache-2.0

import logging

import click


def parse_quiet_verbose(ctx: click.Context, quiet: bool, verbose: int) -> int:
    if quiet and verbose:
        msg = '--quiet and --verbose are mutually exclusive'
        raise click.UsageError(msg, ctx=ctx)
    if quiet:
        return logging.ERROR
    elif verbose == 0:
        return logging.WARNING
    elif verbose == 1:
        return logging.INFO
    elif verbose >= 2:
        return logging.DEBUG
