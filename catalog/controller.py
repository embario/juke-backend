import abc
import typing


class ResourceStrategy(abc.ABC):
    def __init__(self, path, data):
        self.path = path
        self.data = data

    @abc.abstractmethod
    def route(self) -> typing.List[typing.Any]:
        pass


class ExternalResourceStrategy(ResourceStrategy):
    def route(self) -> typing.List[typing.Any]:




class InternalResourceStrategy(ResourceStrategy):
    pass


def route(path: str, data: dict) -> typing.Any:
    import ipdb; ipdb.set_trace()

    match path:
        case '/api/v1/genres/' | '/api/v1/artists/' | '/api/v1/albums/' | '/api/v1/tracks/':
            response = ExternalResourceStrategy(path, data).route()
        case _:
            raise Exception("Not found")
