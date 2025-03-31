import sys

def log_colorato(messaggio):
    GIALLO_SU_NERO = "\033[43m\033[30m"
    RESET = "\033[0m"

    sys.stdout.write(f"{GIALLO_SU_NERO}{messaggio}{RESET}")
    sys.stdout.flush()