import psycopg2

from sshtunnel import SSHTunnelForwarder
server = SSHTunnelForwarder(
    ssh_address_or_host=('172.20.51.11', 22),
    ssh_username='lizf',
    ssh_password='rx154465',
    remote_bind_address=('unix:///var/run/docker.sock')
)

server.start()


server.close()
