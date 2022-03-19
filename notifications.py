# -*- coding: future_fstrings -*-

import collections

from tabulate import tabulate

from omada import Omada


def main():
    omada = Omada()
    omada.login()

    notifications = omada.getSiteNotifications()
    print(
        tabulate(
            notifications,
            headers="keys",
        )
    )

    omada.logout()


if __name__ == "__main__":
    main()
