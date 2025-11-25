import hashlib
import logging
from pathlib import Path


# def get_file_hash(file_path: Path) -> str:
#     sha256 = hashlib.sha256()
#     try:
#         with open(file_path, "rb") as f:
#             for chunk in iter(lambda: f.read(4096), b""):
#                 sha256.update(chunk)
#     except FileNotFoundError:
#         logging.error(f"File {file_path} not found")
#         return ""
#     except Exception as e:
#         logging.error(f"Error reading file {file_path}: {e}")
#         return ""
#     return sha256.hexdigest()

def get_bytes_hash(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()