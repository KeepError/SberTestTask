from datetime import datetime, timedelta

import pytest

from src.domain.services import FromTimeGreaterThanToTimeError
from ..dependencies import get_visited_links_service

pytest_plugins = ('pytest_asyncio',)


@pytest.mark.asyncio
async def test_get_visited_domains():
    service = get_visited_links_service()
    now = datetime.now()
    await service.add_visited_urls([
        "https://ya.ru", "https://ya.ru?q=123", "https://test-url.com/test1"
    ])
    await service.add_visited_urls([
        "https://test-url.com/test2"
    ])
    visited_domains = await service.get_visited_domains(now, datetime.now())
    assert sorted(visited_domains) == sorted(["ya.ru", "test-url.com"])


@pytest.mark.asyncio
async def test_get_visited_domain_in_different_time():
    service = get_visited_links_service()
    start1 = datetime.now()
    await service.add_visited_urls([
        "https://ya.ru", "https://ya.ru?q=123", "https://test-url.com/test1"
    ])
    start2 = datetime.now()
    await service.add_visited_urls([
        "https://test-url.com/test2"
    ])
    now = datetime.now()
    visited_domains1 = await service.get_visited_domains(start1, now)
    visited_domains2 = await service.get_visited_domains(start2, now)
    assert sorted(visited_domains1) == sorted(["ya.ru", "test-url.com"])
    assert sorted(visited_domains2) == sorted(["test-url.com"])


@pytest.mark.asyncio
async def test_get_visited_domains_with_from_time_greater_than_to_time():
    service = get_visited_links_service()
    now = datetime.now()
    with pytest.raises(FromTimeGreaterThanToTimeError):
        await service.get_visited_domains(now, now - timedelta(seconds=1))
