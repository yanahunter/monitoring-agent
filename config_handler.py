from enum import Enum
from typing import List, Dict, Union, Callable

import configparser

from monitor import get_cpu_percent, get_free_ram, get_free_disk_space, get_processes_count, get_users_list


class MonitoringParams(Enum):
    cpu_percent = 'cpu_percent'
    free_ram = 'free_ram'
    free_disk_space = 'free_disk_space'
    processes_count = 'processes_count'
    users_list = 'users_list'


MonitoringMapping = Dict[MonitoringParams, Callable[[None], Union[int, float, List[str]]]]

monitoring_mapping: MonitoringMapping = {
    MonitoringParams.cpu_percent: get_cpu_percent,
    MonitoringParams.free_ram: get_free_ram,
    MonitoringParams.free_disk_space: get_free_disk_space,
    MonitoringParams.processes_count: get_processes_count,
    MonitoringParams.users_list: get_users_list,
}


def get_params_from_config(path: str) -> List[str]:
    config = configparser.ConfigParser()
    config.read(path)
    raw_params = config['config']['Params']
    return raw_params.split(', ')


def define_stats_to_monitor(config: List[str], mapping: MonitoringMapping) -> MonitoringMapping:
    return {param: mapping[MonitoringParams[param]] for param in config}


def get_stats(stats_to_monitor: MonitoringMapping) -> Dict[str, Union[int, float, List[str]]]:
    return {param: stats_to_monitor[param]() for param in stats_to_monitor}

