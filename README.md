# TVA Time Authority
A full-stack web3 project on Solana to preserve the memory of humankind with verifiable historical records.

## Overview

- **Smart Contracts**: Rust-based Solana programs developed with Anchor.
- **Frontend**: React/Next.js application with a FAQ-style interface.
- **Backend**: Python FastAPI service integrating an AI model to validate submitted historical versions.

## Directory Structure

```
.
├── .gitignore
├── anchor.toml
├── programs
│   └── time_authority
├── frontend
│   └── ...
└── backend
    └── ...
```

## Setup

### Prerequisites

- Rust & Cargo (https://www.rust-lang.org/tools/install)
- Solana CLI (https://docs.solana.com/cli/install-solana-cli-tools)
- Anchor CLI (https://project-serum.github.io/anchor/getting-started/installation.html)
- Node.js & npm or Yarn (https://nodejs.org/)
- Python 3.8+ and pip

### Smart Contracts

```bash
cd programs/time_authority
cargo build-bpf
# (Optionally) generate keypair and deploy to localnet or other cluster
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```
