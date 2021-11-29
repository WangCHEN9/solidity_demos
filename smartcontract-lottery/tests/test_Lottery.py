from brownie import Lottery, accounts, config, network
from scripts.helpful_scripts import get_account
from web3 import Web3


def test_get_entrance_fee():
    account = get_account()
    lottery = Lottery.deploy(
        config["networks"][network.show_active()]["eth_usd_price_feed"],
        {"from": account},
    )
    print(lottery.getEntranceFee())
    assert lottery.getEntranceFee() > Web3.toWei(0.010, "ether")
    assert lottery.getEntranceFee() < Web3.toWei(0.015, "ether")
