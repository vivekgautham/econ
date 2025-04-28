import asyncio
import os
import random
import tempfile

import aiofiles


async def async_writer(file_paths, lines):
    for path in file_paths:
        async with aiofiles.open(path, mode="w") as f:
            f.write("\n".join(lines))


def sync_writer(file_paths, num_of_lines):
    for path in file_paths:
        with open(path, mode="w") as f:
            f.write("\n".join(lines))


def async_temp_dir_writer(num_of_files, num_of_lines):
    with tempfile.TemporaryDirectory(suffix="_async", delete=True) as tmp_dir:
        asyncio.run(
            async_writer(
                [os.path.join(tmp_dir, f"file{i}") for i in range(num_of_files)],
                [str(random.random()) for i in range(num_of_lines)],
            )
        )


def sync_temp_dir_writer(num_of_files, num_of_lines):
    with tempfile.TemporaryDirectory(suffix="_sync", delete=True) as tmp_dir:
        sync_writer(
            [os.path.join(tmp_dir, f"file{i}") for i in range(num_of_files)],
            [str(random.random()) for i in range(num_of_lines)],
        )
