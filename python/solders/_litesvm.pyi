from pathlib import Path
from typing import Dict, List, Optional, Sequence, Set, Tuple, Union

from solders.account import Account
from solders.clock import Clock
from solders.compute_budget import ComputeBudget
from solders.epoch_rewards import EpochRewards
from solders.epoch_schedule import EpochSchedule
from solders.hash import Hash
from solders.pubkey import Pubkey
from solders.rent import Rent
from solders.signature import Signature
from solders.slot_history import SlotHistory
from solders.stake_history import StakeHistory
from solders.transaction import Transaction, VersionedTransaction
from solders.transaction_metadata import SimulateResult, TransactionResult

class FeatureSet:
    def __init__(self, active: Dict[Pubkey, int], inactive: Set[Pubkey]) -> None: ...
    @property
    def active(self) -> Dict[Pubkey, int]: ...
    @active.setter
    def active(self, val: Dict[Pubkey, int]) -> None: ...
    @property
    def inactive(self) -> Set[Pubkey]: ...
    @inactive.setter
    def inactive(self, val: Set[Pubkey]) -> None: ...
    @staticmethod
    def default() -> "FeatureSet": ...
    @staticmethod
    def all_enabled() -> "FeatureSet": ...
    def is_active(self, feature_id: Pubkey) -> bool: ...
    def activated_slot(self, feature_id: Pubkey) -> Optional[int]: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __richcmp__(self, other: "FeatureSet", op: int) -> bool: ...

class LiteSVM:
    def __init__(self) -> None: ...
    @staticmethod
    def default() -> "LiteSVM": ...
    def set_compute_budget(self, budget: ComputeBudget) -> None: ...
    def set_sigverify(self, sigverify: bool) -> None: ...
    def set_blockhash_check(self, check: bool) -> None: ...
    def set_sysvars(self) -> None: ...
    def set_builtins(self, feature_set: Optional[FeatureSet]) -> None: ...
    def set_lamports(self, lamports: int) -> None: ...
    def set_spl_programs(self) -> None: ...
    def set_transaction_history(self, capacity: int) -> None: ...
    def set_log_bytes_limit(self, limit: Optional[int]) -> None: ...
    def set_precompiles(self, feature_set: Optional[FeatureSet]) -> None: ...
    def minimum_balance_for_rent_exemption(self, data_len: int) -> int: ...
    def get_account(self, pubkey: Pubkey) -> Optional[Account]: ...
    def set_account(self, pubkey: Pubkey, data: Account) -> None: ...
    def get_balance(self, pubkey: Pubkey) -> Optional[int]: ...
    def latest_blockhash(self) -> Hash: ...
    def get_transaction(self, signature: Signature) -> Optional[TransactionResult]: ...
    def airdrop(self, pubkey: Pubkey, lamports: int) -> TransactionResult: ...
    def add_program_from_file(self, program_id: Pubkey, path: Path) -> None: ...
    def add_program(
        self, program_id: Pubkey, program_bytes: Union[bytes, Sequence[int]]
    ) -> None: ...
    def send_transaction(
        self, tx: Union[Transaction, VersionedTransaction]
    ) -> TransactionResult: ...
    def simulate_transaction(
        self, tx: Union[Transaction, VersionedTransaction]
    ) -> SimulateResult: ...
    def expire_blockhash(self) -> None: ...
    def warp_to_slot(self, slot: int) -> None: ...
    def get_compute_budget(self) -> Optional[ComputeBudget]: ...
    def get_clock(self) -> Clock: ...
    def set_clock(self, clock: Clock) -> None: ...
    def get_rent(self) -> Rent: ...
    def set_rent(self, rent: Rent) -> None: ...
    def get_epoch_rewards(self) -> EpochRewards: ...
    def set_epoch_rewards(self, rewards: EpochRewards) -> None: ...
    def get_epoch_schedule(self) -> EpochSchedule: ...
    def set_epoch_schedule(self, schedule: EpochSchedule) -> None: ...
    def get_last_restart_slot(self) -> int: ...
    def set_last_restart_slot(self, slot: int) -> None: ...
    def get_slot_hashes(self) -> List[Tuple[int, Hash]]: ...
    def set_slot_hashes(self, hashes: Sequence[Tuple[int, Hash]]) -> None: ...
    def get_slot_history(self) -> SlotHistory: ...
    def set_slot_history(self, history: SlotHistory) -> None: ...
    def get_stake_history(self) -> StakeHistory: ...
    def set_stake_history(self, history: StakeHistory) -> None: ...
