from cqlengine import connection
from feedly import settings


def setup_connection():
    connection.setup(
        settings.FEEDLY_CASSANDRA_HOSTS,
        max_connections=settings.FEEDLY_CASSANDRA_CONNECTION_POOL_SIZE,
        consistency=settings.FEEDLY_CASSANDRA_CONSITENCY_LEVEL,
        default_keyspace=settings.FEEDLY_DEFAULT_KEYSPACE
    )
