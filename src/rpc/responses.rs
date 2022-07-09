#![allow(clippy::large_enum_variant)]
use std::fmt::Display;

use pyo3::{prelude::*, types::PyBytes, PyClass};
use serde::{Deserialize, Serialize};
use serde_with::{serde_as, FromInto};
use solana_sdk::clock::Slot;
use solders_macros::{common_methods, common_methods_rpc_resp, richcmp_eq_only};

use crate::{
    account::{Account, AccountJSON},
    py_from_bytes_general_via_bincode, pybytes_general_via_bincode,
    tmp_account_decoder::UiAccount,
    to_py_err, CommonMethods, PyBytesBincode, PyFromBytesBincode, RichcmpEqualityOnly,
};
// use solana_client::nonblocking::rpc_client;
// use solana_client::rpc_response::Response;
// use solana_rpc::rpc;

// note: the `data` field of the error struct is always None

pub trait CommonMethodsRpcResp<'a>:
    std::fmt::Display
    + std::fmt::Debug
    + PyBytesBincode
    + PyFromBytesBincode<'a>
    + IntoPy<PyObject>
    + Clone
    + Serialize
    + Deserialize<'a>
    + PyClass
{
    fn pybytes<'b>(&self, py: Python<'b>) -> &'b PyBytes {
        self.pybytes_bincode(py)
    }

    fn pystr(&self) -> String {
        self.to_string()
    }
    fn pyrepr(&self) -> String {
        format!("{:#?}", self)
    }

    fn py_from_bytes(raw: &'a [u8]) -> PyResult<Self> {
        Self::py_from_bytes_bincode(raw)
    }

    fn pyreduce(&self) -> PyResult<(PyObject, PyObject)> {
        let gil = Python::acquire_gil();
        let py = gil.python();
        let cloned = self.clone();
        let constructor = cloned.into_py(py).getattr(py, "from_bytes")?;
        Ok((constructor, (self.pybytes(py).to_object(py),).to_object(py)))
    }

    fn py_to_json(&self) -> String {
        serde_json::to_string(self).unwrap()
    }

    fn py_from_json(raw: &'a str) -> PyResult<Resp<Self>> {
        serde_json::from_str(raw).map_err(to_py_err)
    }
}

macro_rules! resp_traits {
    ($name:ident) => {
        impl PyBytesBincode for $name {}
        impl PyFromBytesBincode<'_> for $name {}
        impl RichcmpEqualityOnly for $name {}
        impl Display for $name {
            fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
                write!(f, "{:?}", self)
            }
        }
        impl<'a> CommonMethodsRpcResp<'a> for $name {}
    };
}

#[derive(Debug, PartialEq, Clone, Serialize, Deserialize)]
#[pyclass(module = "solders.rpc.responses", subclass)]
pub struct RpcError {
    /// Code
    #[pyo3(get)]
    pub code: i64,
    /// Message
    #[pyo3(get)]
    pub message: String,
}

#[richcmp_eq_only]
#[common_methods]
#[pymethods]
impl RpcError {
    #[new]
    pub fn new(code: i64, message: &str) -> Self {
        Self {
            code,
            message: message.to_string(),
        }
    }
}

impl RichcmpEqualityOnly for RpcError {}
impl Display for RpcError {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        write!(f, "{:?}", self)
    }
}
pybytes_general_via_bincode!(RpcError);
py_from_bytes_general_via_bincode!(RpcError);
impl<'a> CommonMethods<'a> for RpcError {}

#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
#[pyclass(module = "solders.rpc.responses", subclass)]
pub struct RpcResponseContext {
    #[pyo3(get)]
    pub slot: Slot,
    #[pyo3(get)]
    #[serde(skip_serializing_if = "Option::is_none", default)]
    pub api_version: Option<String>,
}

#[richcmp_eq_only]
#[common_methods]
#[pymethods]
impl RpcResponseContext {
    #[new]
    pub fn new(slot: Slot, api_version: Option<String>) -> Self {
        Self { slot, api_version }
    }
}

impl RichcmpEqualityOnly for RpcResponseContext {}
impl Display for RpcResponseContext {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        write!(f, "{:?}", self)
    }
}
pybytes_general_via_bincode!(RpcResponseContext);
py_from_bytes_general_via_bincode!(RpcResponseContext);
impl<'a> CommonMethods<'a> for RpcResponseContext {}

#[derive(Serialize, Deserialize, Clone, Debug, PartialEq)]
#[serde(untagged)]
pub enum Resp<T: PyClass + IntoPy<PyObject>> {
    Result {
        #[serde(skip)]
        jsonrpc: crate::rpc::requests::V2,
        result: T,
        #[serde(skip)]
        id: u64,
    },
    Error {
        #[serde(skip)]
        jsonrpc: crate::rpc::requests::V2,
        error: RpcError,
        #[serde(skip)]
        id: u64,
    },
}

impl<T: PyClass + IntoPy<PyObject>> IntoPy<PyObject> for Resp<T> {
    fn into_py(self, py: Python<'_>) -> PyObject {
        match self {
            Self::Error { error: e, .. } => e.into_py(py),
            Self::Result { result: r, .. } => r.into_py(py),
        }
    }
}

#[serde_as]
#[derive(Debug, PartialEq, Eq, Serialize, Deserialize, Clone)]
#[pyclass(module = "solders.rpc.responses", subclass)]
pub struct GetAccountInfoResp {
    #[pyo3(get)]
    context: RpcResponseContext,
    #[pyo3(get)]
    #[serde_as(as = "Option<FromInto<UiAccount>>")]
    value: Option<Account>,
}

resp_traits!(GetAccountInfoResp);

#[common_methods_rpc_resp]
#[pymethods]
impl GetAccountInfoResp {
    #[new]
    pub fn new(value: Option<Account>, context: RpcResponseContext) -> Self {
        Self { value, context }
    }
}

#[serde_as]
#[derive(Debug, PartialEq, Eq, Serialize, Deserialize, Clone)]
#[pyclass(module = "solders.rpc.responses", subclass)]
pub struct GetAccountInfoJsonParsedResp {
    #[pyo3(get)]
    context: RpcResponseContext,
    #[pyo3(get)]
    #[serde_as(as = "Option<FromInto<UiAccount>>")]
    value: Option<AccountJSON>,
}

resp_traits!(GetAccountInfoJsonParsedResp);

#[common_methods_rpc_resp]
#[pymethods]
impl GetAccountInfoJsonParsedResp {
    #[new]
    pub fn new(value: Option<AccountJSON>, context: RpcResponseContext) -> Self {
        Self { value, context }
    }
}

#[derive(Debug, PartialEq, Eq, Serialize, Deserialize, Clone)]
#[serde(rename_all = "camelCase")]
#[pyclass(module = "solders.rpc.responses", subclass)]
pub struct GetBalanceResp {
    #[pyo3(get)]
    pub context: RpcResponseContext,
    #[pyo3(get)]
    pub value: u64,
}

resp_traits!(GetBalanceResp);

#[common_methods_rpc_resp]
#[pymethods]
impl GetBalanceResp {
    #[new]
    pub fn new(value: u64, context: RpcResponseContext) -> Self {
        Self { value, context }
    }
}

// The one in solana_client isn't clonable
#[derive(Debug, PartialEq, Eq, Serialize, Deserialize, Clone)]
#[serde(rename_all = "camelCase")]
#[pyclass(module = "solders.rpc.responses", subclass)]
pub struct GetBlockCommitmentResp {
    #[pyo3(get)]
    pub commitment: Option<[u64; 32]>,
    #[pyo3(get)]
    pub total_stake: u64,
}

resp_traits!(GetBlockCommitmentResp);

#[common_methods_rpc_resp]
#[pymethods]
impl GetBlockCommitmentResp {
    #[new]
    pub fn new(commitment: Option<[u64; 32]>, total_stake: u64) -> Self {
        Self {
            commitment,
            total_stake,
        }
    }
}

pub(crate) fn create_responses_mod(py: Python<'_>) -> PyResult<&PyModule> {
    let m = PyModule::new(py, "responses")?;
    m.add_class::<RpcResponseContext>()?;
    m.add_class::<RpcError>()?;
    m.add_class::<GetAccountInfoResp>()?;
    m.add_class::<GetAccountInfoJsonParsedResp>()?;
    m.add_class::<GetBalanceResp>()?;
    m.add_class::<GetBlockCommitmentResp>()?;
    Ok(m)
}