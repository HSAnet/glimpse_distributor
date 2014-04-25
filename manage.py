#!/usr/bin/env python
import os
import sys

from distributor.common.utils import select_target


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "distributor.settings.%s" % select_target())

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
