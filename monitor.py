from typing import List

import psutil


def get_cpu_percent() -> float:
    return psutil.cpu_percent(interval=1)


def get_free_ram() -> int:
    return psutil.virtual_memory().free


def get_free_disk_space() -> int:
    return psutil.disk_usage('/').free


def get_processes_count() -> int:
    return len(psutil.pids())


def get_users_list() -> List[str]:
    return [user_data.name for user_data in psutil.users()]
