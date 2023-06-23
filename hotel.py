from abc import ABC, abstractmethod
import logging

from exception import CustomException


class Hotel(ABC):
    """Base class for different types of hotels."""

    @abstractmethod
    def get_location(self) -> str:
        """Abstract method for getting the location of the hotel."""
        pass


def logged(exception, mode):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except CustomException as e:
                logger = logging.getLogger(__name__)
                if mode == "console":
                    handler = logging.StreamHandler()
                elif mode == "file":
                    logging.basicConfig(filename="log.txt", filemode='a')
                    handler = logging.FileHandler(filename='log.txt')
                else:
                    raise CustomException()

                logger.addHandler(handler)
                logger.setLevel(logging.ERROR)
                logger.exception(e)  # Log the exception
                logger.removeHandler(handler)  # Remove the handler after logging

        return wrapper

    return decorator






