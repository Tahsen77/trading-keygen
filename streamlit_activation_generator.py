"""
Smart Vault Pro - Official License Activation Key Generator & Validator
=======================================================================
Compatible with Smart Vault Android App (2026 Edition)

Security Protocol:
- Secret Salt: TAHSEEN_TRADING_VAULT_2026
- Algorithm: SHA-256
- Digest Format: Uppercase Hexadecimal (64 characters)
- Formula: hashlib.sha256(f"{device_id.strip()}_{SECRET_SALT}".encode('utf-8')).hexdigest().upper()
"""

import sys
import hashlib
from typing import Tuple

SECRET_SALT = "TAHSEEN_TRADING_VAULT_2026"

MASTER_KEYS = {
    "VAULT-80-VIP-2026",
    "SMART-VAULT-PRO-80",
    "SV-PRO-USDT-2026"
}


def generate_activation_key(device_id: str) -> str:
    """Generates the official activation key for a given Device ID."""
    clean_id = device_id.strip()
    if not clean_id:
        return ""
    payload = f"{clean_id}_{SECRET_SALT}".encode('utf-8')
    hash_object = hashlib.sha256(payload)
    return hash_object.hexdigest().upper()


def verify_activation_key(device_id: str, entered_key: str) -> Tuple[bool, str]:
    """Validates an entered activation key against a user's Device ID."""
    clean_key = entered_key.strip().upper()
    clean_device_id = device_id.strip()

    if not clean_device_id:
        return False, "Device ID is missing or empty."
    if not clean_key:
        return False, "Activation Key is empty."

    if clean_key in MASTER_KEYS:
        return True, "Valid (Master Bypass License Key)"

    expected_key = generate_activation_key(clean_device_id)
    expected_upper = generate_activation_key(clean_device_id.upper())

    if clean_key == expected_key or clean_key == expected_upper:
        return True, "Valid (Device-Bound SHA-256 License)"

    return False, "Invalid Key (Signature does not match Device ID)"


# Streamlit Web UI
try:
    import streamlit as st
    HAS_STREAMLIT = True
except ImportError:
    HAS_STREAMLIT = False


def run_streamlit_app():
    if not HAS_STREAMLIT:
        print("[ERROR] Streamlit is not installed. Run 'pip install streamlit'.")
        return

    st.set_page_config(page_title="Smart Vault Pro — License Generator", page_icon="🔐", layout="centered")

    st.markdown("""
        <style>
        .stApp { background-color: #0B0E14; color: #E2E8F0; }
        .main-header { text-align: center; padding: 1.5rem 0; border-bottom: 1px solid #1E293B; margin-bottom: 2rem; }
        .main-header h1 { color: #FFD700; font-size: 2.2rem; font-weight: 800; }
        .main-header p { color: #94A3B8; font-size: 0.95rem; }
        .key-box {
            background: linear-gradient(135deg, #131A2A 0%, #1A2234 100%);
            border: 1px solid #FFD700;
            border-radius: 12px;
            padding: 1.25rem;
            margin: 1.25rem 0;
            box-shadow: 0 4px 20px rgba(255, 215, 0, 0.15);
        }
        .key-text {
            font-family: 'Courier New', Courier, monospace;
            color: #38BDF8;
            font-size: 1.15rem;
            font-weight: bold;
            word-break: break-all;
            user-select: all;
        }
        </style>
        <div class="main-header">
            <h1>🔐 Smart Vault Pro</h1>
            <p>Cryptographic License Key Generator & Validator (2026 Edition)</p>
        </div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["⚡ Single Key Generator", "🔍 Key Validator / Checker", "📋 Batch Generator"])

    with tab1:
        st.subheader("Generate Device License")
        device_id_input = st.text_input("User Device ID", placeholder="e.g. SV-7B3A-4F91-C82D")
        auto_uppercase = st.checkbox("Auto-uppercase Device ID", value=True)

        if st.button("Generate License Key 🔑", type="primary", use_container_width=True):
            clean_id = device_id_input.strip()
            if auto_uppercase:
                clean_id = clean_id.upper()

            if not clean_id:
                st.error("⚠️ Please enter a valid Device ID.")
            else:
                key = generate_activation_key(clean_id)
                st.success("✅ Activation Key Generated Successfully!")
                st.markdown(f'<div class="key-box"><div class="key-text">{key}</div></div>', unsafe_allow_html=True)
                st.code(key, language="text")

                msg = (
                    f"Hello! Here is your official Smart Vault Pro lifetime license key:\n\n"
                    f"Device ID: {clean_id}\n"
                    f"License Key: {key}\n\n"
                    f"Paste this key into the app to unlock all VIP features immediately!"
                )
                st.text_area("Ready-to-send Customer Message", value=msg, height=130)

    with tab2:
        st.subheader("Verify License Key")
        test_device_id = st.text_input("Device ID to Check", placeholder="e.g. SV-7B3A-4F91-C82D")
        test_key = st.text_input("Activation Key to Test", placeholder="Paste the 64-character hex key here...")

        if st.button("Verify Key Integrity 🛡️", use_container_width=True):
            is_valid, message = verify_activation_key(test_device_id, test_key)
            if is_valid:
                st.success(f"MATCH: {message}")
            else:
                st.error(f"MISMATCH: {message}")

    with tab3:
        st.subheader("Batch Key Generator")
        batch_input = st.text_area("Device IDs (One per line)", height=150)
        if st.button("Generate All Keys 🚀", use_container_width=True):
            lines = [line.strip() for line in batch_input.splitlines() if line.strip()]
            if lines:
                results = [f"{d_id} => {generate_activation_key(d_id)}" for d_id in lines]
                st.text_area("Generated Results", value="\n".join(results), height=200)

    st.caption(f"🔒 Salt: `{SECRET_SALT}` | Hash: `SHA-256` | Smart Vault Engine v2.0")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] not in ("--help", "-h"):
        arg = sys.argv[1].strip()
        print(f"Device ID:      {arg}")
        print(f"Activation Key: {generate_activation_key(arg)}")
    elif HAS_STREAMLIT and "streamlit" in sys.modules:
        run_streamlit_app()
    else:
        run_streamlit_app()