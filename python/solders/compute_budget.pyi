from solders.instruction import Instruction
from solders.pubkey import Pubkey

ID: Pubkey

def request_heap_frame(bytes_: int) -> Instruction: ...
def set_compute_unit_limit(units: int) -> Instruction: ...
def set_compute_unit_price(micro_lamports: int) -> Instruction: ...

class ComputeBudget:
    def __init__(self) -> None: ...
    @property
    def compute_unit_limit(self) -> int: ...
    @compute_unit_limit.setter
    def compute_unit_limit(self, val: int) -> None: ...
    @property
    def log_64_units(self) -> int: ...
    @log_64_units.setter
    def log_64_units(self, val: int) -> None: ...
    @property
    def create_program_address_units(self) -> int: ...
    @create_program_address_units.setter
    def create_program_address_units(self, val: int) -> None: ...
    @property
    def invoke_units(self) -> int: ...
    @invoke_units.setter
    def invoke_units(self, val: int) -> None: ...
    @property
    def max_instruction_stack_depth(self) -> int: ...
    @max_instruction_stack_depth.setter
    def max_instruction_stack_depth(self, val: int) -> None: ...
    @property
    def max_instruction_trace_length(self) -> int: ...
    @max_instruction_trace_length.setter
    def max_instruction_trace_length(self, val: int) -> None: ...
    @property
    def sha256_base_cost(self) -> int: ...
    @sha256_base_cost.setter
    def sha256_base_cost(self, val: int) -> None: ...
    @property
    def sha256_byte_cost(self) -> int: ...
    @sha256_byte_cost.setter
    def sha256_byte_cost(self, val: int) -> None: ...
    @property
    def sha256_max_slices(self) -> int: ...
    @sha256_max_slices.setter
    def sha256_max_slices(self, val: int) -> None: ...
    @property
    def max_call_depth(self) -> int: ...
    @max_call_depth.setter
    def max_call_depth(self, val: int) -> None: ...
    @property
    def stack_frame_size(self) -> int: ...
    @stack_frame_size.setter
    def stack_frame_size(self, val: int) -> None: ...
    @property
    def log_pubkey_units(self) -> int: ...
    @log_pubkey_units.setter
    def log_pubkey_units(self, val: int) -> None: ...
    @property
    def max_cpi_instruction_size(self) -> int: ...
    @max_cpi_instruction_size.setter
    def max_cpi_instruction_size(self, val: int) -> None: ...
    @property
    def cpi_bytes_per_unit(self) -> int: ...
    @cpi_bytes_per_unit.setter
    def cpi_bytes_per_unit(self, val: int) -> None: ...
    @property
    def sysvar_base_cost(self) -> int: ...
    @sysvar_base_cost.setter
    def sysvar_base_cost(self, val: int) -> None: ...
    @property
    def secp256k1_recover_cost(self) -> int: ...
    @secp256k1_recover_cost.setter
    def secp256k1_recover_cost(self, val: int) -> None: ...
    @property
    def syscall_base_cost(self) -> int: ...
    @syscall_base_cost.setter
    def syscall_base_cost(self, val: int) -> None: ...
    @property
    def curve25519_edwards_validate_point_cost(self) -> int: ...
    @curve25519_edwards_validate_point_cost.setter
    def curve25519_edwards_validate_point_cost(self, val: int) -> None: ...
    @property
    def curve25519_edwards_add_cost(self) -> int: ...
    @curve25519_edwards_add_cost.setter
    def curve25519_edwards_add_cost(self, val: int) -> None: ...
    @property
    def curve25519_edwards_subtract_cost(self) -> int: ...
    @curve25519_edwards_subtract_cost.setter
    def curve25519_edwards_subtract_cost(self, val: int) -> None: ...
    @property
    def curve25519_edwards_multiply_cost(self) -> int: ...
    @curve25519_edwards_multiply_cost.setter
    def curve25519_edwards_multiply_cost(self, val: int) -> None: ...
    @property
    def curve25519_edwards_msm_base_cost(self) -> int: ...
    @curve25519_edwards_msm_base_cost.setter
    def curve25519_edwards_msm_base_cost(self, val: int) -> None: ...
    @property
    def curve25519_edwards_msm_incremental_cost(self) -> int: ...
    @curve25519_edwards_msm_incremental_cost.setter
    def curve25519_edwards_msm_incremental_cost(self, val: int) -> None: ...
    @property
    def curve25519_ristretto_validate_point_cost(self) -> int: ...
    @curve25519_ristretto_validate_point_cost.setter
    def curve25519_ristretto_validate_point_cost(self, val: int) -> None: ...
    @property
    def curve25519_ristretto_add_cost(self) -> int: ...
    @curve25519_ristretto_add_cost.setter
    def curve25519_ristretto_add_cost(self, val: int) -> None: ...
    @property
    def curve25519_ristretto_subtract_cost(self) -> int: ...
    @curve25519_ristretto_subtract_cost.setter
    def curve25519_ristretto_subtract_cost(self, val: int) -> None: ...
    @property
    def curve25519_ristretto_multiply_cost(self) -> int: ...
    @curve25519_ristretto_multiply_cost.setter
    def curve25519_ristretto_multiply_cost(self, val: int) -> None: ...
    @property
    def curve25519_ristretto_msm_base_cost(self) -> int: ...
    @curve25519_ristretto_msm_base_cost.setter
    def curve25519_ristretto_msm_base_cost(self, val: int) -> None: ...
    @property
    def curve25519_ristretto_msm_incremental_cost(self) -> int: ...
    @curve25519_ristretto_msm_incremental_cost.setter
    def curve25519_ristretto_msm_incremental_cost(self, val: int) -> None: ...
    @property
    def heap_size(self) -> int: ...
    @heap_size.setter
    def heap_size(self, val: int) -> None: ...
    @property
    def heap_cost(self) -> int: ...
    @heap_cost.setter
    def heap_cost(self, val: int) -> None: ...
    @property
    def mem_op_base_cost(self) -> int: ...
    @mem_op_base_cost.setter
    def mem_op_base_cost(self, val: int) -> None: ...
    @property
    def alt_bn128_addition_cost(self) -> int: ...
    @alt_bn128_addition_cost.setter
    def alt_bn128_addition_cost(self, val: int) -> None: ...
    @property
    def alt_bn128_multiplication_cost(self) -> int: ...
    @alt_bn128_multiplication_cost.setter
    def alt_bn128_multiplication_cost(self, val: int) -> None: ...
    @property
    def alt_bn128_pairing_one_pair_cost_first(self) -> int: ...
    @alt_bn128_pairing_one_pair_cost_first.setter
    def alt_bn128_pairing_one_pair_cost_first(self, val: int) -> None: ...
    @property
    def alt_bn128_pairing_one_pair_cost_other(self) -> int: ...
    @alt_bn128_pairing_one_pair_cost_other.setter
    def alt_bn128_pairing_one_pair_cost_other(self, val: int) -> None: ...
    @property
    def big_modular_exponentiation_base_cost(self) -> int: ...
    @big_modular_exponentiation_base_cost.setter
    def big_modular_exponentiation_base_cost(self, val: int) -> None: ...
    @property
    def big_modular_exponentiation_cost_divisor(self) -> int: ...
    @big_modular_exponentiation_cost_divisor.setter
    def big_modular_exponentiation_cost_divisor(self, val: int) -> None: ...
    @property
    def poseidon_cost_coefficient_a(self) -> int: ...
    @poseidon_cost_coefficient_a.setter
    def poseidon_cost_coefficient_a(self, val: int) -> None: ...
    @property
    def poseidon_cost_coefficient_c(self) -> int: ...
    @poseidon_cost_coefficient_c.setter
    def poseidon_cost_coefficient_c(self, val: int) -> None: ...
    @property
    def remaining_compute_units_cost(self) -> int: ...
    @remaining_compute_units_cost.setter
    def remaining_compute_units_cost(self, val: int) -> None: ...
    @property
    def alt_bn128_g1_compress(self) -> int: ...
    @alt_bn128_g1_compress.setter
    def alt_bn128_g1_compress(self, val: int) -> None: ...
    @property
    def alt_bn128_g1_decompress(self) -> int: ...
    @alt_bn128_g1_decompress.setter
    def alt_bn128_g1_decompress(self, val: int) -> None: ...
    @property
    def alt_bn128_g2_compress(self) -> int: ...
    @alt_bn128_g2_compress.setter
    def alt_bn128_g2_compress(self, val: int) -> None: ...
    @property
    def alt_bn128_g2_decompress(self) -> int: ...
    @alt_bn128_g2_decompress.setter
    def alt_bn128_g2_decompress(self, val: int) -> None: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __richcmp__(self, other: "ComputeBudget", op: int) -> bool: ...
