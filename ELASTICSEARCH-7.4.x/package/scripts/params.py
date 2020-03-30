# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
Elasticsearch Params configurations
"""

from resource_management.libraries.functions.version import format_hdp_stack_version, compare_versions
from resource_management import *
import status_params
import os

config = Script.get_config()

hostname = config['hostname']


# es env
es_user = config['configurations']['elasticsearch-env']['elasticsearch.user']
es_group = config['configurations']['elasticsearch-env']['elasticsearch.group']

es_master_base_dir = config['configurations']['elasticsearch-env']['elasticsearch.base.dir'] + '/master'
es_slave_base_dir = config['configurations']['elasticsearch-env']['elasticsearch.base.dir'] + '/slave'
es_client_base_dir = config['configurations']['elasticsearch-env']['elasticsearch.base.dir'] + '/client'

es_master_home = es_master_base_dir
es_master_bin = es_master_base_dir + '/bin'
es_slave_home = es_slave_base_dir
es_slave_bin = es_slave_base_dir + '/bin'
es_client_home = es_client_base_dir
es_client_bin = es_client_base_dir + '/bin'

es_master_conf_dir = es_master_base_dir + '/config'
es_slave_conf_dir = es_slave_base_dir + '/config'
es_client_conf_dir = es_client_base_dir + '/config'

es_master_pid_dir = config['configurations']['elasticsearch-env']['elasticsearch.pid.dir'] + '/master'
es_slave_pid_dir = config['configurations']['elasticsearch-env']['elasticsearch.pid.dir'] + '/slave'
es_client_pid_dir = config['configurations']['elasticsearch-env']['elasticsearch.pid.dir'] + '/client'

es_master_pid_file = format("{es_master_pid_dir}/elasticsearch-master.pid")
es_slave_pid_file = format("{es_slave_pid_dir}/elasticsearch-slave.pid")
es_client_pid_file = format("{es_client_pid_dir}/elasticsearch-client.pid")

es_download_url = config['configurations']['elasticsearch-env']['elasticsearch.download.url']

# jvm
heap_size = config['configurations']['elasticsearch-env']['elasticsearch.heap.size'] + 'g'
jvm_opts = config['configurations']['elasticsearch-env']['jvm.opts']

#log4j
log4j2_opts = config['configurations']['elasticsearch-log4j2']['log4j2.opts']

# es config
cluster_name = config['configurations']['elasticsearch-config']['cluster.name']
hostname = config['hostname']
node_attr_rack = config['configurations']['elasticsearch-config']['node.attr.rack']

data_dir = config['configurations']['elasticsearch-config']['path.data']

es_master_log_dir = config['configurations']['elasticsearch-config']['path.logs'] + '/master'
es_slave_log_dir = config['configurations']['elasticsearch-config']['path.logs'] + '/slave'
es_client_log_dir = config['configurations']['elasticsearch-config']['path.logs'] + '/client'

es_master_install_log = es_master_log_dir + '/elasticsearch-install.log'
es_slave_install_log = es_slave_log_dir + '/elasticsearch-install.log'
es_client_install_log = es_client_log_dir + '/elasticsearch-install.log'

# multi data path
master_path_data = ','.join(x + '/master' for x in data_dir.split(','))
slave_path_data = ','.join(x + '/slave' for x in data_dir.split(','))
client_path_data = ','.join(x + '/client' for x in data_dir.split(','))

# single log path
master_path_logs = es_master_log_dir
slave_path_logs = es_slave_log_dir
client_path_logs = es_client_log_dir

bootstrap_memory_lock = str(config['configurations']['elasticsearch-config']['bootstrap.memory.lock'])
if bootstrap_memory_lock is True:
    bootstrap_memory_lock = 'true'
else:
    bootstrap_memory_lock = 'false'

#network_host = config['configurations']['elasticsearch-config']['network.host']
#http_port = config['configurations']['elasticsearch-config']['http_port']

discovery_seed_hosts = str(config['configurations']['elasticsearch-config']['discovery.seed.hosts'])

# Need to parse the comma separated hostnames to create the proper string format within the configuration file
# Expects the format ["host1","host2"]
master_node_list = discovery_seed_hosts.split(',')
discovery_seed_hosts = '[' +  ','.join('"' + x + '"' for x in master_node_list) + ']'


cluster_initial_master_nodes = str(config['configurations']['elasticsearch-config']['cluster.initial.master.nodes'])

# Need to parse the comma separated hostnames to create the proper string format within the configuration file
# Expects the format ["host1","host2"]
master_initial_node_list = cluster_initial_master_nodes.split(',')
cluster_initial_master_nodes = '[' +  ','.join('"' + x + '"' for x in master_initial_node_list) + ']'

gateway_recover_after_nodes = config['configurations']['elasticsearch-config']['gateway.recover.after.nodes']
node_max_local_storage_nodes = config['configurations']['elasticsearch-config']['node.max.local.storage.nodes']

action_destructive_requires_name = str(config['configurations']['elasticsearch-config']['action.destructive.requires.name'])
if action_destructive_requires_name is True:
    action_destructive_requires_name = 'true'
else:
    action_destructive_requires_name = 'false'




