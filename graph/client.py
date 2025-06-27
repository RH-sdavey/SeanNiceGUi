from msgraph_beta import GraphServiceClient
from azure.identity import InteractiveBrowserCredential, TokenCachePersistenceOptions


class Client:

    def __init__(self) -> None:
        self.credential = InteractiveBrowserCredential(cache_persistence_options=TokenCachePersistenceOptions())
        self.graph = GraphServiceClient(credentials=self.credential)


client = Client()

