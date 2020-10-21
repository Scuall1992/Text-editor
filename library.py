from typing import Tuple, Optional

def run_search_to_word(s: str, text: str) -> Optional[Tuple[int, int]]: 
    pass

def run_forward_word(s: str, begin: int) -> Optional[Tuple[int, int]]:
    pass

def run_delete_by_text(s: str, text: str) -> Optional[str]:
    pass

def run_delete_by_pointers(s: str, begin: int, end: int) -> Optional[str]:
    pass

def run_add_at_begin(s: str, begin: int, text: str) -> Optional[Tuple[str, int]]:
    pass

def run_copy_to_buffer(s: str, begin: int, end: int) -> Optional[str]:
    pass


funcs = {
    "run_search_to_word": run_search_to_word,
    "run_forward_word":run_forward_word,
    "run_delete_by_text":run_delete_by_text,
    "run_delete_by_pointers":run_delete_by_pointers,
    "run_add_at_begin":run_add_at_begin,
    "run_copy_to_buffer":run_copy_to_buffer,
}