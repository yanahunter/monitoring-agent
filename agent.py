import asyncio
import copy
import datetime
from typing import NoReturn, List, Dict, Union

import requests
from rx import interval
from rx.scheduler.eventloop import AsyncIOScheduler

from config_handler import monitoring_mapping, define_stats_to_monitor, get_stats, get_params_from_config
from settings import CONFIG_PATH, COMPUTER_UUID, REPORT_URL, INTERVAL


def add_details_to_stats(
        stats: Dict[str, Union[int, float, List[str]]]
) -> Dict[str, Union[int, float, str, List[str]]]:
    stats_copy: Dict[str, Union[int, float, str, List[str]]] = copy.deepcopy(stats)
    stats_copy.update({'computer_id': COMPUTER_UUID})
    stats_copy.update({'date': str(datetime.datetime.now())})
    return stats_copy


def send_stats(params: List[str]) -> NoReturn:
    stats_to_monitor = define_stats_to_monitor(params, monitoring_mapping)
    stats = get_stats(stats_to_monitor)
    prepared_stats = add_details_to_stats(stats)
    requests.post(REPORT_URL, prepared_stats)


def handle_sending() -> NoReturn:
    params = get_params_from_config(CONFIG_PATH)
    send_stats(params)


async def main(event_loop: asyncio.AbstractEventLoop) -> NoReturn:
    interval(INTERVAL).subscribe(
        on_next=lambda tick: handle_sending(),
        scheduler=AsyncIOScheduler(event_loop)
    )

loop = asyncio.get_event_loop()
loop.create_task(main(loop))
loop.run_forever()
