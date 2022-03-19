# -*- coding: future_fstrings -*-

import collections

from tabulate import tabulate

from omada import Omada


def main():
    omada = Omada()
    omada.login()

    alerts = omada.getSiteAlerts()
    print(
        tabulate(
            alerts["data"],
            headers="keys",
        )
    )

    omada.logout()


if __name__ == "__main__":
    main()
