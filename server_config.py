import configparser
import ast

config = configparser.ConfigParser()
config.read('server_config.ini')

Server = {}
Server['server'] = config['Server'].get('server')
Server['database'] = config['Server'].get('database')
Server['username'] = config['Server'].get('username')
Server['password'] = config['Server'].get('password')








