FEEDLY_NYDUS_CONFIG = {
    'CONNECTIONS': {
        'redis': {
            'engine': 'nydus.db.backends.redis.Redis',
            'router': 'nydus.db.routers.redis.PrefixPartitionRouter',
            'hosts': {
                0: {'prefix': 'default', 'db': 2, 'host': 'localhost', 'port': 6379},
                12: {'prefix': 'feedly:', 'db': 0, 'host': 'localhost', 'port': 6379},
                13: {'prefix': 'feedly:', 'db': 1, 'host': 'localhost', 'port': 6379},
                14: {'prefix': 'notification:', 'db': 3, 'host': 'localhost', 'port': 6379},
            }
        },
    }
}

FEEDLY_CASSANDRA_HOSTS = ['localhost']

# if True detects the nodes by querying the cassandra seeds
FEEDLY_DISCOVER_CASSANDRA_NODES = True
# timeout before giving up upon requests
FEEDLY_CASSANDRA_TIMEOUT = 0.75
# pycassa connection pool size
FEEDLY_CASSANDRA_CONNECTION_POOL_SIZE = 2

FEEDLY_DEFAULT_KEYSPACE = 'feedly'

try:
    from pycassa.cassandra.ttypes import ConsistencyLevel
except ImportError:
    pass
else:
    FEEDLY_CASSANDRA_WRITE_CONSISTENCY_LEVEL = ConsistencyLevel.ONE
    FEEDLY_CASSANDRA_READ_CONSISTENCY_LEVEL = ConsistencyLevel.ONE

FEEDLY_CASSANDRA_CONSITENCY_LEVEL = 'ONE'
