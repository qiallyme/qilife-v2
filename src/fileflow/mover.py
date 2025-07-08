"""
src/fileflow/mover.py

Handles the main file processing pipeline: context, rename, move, and record vectors.
"""

def run_full_pipeline(filepath: str, db_manager, context_memory, vector_storage):
    """
    Stub orchestrator for full file processing.
    :param filepath: Path to the file to process.
    :param db_manager: Instance of DatabaseManager for logging reviews.
    :param context_memory: Instance of ContextMemory for embeddings.
    :param vector_storage: Instance of VectorStorage for storing vectors.
    """
    print(f"🔄 Running full pipeline for {filepath}")
    # TODO: Implement actual pipeline steps:
    # 1. Extract text or metadata (use ContentExtractor)
    # 2. Store context embeddings via context_memory
    # 3. Determine new filename and rename (use rename_rules or fileflow logic)
    # 4. Move file to target folder
    # 5. Log entry in database and vector store
