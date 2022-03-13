use pyo3::{basic::CompareOp, prelude::*};
use solana_sdk::{
    instruction::{
        AccountMeta as AccountMetaOriginal, CompiledInstruction as CompiledInstructionOriginal,
        Instruction as InstructionOriginal,
    },
    pubkey::Pubkey as PubkeyOriginal,
};

use crate::{pubkey::Pubkey, RichcmpEqualityOnly};

/// Describes a single account read or written by a program during instruction
/// execution.
///
/// When constructing an [`Instruction`], a list of all accounts that may be
/// read or written during the execution of that instruction must be supplied.
/// Any account that may be mutated by the program during execution, either its
/// data or metadata such as held lamports, must be writable.
///
/// Note that because the Solana runtime schedules parallel transaction
/// execution around which accounts are writable, care should be taken that only
/// accounts which actually may be mutated are specified as writable.
#[pyclass]
#[derive(PartialEq, Debug, Clone)]
pub struct AccountMeta(pub AccountMetaOriginal);
#[pymethods]
impl AccountMeta {
    /// Construct metadata for an account.
    #[new]
    pub fn new(pubkey: &Pubkey, is_signer: bool, is_writable: bool) -> Self {
        let underlying_pubkey = pubkey.0;
        let underlying = if is_writable {
            AccountMetaOriginal::new(underlying_pubkey, is_signer)
        } else {
            AccountMetaOriginal::new_readonly(underlying_pubkey, is_signer)
        };
        underlying.into()
    }

    #[getter]
    pub fn pubkey(&self) -> Pubkey {
        self.0.pubkey.into()
    }

    #[getter]
    pub fn is_signer(&self) -> bool {
        self.0.is_signer
    }

    #[getter]
    pub fn is_writable(&self) -> bool {
        self.0.is_writable
    }

    pub fn __repr__(&self) -> String {
        format!("{:#?}", self)
    }

    pub fn __str__(&self) -> String {
        format!("{:?}", self)
    }

    pub fn __richcmp__(&self, other: &Self, op: CompareOp) -> PyResult<bool> {
        self.richcmp(other, op)
    }
}

impl RichcmpEqualityOnly for AccountMeta {}

impl From<AccountMetaOriginal> for AccountMeta {
    fn from(am: AccountMetaOriginal) -> Self {
        Self(am)
    }
}

#[pyclass]
#[derive(PartialEq, Debug)]
pub struct Instruction(InstructionOriginal);

#[pymethods]
impl Instruction {
    #[new]
    pub fn new(program_id: &Pubkey, data: &[u8], accounts: Vec<AccountMeta>) -> Self {
        let underlying_accounts: Vec<AccountMetaOriginal> =
            accounts.into_iter().map(|x| x.0).collect();
        let underlying =
            InstructionOriginal::new_with_bytes(program_id.0, data, underlying_accounts);
        underlying.into()
    }

    /// Pubkey of the program that executes this instruction.
    #[getter]
    pub fn program_id(&self) -> Pubkey {
        self.0.program_id.into()
    }

    /// Opaque data passed to the program for its own interpretation.
    #[getter]
    pub fn data(&self) -> Vec<u8> {
        self.0.clone().data
    }

    /// Metadata describing accounts that should be passed to the program.
    #[getter]
    pub fn accounts(&self) -> Vec<AccountMeta> {
        self.0
            .accounts
            .clone()
            .into_iter()
            .map(AccountMeta)
            .collect()
    }

    pub fn __repr__(&self) -> String {
        format!("{:#?}", self)
    }

    pub fn __str__(&self) -> String {
        format!("{:?}", self)
    }

    pub fn __richcmp__(&self, other: &Self, op: CompareOp) -> PyResult<bool> {
        self.richcmp(other, op)
    }
}

impl RichcmpEqualityOnly for Instruction {}

impl From<InstructionOriginal> for Instruction {
    fn from(ix: InstructionOriginal) -> Self {
        Self(ix)
    }
}

/// A compact encoding of an instruction.
///
/// A `CompiledInstruction` is a component of a multi-instruction [`Message`],
/// which is the core of a Solana transaction. It is created during the
/// construction of `Message`. Most users will not interact with it directly.
#[pyclass]
#[derive(PartialEq, Eq, Debug)]
pub struct CompiledInstruction(CompiledInstructionOriginal);

#[pymethods]
impl CompiledInstruction {
    #[new]
    pub fn new(program_id_index: u8, data: &[u8], accounts: &[u8]) -> Self {
        CompiledInstructionOriginal::new_from_raw_parts(
            program_id_index,
            data.to_vec(),
            accounts.to_vec(),
        )
        .into()
    }

    pub fn program_id(&self, program_ids: Vec<Pubkey>) -> Pubkey {
        let underlying_pubkeys: Vec<PubkeyOriginal> = program_ids.iter().map(|x| x.0).collect();
        let underlying = *self.0.program_id(&underlying_pubkeys[..]);
        underlying.into()
    }

    /// Index into the transaction keys array indicating the program account that executes this instruction.
    #[getter]
    pub fn program_id_index(&self) -> u8 {
        self.0.program_id_index
    }

    /// Ordered indices into the transaction keys array indicating which accounts to pass to the program.
    #[getter]
    pub fn accounts(&self) -> Vec<u8> {
        self.0.accounts.clone()
    }

    /// The program input data.
    #[getter]
    pub fn data(&self) -> Vec<u8> {
        self.0.data.clone()
    }

    pub fn __repr__(&self) -> String {
        format!("{:#?}", self)
    }

    pub fn __str__(&self) -> String {
        format!("{:?}", self)
    }

    pub fn __richcmp__(&self, other: &Self, op: CompareOp) -> PyResult<bool> {
        self.richcmp(other, op)
    }
}

impl RichcmpEqualityOnly for CompiledInstruction {}

impl From<CompiledInstructionOriginal> for CompiledInstruction {
    fn from(ix: CompiledInstructionOriginal) -> Self {
        Self(ix)
    }
}