from typing import Tuple, Optional


def run_search_to_word(s: str, text: str) -> Optional[Tuple[int, int]]:
    begin = s.find(text)
    if begin == -1:
        return None

    end = begin + len(text)
    return begin, end


def run_forward_word(s: str, begin: int) -> Optional[Tuple[str, int]]:
    if not (0 <= begin < len(s)):
        return None
    begin = min(s.find(" ", begin), s.find("\n", begin))+1
    end = min(s.find(" ", begin), s.find("\n", begin))

    if begin == 0:
        return -1

    return begin, end

def run_backward_word(s: str, begin: int) -> Optional[Tuple[str, int]]:
    if not (0 <= begin < len(s)):
        return None
    begin = max(s.rfind(" ", 0, begin-1), s.rfind("\n", 0, begin-1))+1
    end = min(s.find(" ", begin), s.find("\n", begin))

    if begin == 0:
        return -1

    return begin, end


def run_delete_by_text(s: str, text: str) -> Optional[str]:
    pass


def run_delete_by_pointers(s: str, begin: int, end: int) -> Optional[str]:
    return s[:begin] + s[end+1:]


def run_add_before(s: str, begin: int, text: str) -> Optional[Tuple[str, int]]:
    if not (0 < begin < len(s)):
        return None

    return f"{s[:begin]}{text} {s[begin:]}", begin+len(text)


def run_add_after(s: str, begin: int, text: str) -> Optional[Tuple[str, int]]:
    if not (0 < begin < len(s)):
        return None
    begin = min(s.find(" ", begin), s.find("\n", begin))
    return f"{s[:begin]} {text}{s[begin:]}", begin+1


def run_add_at_begin(s: str, begin: int, text: str) -> Optional[Tuple[str, int]]:
    if not (0 < begin < len(s)):
        return None

    return f"{s[:begin]}{text}{s[begin:]}", begin+len(text)


def run_copy_to_buffer(s: str, begin: int, end: int) -> Optional[str]:
    if end <= begin or begin < 0 or end >= len(s) or begin >= len(s):
        return None

    return f" {s[begin: end]}"


funcs = {
    "run_search_to_word": run_search_to_word,
    "run_forward_word": run_forward_word,
    "run_backward_word": run_backward_word,
    "run_delete_by_text": run_delete_by_text,
    "run_delete_by_pointers": run_delete_by_pointers,
    "run_add_before": run_add_before,
    "run_add_after": run_add_after,
    "run_copy_to_buffer": run_copy_to_buffer,
}
