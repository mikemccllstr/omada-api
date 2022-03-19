# -*- coding: future_fstrings -*-

import collections

from tabulate import tabulate

from omada import Omada


def main():
    omada = Omada()
    omada.login()

    events = omada.getSiteEvents()
    print(
        tabulate(
            events["data"],
            headers="keys",
        )
    )

    omada.logout()


if __name__ == "__main__":
    main()
