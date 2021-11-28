from brownie import SimpleStorage, accounts, config


def read_contract():
    simple_storage = SimpleStorage[-1]  # get latest deploy contract
    print(simple_storage.retrieve())


def main():
    read_contract()


if __name__ == "__main__":
    main()
