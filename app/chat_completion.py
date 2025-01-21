from app.ai import load_generator, truncate_dialog
from config import ModelConfig
from llama_models.llama3.api.datatypes import UserMessage, CompletionMessage
from llama_models.llama3.reference_impl.generation import Llama
from typing import Optional


def chat(
        generator: Llama,
        dialog: list,
        user_message: str
):
    # Add user message to dialog
    dialog.append(UserMessage(role="user", content=user_message))
    dialog = truncate_dialog(dialog, ModelConfig.MAX_DIALOG_LENGTH)

    # Generate assistant response
    result = generator.chat_completion(
        dialog,
        max_gen_len=ModelConfig.MAX_GEN_LEN,
        temperature=ModelConfig.TEMPERATURE,
        top_p=ModelConfig.TOP_P,
    )
    return result.generation


def chat_completion(
        ckpt_dir: str,
        model_parallel_size: Optional[int] = None
):
    print(f"Using checkpoint directory: {ckpt_dir}, model_parallel_size: {model_parallel_size}")
    generator = load_generator(ckpt_dir=ckpt_dir, model_parallel_size=model_parallel_size)
    dialog = []
    print("Start a chat. Type 'exit' to quit.")

    while True:
        user_message = input("You: ")
        if user_message.strip().lower() == "exit":
            print("Exiting chat. Goodbye!")
            break

        # Get assistant message
        assistant_message: CompletionMessage = chat(generator, dialog, user_message)
        dialog.append(assistant_message)

        # Print messages
        print(f"Assistant: {assistant_message.content}")
        print("\n==================================\n")
