from llama_models.llama3.reference_impl.generation import Llama
from typing import Optional
from config import ModelConfig


# Load the model
def load_generator(
        ckpt_dir: str = ModelConfig.CKPT_DIR,
        max_seq_len: int = ModelConfig.MAX_SEQ_LEN,
        max_batch_size: int = ModelConfig.MAX_BATCH_SIZE,
        model_parallel_size: Optional[int] = ModelConfig.MODEL_PARALLEL_SIZE,
):
    return Llama.build(
        ckpt_dir=ckpt_dir,
        max_seq_len=max_seq_len,
        max_batch_size=max_batch_size,
        model_parallel_size=model_parallel_size,
    )


def truncate_dialog(dialog, max_length):
    """Truncate dialog for correspond limit token."""
    total_tokens = 0
    truncated_dialog = []
    for message in reversed(dialog):
        message_tokens = len(message.content.split())
        if total_tokens + message_tokens <= max_length:
            truncated_dialog.insert(0, message)
            total_tokens += message_tokens
        else:
            break
    return truncated_dialog
