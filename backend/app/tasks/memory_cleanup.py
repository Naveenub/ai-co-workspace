def cleanup_old_memory(memory_list: list[str], max_length: int = 100):
    # Keep only last `max_length` items
    return memory_list[-max_length:]
