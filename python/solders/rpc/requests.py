from typing import Sequence, Union

from ..solders import (
    AccountSubscribe,
    AccountUnsubscribe,
    BlockSubscribe,
    BlockUnsubscribe,
    GetAccountInfo,
    GetBalance,
    GetBlock,
    GetBlockCommitment,
    GetBlockHeight,
    GetBlockProduction,
    GetBlocks,
    GetBlocksWithLimit,
    GetBlockTime,
    GetClusterNodes,
    GetEpochInfo,
    GetEpochSchedule,
    GetFeeForMessage,
    GetFirstAvailableBlock,
    GetGenesisHash,
    GetHealth,
    GetHighestSnapshotSlot,
    GetIdentity,
    GetInflationGovernor,
    GetInflationRate,
    GetInflationReward,
    GetLargestAccounts,
    GetLatestBlockhash,
    GetLeaderSchedule,
    GetMaxRetransmitSlot,
    GetMaxShredInsertSlot,
    GetMinimumBalanceForRentExemption,
    GetMultipleAccounts,
    GetProgramAccounts,
    GetRecentPerformanceSamples,
    GetSignaturesForAddress,
    GetSignatureStatuses,
    GetSlot,
    GetSlotLeader,
    GetSlotLeaders,
    GetStakeActivation,
    GetSupply,
    GetTokenAccountBalance,
    GetTokenAccountsByDelegate,
    GetTokenAccountsByOwner,
    GetTokenLargestAccounts,
    GetTokenSupply,
    GetTransaction,
    GetTransactionCount,
    GetVersion,
    GetVoteAccounts,
    IsBlockhashValid,
    LogsSubscribe,
    LogsUnsubscribe,
    MinimumLedgerSlot,
    ProgramSubscribe,
    ProgramUnsubscribe,
    RequestAirdrop,
    RootSubscribe,
    RootUnsubscribe,
    SendLegacyTransaction,
    SendRawTransaction,
    SendVersionedTransaction,
    SignatureSubscribe,
    SignatureUnsubscribe,
    SimulateLegacyTransaction,
    SimulateVersionedTransaction,
    SlotSubscribe,
    SlotsUpdatesSubscribe,
    SlotsUpdatesUnsubscribe,
    SlotUnsubscribe,
    ValidatorExit,
    VoteSubscribe,
    VoteUnsubscribe,
)
from ..solders import (
    batch_requests_to_json as _batch_to_json,
)

Body = Union[
    GetAccountInfo,
    GetBalance,
    GetBlock,
    GetBlockHeight,
    GetBlockProduction,
    GetBlockCommitment,
    GetBlocks,
    GetBlocksWithLimit,
    GetBlockTime,
    GetClusterNodes,
    GetEpochInfo,
    GetEpochSchedule,
    GetFeeForMessage,
    GetFirstAvailableBlock,
    GetGenesisHash,
    GetHealth,
    GetHighestSnapshotSlot,
    GetIdentity,
    GetInflationGovernor,
    GetInflationRate,
    GetInflationReward,
    GetLargestAccounts,
    GetLatestBlockhash,
    GetLeaderSchedule,
    GetMaxRetransmitSlot,
    GetMaxShredInsertSlot,
    GetMinimumBalanceForRentExemption,
    GetMultipleAccounts,
    GetProgramAccounts,
    GetRecentPerformanceSamples,
    GetSignaturesForAddress,
    GetSignatureStatuses,
    GetSlot,
    GetSlotLeader,
    GetSlotLeaders,
    GetStakeActivation,
    GetSupply,
    GetTokenAccountBalance,
    GetTokenAccountsByDelegate,
    GetTokenAccountsByOwner,
    GetTokenLargestAccounts,
    GetTokenSupply,
    GetTransaction,
    GetTransactionCount,
    GetVersion,
    GetVoteAccounts,
    IsBlockhashValid,
    MinimumLedgerSlot,
    RequestAirdrop,
    SendLegacyTransaction,
    SendRawTransaction,
    SendVersionedTransaction,
    ValidatorExit,
    AccountSubscribe,
    BlockSubscribe,
    LogsSubscribe,
    ProgramSubscribe,
    SignatureSubscribe,
    SlotSubscribe,
    SlotsUpdatesSubscribe,
    RootSubscribe,
    VoteSubscribe,
    AccountUnsubscribe,
    BlockUnsubscribe,
    LogsUnsubscribe,
    ProgramUnsubscribe,
    SignatureUnsubscribe,
    SimulateLegacyTransaction,
    SimulateVersionedTransaction,
    SlotUnsubscribe,
    SlotsUpdatesUnsubscribe,
    RootUnsubscribe,
    VoteUnsubscribe,
]


def batch_to_json(reqs: Sequence[Body]) -> str:
    """Serialize a list of request objects into a single batch request JSON.

    Args:
        reqs: A list of request objects.

    Returns:
        str: The batch JSON string.

    Example:
        >>> from solders.rpc.requests import batch_to_json, GetClusterNodes, GetEpochSchedule
        >>> batch_to_json([GetClusterNodes(0), GetEpochSchedule(1)])
        '[{"method":"getClusterNodes","jsonrpc":"2.0","id":0},{"method":"getEpochSchedule","jsonrpc":"2.0","id":1}]'
    """  # noqa: E501
    return _batch_to_json(reqs)


__all__ = [
    "Body",
    "GetAccountInfo",
    "GetBalance",
    "GetBlock",
    "GetBlockHeight",
    "GetBlockProduction",
    "GetBlockCommitment",
    "GetBlocks",
    "GetBlocksWithLimit",
    "GetBlockTime",
    "GetEpochInfo",
    "GetFeeForMessage",
    "GetIdentity",
    "GetInflationGovernor",
    "GetInflationReward",
    "GetLargestAccounts",
    "GetLatestBlockhash",
    "GetLeaderSchedule",
    "GetMinimumBalanceForRentExemption",
    "GetMultipleAccounts",
    "GetProgramAccounts",
    "GetRecentPerformanceSamples",
    "GetSignaturesForAddress",
    "GetSignatureStatuses",
    "GetSlot",
    "GetSlotLeader",
    "GetSlotLeaders",
    "GetStakeActivation",
    "GetSupply",
    "GetTokenAccountBalance",
    "GetTokenAccountsByDelegate",
    "GetTokenAccountsByOwner",
    "GetTokenLargestAccounts",
    "GetTokenSupply",
    "GetTransaction",
    "GetTransactionCount",
    "GetVoteAccounts",
    "IsBlockhashValid",
    "RequestAirdrop",
    "SendLegacyTransaction",
    "SendRawTransaction",
    "SendVersionedTransaction",
    "SimulateLegacyTransaction",
    "SimulateVersionedTransaction",
    "ValidatorExit",
    "AccountSubscribe",
    "BlockSubscribe",
    "LogsSubscribe",
    "ProgramSubscribe",
    "SignatureSubscribe",
    "GetClusterNodes",
    "GetEpochSchedule",
    "GetFirstAvailableBlock",
    "GetGenesisHash",
    "GetHealth",
    "GetHighestSnapshotSlot",
    "GetInflationRate",
    "GetMaxRetransmitSlot",
    "GetMaxShredInsertSlot",
    "GetVersion",
    "MinimumLedgerSlot",
    "SlotSubscribe",
    "SlotsUpdatesSubscribe",
    "RootSubscribe",
    "VoteSubscribe",
    "AccountUnsubscribe",
    "BlockUnsubscribe",
    "LogsUnsubscribe",
    "ProgramUnsubscribe",
    "SignatureUnsubscribe",
    "SlotUnsubscribe",
    "SlotsUpdatesUnsubscribe",
    "RootUnsubscribe",
    "VoteUnsubscribe",
]
