# encoding: utf-8
# author: wm-chen
# clover_utils.py
# 2021/7/23 5:25 下午
# desc:
import json
from web3 import Web3
from CLover_Ui_Test.clover_app.common.clv_contract import ClvAbi
# ROUND_HALF_UP 四舍五入   ROUND_FLOOR 舍去 ROUND_CEILING 入
from decimal import Decimal, ROUND_HALF_UP, ROUND_FLOOR


class CloverUtils:

    def __init__(self, provider_type):
        self.provider_type = provider_type
        if self.provider_type == 'eth':
            self.w3 = Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/e4dabe201ff242b9b19e8d02e8d207e1'))
            self.abi = json.loads(ClvAbi.eth_clv['result'])
        elif self.provider_type == 'clv':
            self.w3 = Web3(Web3.HTTPProvider('https://rpc-3.clover.finance'))
        elif self.provider_type == 'bsc':
            self.w3 = Web3(Web3.HTTPProvider('https://data-seed-prebsc-1-s1.binance.org:8545'))
            self.abi = json.loads(ClvAbi.bsc_clv['result'])

    def token_balance(self, _address, token_address=None):
        if not token_address:
            return format(self.get_balance(_address), ',')
        else:
            return format(self.get_erc20_balance(_address, token_address), ',')

    def get_balance(self, _address):
        check_address = self.w3.toChecksumAddress(_address)
        _balance = self.w3.eth.get_balance(check_address)
        return Decimal(str(self.w3.fromWei(_balance, 'ether'))).quantize(Decimal('0.000'), rounding=ROUND_FLOOR)

    def get_erc20_balance(self, _address, token_address):
        check_address = self.w3.toChecksumAddress(_address)
        if not self.w3.isChecksumAddress(token_address):
            token_address = self.w3.toChecksumAddress(token_address)
        source_code = self.w3.eth.get_code(token_address)
        contract = self.w3.eth.contract(abi=self.abi, address=token_address, bytecode=source_code)
        _balance = contract.functions.balanceOf(check_address).call()
        return Decimal(str(self.w3.fromWei(_balance, 'ether'))).quantize(Decimal('0.000'), rounding=ROUND_FLOOR)


if __name__ == '__main__':
    address = '0x4814c94a4e8e876750b3512d657ee79266566591'
    eth_clv_address = '0x654F17eAB141F47Ee882CA762dcFDEFA9EefD237'
    bsc_clv_address = '0x7c9b951d88fa66820fb3b62e5800d5e82fd490b3'
    balance1 = CloverUtils('eth').get_erc20_balance(address, eth_clv_address)
    balance2 = CloverUtils('clv').get_balance(address)
    balance3 = CloverUtils('bsc').get_erc20_balance(address, bsc_clv_address)
    print(balance1)
    print(balance2)
    print(balance3)
    network = CloverUtils('clv').w3
    print(network.toInt(0x91ede7))