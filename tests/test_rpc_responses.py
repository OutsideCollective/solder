from solders.rpc.responses import (
    GetAccountInfoResp,
    GetAccountInfoRespJsonParsed,
    RpcResponseContext,
    RpcError,
)
from solders.account import Account, ParsedAccount, AccountJSON
from solders.pubkey import Pubkey
from based58 import b58decode


def test_get_account_info() -> None:
    raw = """{
  "jsonrpc": "2.0",
  "result": {
    "context": {
      "slot": 1
    },
    "value": {
      "data": [
        "11116bv5nS2h3y12kD1yUKeMZvGcKLSjQgX6BeV7u1FrjeJcKfsHRTPuR3oZ1EioKtYGiYxpxMG5vpbZLsbcBYBEmZZcMKaSoGx9JZeAuWf",
        "base58"
      ],
      "executable": false,
      "lamports": 1000000000,
      "owner": "11111111111111111111111111111111",
      "rentEpoch": 2
    }
  },
  "id": 1
}"""
    parsed = GetAccountInfoResp.from_json(raw)
    context = RpcResponseContext(slot=1)
    value = Account(
        data=b58decode(
            b"11116bv5nS2h3y12kD1yUKeMZvGcKLSjQgX6BeV7u1FrjeJcKfsHRTPuR3oZ1EioKtYGiYxpxMG5vpbZLsbcBYBEmZZcMKaSoGx9JZeAuWf"
        ),
        executable=False,
        lamports=1000000000,
        owner=Pubkey.from_string("11111111111111111111111111111111"),
        rent_epoch=2,
    )
    assert parsed == GetAccountInfoResp(context=context, value=value)


def test_get_account_info_null() -> None:
    raw = '{"jsonrpc":"2.0","result":{"context":{"apiVersion":"1.10.26","slot":146423291},"value":null},"id":1}'
    parsed = GetAccountInfoResp.from_json(raw)
    assert parsed.value is None
    context = RpcResponseContext(slot=146423291, api_version="1.10.26")
    value = None
    assert parsed == GetAccountInfoResp(context=context, value=value)


def test_get_account_info_error() -> None:
    raw = '{"jsonrpc":"2.0","error":{"code":-32602,"message":"Invalid param: WrongSize"},"id":1}'
    parsed = GetAccountInfoResp.from_json(raw)
    error = RpcError(code=-32602, message="Invalid param: WrongSize")
    assert parsed == error


def test_get_account_info_json_parsed() -> None:
    raw = '{"jsonrpc":"2.0","result":{"context":{"apiVersion":"1.10.25","slot":140702417},"value":{"data":{"parsed":{"info":{"isNative":false,"mint":"EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v","owner":"vines1vzrYbzLMRdu58ou5XTby4qAqVRLmqo36NKPTg","state":"initialized","tokenAmount":{"amount":"36010000000","decimals":6,"uiAmount":36010.0,"uiAmountString":"36010"}},"type":"account"},"program":"spl-token","space":165},"executable":false,"lamports":2039280,"owner":"TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA","rentEpoch":325}},"id":1}'
    parsed = GetAccountInfoRespJsonParsed.from_json(raw)
    parsed_account = ParsedAccount(program="spl-token", space=165, parsed='{"info":{"isNative":false,"mint":"EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v","owner":"vines1vzrYbzLMRdu58ou5XTby4qAqVRLmqo36NKPTg","state":"initialized","tokenAmount":{"amount":"36010000000","decimals":6,"uiAmount":36010.0,"uiAmountString":"36010"}},"type":"account"}')
    assert parsed.value.data == parsed_account
    account_json = AccountJSON(lamports=2039280, data=parsed_account, owner=Pubkey.from_string("TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"), executable=False, rent_epoch=325)
    context = RpcResponseContext(slot=140702417, api_version="1.10.25")
    assert parsed == GetAccountInfoRespJsonParsed(context=context, value=account_json)
