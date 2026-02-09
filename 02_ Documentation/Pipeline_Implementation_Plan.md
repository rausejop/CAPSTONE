# Pipeline Implementation Plan: Multi-Modal Intelligence Tool

Based on **ADR-001**, this plan outlines the step-by-step construction of a sequential integrated pipeline optimized for 8GB RAM environments using 2026 tech stack.

## Phase 1: Environment & Foundation
- [ ] **Step 1.1: Virtual Environment Setup**
    - Create a Python 3.14 environment.
    - Install core dependencies: `langchain`, `langchain-community`, `ollama`, `playwright`, `chromadb`, `fastembed`, `beautifulsoup4`, `gtts`, `matplotlib`, `pypdf`.
- [ ] **Step 1.2: Ollama Configuration**
    - Pull models: `llama3.2:3b-instruct-q4_K_M` and `mistral-nemo:12b-instruct-v1-q4_K_M`.
    - Verify Ollama API responsiveness.
- [ ] **Step 1.3: Playwright Initialization**
    - Run `playwright install chromium` for headless scraping.

## Phase 2: Sequential Ingestion (The Collector)
- [ ] **Step 2.1: Web & Social Media Scraper (FUNC04, FUNC02)**
    - Implement a `Scraper` class using `AsyncChromiumLoader` (Playwright) for dynamic content.
    - Integrate `WebBaseLoader` for static sites.
    - Add metadata extraction (URL, Date, Source).
- [ ] **Step 2.2: Document Processor**
    - Implement PDF loading using `PyPDFLoader`.
    - Define chunking strategy (e.g., RecursiveCharacterTextSplitter) with overlaps to maintain context within RAM limits.

## Phase 3: Embedding & Persistence (The Transformer)
- [ ] **Step 3.1: Vector Store Setup (FUNC05)**
    - Initialize `ChromaDB` as a persistent store in `04_Database/chroma_db`.
    - Configure `FastEmbed` for memory-efficient local embeddings.
- [ ] **Step 3.2: Ingestion Logic**
    - Create a script to process chunks: Ingest -> Embed -> Store.
    - Ensure sequential batching to avoid OOM.

## Phase 4: Intelligence & Analysis (The Synthesizer)
- [ ] **Step 4.1: Multi-Modal Analysis Suite**
    - **FUNC01 (Sentiment):** Implement a LangChain chain using Llama 3.2 for sentiment extraction.
    - **FUNC03 (Translation):** Implement zero-shot translation prompts for multi-lingual support.
    - **FUNC05 (Clustering):** Implement logic to group similar documents via vector search and LLM summary labeling. Given an input direcotry with a PDF, move each pdf to the relative Dewey Decimal System directory.
- [ ] **Step 4.2: Theoretical Alignment (ADR-001 Requirement)**
    - Create documentation in `05_Theory/` explaining:
        - 4-bit Quantization benefits.
        - RAG (Retrieval-Augmented Generation) flow.
        - Knowledge Distillation in 3B models.

## Phase 5: Output & Interface (GUI/CLI)
- [ ] **Step 5.1: CLI Implementation (06_GUI_CLI)**
    - Build a verbose logging interface showing the sequential flow status.
    - Integration of `Matplotlib` to generate clusters visualization PNGs.
- [ ] **Step 5.2: Audio Synthesis (FUNC06)**
    - Implement `gTTS` or `Piper` for low-latency summary reading.

## Phase 6: Validation & Cleanup
- [ ] **Step 6.1: RAM Stress Test**
    - Validate that the pipeline stays under the 8GB free RAM ceiling.
    - Use loguru and rich libraries to monitor the statusof every line
- [ ] **Step 6.2: Final Documentation**
    - Update `02_ Documentation/` with user guides and system architecture diagrams.
