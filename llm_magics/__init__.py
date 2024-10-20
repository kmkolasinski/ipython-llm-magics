def load_ipython_extension(ipython):  # type: ignore
    from llm_magics.ipython import LLMMagics

    magic = LLMMagics(ipython)
    ipython.register_magics(magic)
