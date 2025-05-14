import aiofiles
import asyncio
from datetime import datetime
import inspect
from enum import Enum, auto

class LogLevel(Enum): # организуем наш логгер
    INFO = auto()
    ERROR = auto()
    DEBUG = auto()

class AsyncLogger: # основа для логгера
    def init(self, filename=None):
        self.filename = filename or f"logs/log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    
    async def _write_log(self, level: LogLevel, message: str):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        caller_frame = inspect.currentframe().f_back.f_back
        caller_info = inspect.getframeinfo(caller_frame)
        caller_name = caller_info.function
        
        log_entry = f"[{timestamp}] [{level.name}] {caller_name}: {message}\n" # содержимое логгера
        
        async with aiofiles.open(self.filename, mode='a') as f:
            await f.write(log_entry)
    
    async def info(self, message: str): # выводит информацию процесса задачи
        await self._write_log(LogLevel.INFO, message)
    async def error(self, message: str): # выводит ошибку
        await self._write_log(LogLevel.ERROR, message)
    async def debug(self, message: str): # дебаг
        await self._write_log(LogLevel.DEBUG, message)

class AsyncTaskQueue: # Очередь задач
    def init(self, logger: AsyncLogger):
        self.tasks = asyncio.Queue()
        self.logger = logger
    
    async def add_task(self, task):
        await self.tasks.put(task)
        await self.logger.info(f"Task added: {task}")
    
    async def process_task(self):
        if self.tasks.empty():
            await self.logger.error("No tasks to process!")
            return None
        
        task = await self.tasks.get()
        await self.logger.info(f"Processing task: {task}. Queue size: {self.tasks.qsize()}")
        
        self.tasks.task_done()
        return task
    
    async def finish(self):
        if not self.tasks.empty():
            await self.logger.error("Queue is not empty! Tasks remaining.")
        else:
            await self.logger.info("All tasks processed. Queue is empty.")

async def main():
    logger = AsyncLogger()
    queue = AsyncTaskQueue()
    
    for i in range(3):
        await queue.add_task(f"Task_{i}")
    while not queue.tasks.empty():
        await queue.process_task()
    await queue.finish()

if __name__ == "__main__":
    asyncio.run(main())