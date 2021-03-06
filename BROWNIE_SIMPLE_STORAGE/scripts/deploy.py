from brownie import accounts, config, SimpleStorage, network
import os


def deploy_simple_storage():
    account = get_ccount()
    print(account)
    simple_storage = SimpleStorage.deploy(
        {
            "from": account,
        }
    )
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    update_stored_value = simple_storage.retrieve()
    print(update_stored_value)


def get_ccount():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallet"]["from_key"])


def main():
    deploy_simple_storage()


if __name__ == "__main__":
    main()
