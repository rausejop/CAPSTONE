================================================================================
          PROJECT: MULTI-MODAL GEOPOLITICAL INTELLIGENCE PIPELINE
================================================================================
Version: 1.1 | Date: February 2026 | Environment: Windows 11 (8GB RAM)
================================================================================

1. PROJECT OVERVIEW
--------------------------------------------------------------------------------
This project implements a modular, local intelligence platform designed to 
aggregate, process, and synthesise geopolitical data, with a primary focus 
on USA-Iran relations. The system is architected to operate within a strict 
8GB RAM overhead by employing sequential processing and 4-bit model 
quantization.

The core philosophy follows the "Collector -> Transformer -> Synthesizer" 
modular flow, ensuring data integrity via cryptographic hashing (SHA-256) 
and X.509v3 digital evidence.

2. TECHNICAL SPECIFICATIONS
--------------------------------------------------------------------------------
* Language: Python 3.10+
* Architecture: Micro-Manager Modular Design
* RAM Optimization: 
    - 4-bit Quantization (Llama 3.2 3B via Ollama)
    - Persistent Local Vector Storage (ChromaDB)
    - Explicit memory garbage collection between modules
* Data Standards: UTF-8 encoding, JSON unified structures, text-only parsing.

3. FILE INDEX & DIRECTORY STRUCTURE
--------------------------------------------------------------------------------
Below is the inventory of the project files and their respective functions:

CORE FILES:
- main.py               : The central FastAPI gateway. Standardises 
                          communication between agents and the core engine.
- requirements.txt      : Comprehensive list of dependencies and libraries.
- test_pipeline.py      : Integration script to verify end-to-end functionality.

THE SIX MANAGERS (The Intelligence Pipeline):
- m1_ingestion.py       : THE GATEKEEPER. Uses Playwright for DOM rendering
                          and text-only extraction, bypassing API limits.
- m2_transformer.py     : THE LINGUIST. Handles SHA-256 hashing, X.509v3 
                          integrity evidence, and zero-shot translation.
- m3_vdb.py             : THE MEMORY ARCHITECT. Manages ChromaDB persistence
                          and tokenisation (Tiktoken/BPE/SentencePiece).
- m4_intelligence.py    : THE BRAIN. Executes sentiment analysis and insight
                          generation using Llama 3.2 (3B) via Ollama.
- m5_analytics.py       : THE PATTERN FINDER. Performs K-Means clustering 
                          and generates Matplotlib visualisations.
- m6_output.py          : THE VOICE. Handles system logging and Text-to-Speech
                          (TTS) synthesis for final intelligence delivery.

SUPPORTING DIRECTORIES:
- /data                 : Local storage for ChromaDB, logs, and generated audio.
- /theory               : Conceptual documentation and design records (ADR/SDS).

4. SYSTEM RULES
--------------------------------------------------------------------------------
1. TEXT-ONLY: All binary objects (images/videos/audio) are discarded at M1.
2. INTEGRITY: Every record must be uniquely hashed before indexing.
3. EFFICIENCY: Managers must release memory resources immediately after task
   completion to maintain the 8GB RAM ceiling.

================================================================================
                    END OF PROJECT DOCUMENTATION
================================================================================