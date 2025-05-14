import aiofiles
import asyncio
from datetime import datetime
import inspect
import os
from enum import Enum, auto

class LogLevel(Enum):
    INFO = auto()
    ERROR = auto()
    DEBUG = auto()

class AsyncLogger:
    def __init__(self, filename=None):
        self.filename = filename or f"logs/log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        # Создаем директорию для логов, если ее нет
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
    
    async def _write_log(self, level: LogLevel, message: str):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        try:
            caller_frame = inspect.currentframe().f_back.f_back
            caller_info = inspect.getframeinfo(caller_frame)
            caller_name = caller_info.function
        except (AttributeError, ValueError):
            caller_name = "unknown"
        
        log_entry = f"[{timestamp}] [{level.name}] {caller_name}: {message}\n"
        
        try:
            async with aiofiles.open(self.filename, mode='a') as f:
                await f.write(log_entry)
        except Exception as e:
            print(f"Failed to write log: {e}")

    async def info(self, message: str):
        await self._write_log(LogLevel.INFO, message)
    
    async def error(self, message: str):
        await self._write_log(LogLevel.ERROR, message)
    
    async def debug(self, message: str):
        await self._write_log(LogLevel.DEBUG, message)

class AsyncTaskQueue:
    def __init__(self, logger: AsyncLogger):
        self.tasks = asyncio.Queue()
        self.logger = logger
    
    async def add_task(self, task):
        await self.tasks.put(task)
        await self.logger.info(f"Task added: {task}")
    
    async def process_task(self):
        try:
            task = await self.tasks.get()
            await self.logger.info(f"Processing task: {task}. Queue size: {self.tasks.qsize()}")
            # Здесь должна быть обработка задачи
            return task
        finally:
            self.tasks.task_done()
    
    async def finish(self):
        if self.tasks.qsize() > 0:
            await self.logger.error(f"Queue is not empty! {self.tasks.qsize()} tasks remaining.")
        else:
            await self.logger.info("All tasks processed. Queue is empty.")

async def main():
    logger = AsyncLogger()
    queue = AsyncTaskQueue(logger)
    
    for i in range(3):
        await queue.add_task(f"Task_{i}")
    
    while True:
        try:
            task = await asyncio.wait_for(queue.process_task(), timeout=1.0)
            if task is None:
                break
        except asyncio.TimeoutError:
            break
    
    await queue.finish()

if __name__ == "__main__":
    asyncio.run(main())