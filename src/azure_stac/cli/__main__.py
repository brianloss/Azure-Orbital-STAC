# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import sys

from azure_stac.core import get_default_cli


def main() -> int:
    # instantiation our stac cli here
    stac_cli = get_default_cli()

    try:
        # invoke the stac cli and pass the arguments to it
        return stac_cli.invoke(sys.argv[1:])

    except KeyboardInterrupt:
        # if there is a keyboard interruption, then exit with code 1
        sys.exit(1)

    except SystemExit as ex:
        # if there system exit, then use the exit code in the exception
        # otherwise, use exit code 1 if there is no exit code in the
        # exception being thrown
        ex.code = ex.code if ex.code is not None else 1
        raise ex


if __name__ == "__main__":
    main()
