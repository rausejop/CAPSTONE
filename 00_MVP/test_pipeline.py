"""
Integration Test Script.
Validates the flow: Ingestion -> Transformation -> VDB -> Intelligence -> Analytics -> Output.
"""
import asyncio
from m1_ingestion import IngestionManager
from m2_transformer import TransformationManager
from m3_vdb import VectorDBManager
from m4_intelligence import IntelligenceManager
from m5_analytics import AnalyticsManager
from m6_output import OutputManager

async def run_full_test():
    # 1. Initialize Managers
    print("--- Initializing Pipeline ---")
    m1 = IngestionManager(whitelist=["example.com", "reuters.com"])
    m2 = TransformationManager()
    m3 = VectorDBManager()
    m4 = IntelligenceManager()
    m5 = AnalyticsManager(n_clusters=2)
    m6 = OutputManager()

    # 2. Execution Flow
    m6.log_event("Starting Integration Test SYS-01")

    # M1: Ingestion
    # Simulamos un texto capturado (para no depender de internet en el test rápido)
    raw_text = "Tensions between USA and Iran escalate over maritime security in the Gulf."
    m6.log_event("M1: Data Captured")

    # M2: Transformation (Hashing & Standardizing)
    structured_data = m2.process_payload(raw_text, {"url": "https://example.com/news1"})
    m6.log_event(f"M2: Data Transformed with Hash: {structured_data['source_id']}")

    # M3: Vector Storage
    m3.add_to_vector_store(structured_data)
    m6.log_event("M3: Data Indexed in ChromaDB")

    # M4: Intelligence (Sentiment)
    sentiment = m4.analyze_sentiment(structured_data['content'])
    m6.log_event(f"M4: Sentiment Identified: {sentiment['sentiment']}")

    # M5: Analytics (Clustering)
    # Simulamos varios vectores para el test de cluster
    mock_embeddings = [[0.1] * 384, [0.2] * 384, [0.9] * 384] 
    labels = m5.perform_clustering(mock_embeddings)
    m5.visualize_clusters(mock_embeddings, labels, ["Doc1", "Doc2", "Doc3"])
    m6.log_event("M5: Cluster Map Generated")

    # M6: Output
    report = m6.generate_final_report(structured_data, sentiment)
    print(report)
    m6.text_to_speech("Pipeline test completed successfully. Intelligence report is ready.")
    
    print("--- Test Finished: Check /data folder for logs and audio ---")

if __name__ == "__main__":
    asyncio.run(run_full_test())