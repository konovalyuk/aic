from app.ai import load_generator
from termcolor import cprint
from config import ModelConfig
from typing import Optional


def complete_text(
        ckpt_dir: str,
        model_parallel_size: Optional[int] = None
):
    print(f"Using checkpoint directory: {ckpt_dir}, model_parallel_size: {model_parallel_size}")
    generator = load_generator(ckpt_dir=ckpt_dir, model_parallel_size=model_parallel_size)
    print("Enter text to completion (or write 'exit' to finish):")
    while True:
        prompt = input("Enter text: ")
        if prompt.lower() == "exit":
            print("Quit.")
            break

        result = generator.text_completion(
            prompt,
            temperature=ModelConfig.TEMPERATURE,
            top_p=ModelConfig.TOP_P,
            max_gen_len=ModelConfig.MAX_GEN_LEN,
            logprobs=False,
        )

        cprint(f"{prompt}", end="")
        cprint(f"{result.generation}", color="yellow")
        print("\n==================================\n")
