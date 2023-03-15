#!/usr/bin/env python
# Copyright (c) 2016 Orange and others.
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0

# pylint: disable=broad-except
# pylint: disable=consider-using-with
# pylint: disable=unspecified-encoding

"""Class to cleanup Openstack resources"""
import logging
import pathlib
import time
import os
import openstack
import yaml
import pkg_resources
from keystoneauth1 import exceptions as _exc
from xtesting.core import testcase


class ResourceDeletion(testcase.TestCase):
    """Class to cleanup Openstack resources"""
    __logger = logging.getLogger('xtesting.ci.run_tests')
    current_dir = pathlib.Path(__file__).parent
    current_dir = str(current_dir)
    instance_conf_yaml = pkg_resources.resource_filename(
        'k8s_resiliency_validator',
        'onboard_files/conf/instance_info.yaml')
    instance_data = yaml.safe_load(open(instance_conf_yaml, 'r'))
    clouds_data = yaml.safe_load(open('/etc/openstack/clouds.yml', 'r'))
    cloud_key = clouds_data['clouds']
    for key, value in cloud_key.items():
        cloud_name = key

    # pylint: disable=W1505

    def create_connection(self):
        """ Creating Connection to Openstack  """
        try:
            self.__logger.info("Connection Started ")
            conn = openstack.connect(cloud=self.cloud_name)
            if conn.auth_token:
                self.__logger.info("Authentication Successful")
        except _exc.Unauthorized as __e:
            self.__logger.error(__e)
            self.__logger.error("Auth Failed")
        except Exception as __e:
            self.__logger.error(__e)
            self.__logger.error("Connection Failed")
        return conn

    def _get_servers(self, conn):
        """ List the available servers/instances """
        servers = []
        for server in conn.compute.servers():
            if server.name.startswith(self.instance_data['instance_name']):
                servers.append(server)
        return servers

    def delete_servers(self, conn):
        """ Delete the servers/instances """
        server = conn.compute.find_server(self.instance_data['instance_name'])
        if server and server.name == self.instance_data['instance_name']:
            self.__logger.info("Deleting the server")
            for server in self._get_servers(conn):
                conn.compute.delete_server(
                        server, ignore_missing=True, force=False)
        else:
            self.__logger.warn("Instance does not exist")

    def delete_network(self, conn):
        """ Delete the various network elements """
        router = conn.network.find_router(self.instance_data['router_name'])
        network = conn.network.find_network(self.instance_data['network_name'])
        subnet = conn.network.find_subnet(self.instance_data['subnet_name'])
        if router and subnet:
            port = conn.network.ports()
        else:
            port = None
        if port:
            conn.network.remove_interface_from_router(router, subnet.id)
        if router:
            self.__logger.info("Deleting the router")
            conn.network.delete_router(router)
        else:
            self.__logger.warn("Router does not exist")
        if network:
            self.__logger.info("Deleting the network")
            conn.network.delete_network(network)
        else:
            self.__logger.warn("Network does not exist")

    def delete_security_group(self, conn):
        """ Delete the security group"""
        sec_group = conn.network.find_security_group(
                self.instance_data['sec_grp_name'])
        if sec_group:
            self.__logger.info("Deleting the security group")
            conn.network.delete_security_group(sec_group.id)
        else:
            self.__logger.warn("Security group does not exist")

    def delete_keypair(self, conn):
        """ Delete the key pair """
        keypair = conn.compute.find_keypair(self.instance_data['keyname'])
        if keypair:
            conn.compute.delete_keypair(self.instance_data['keyname'])
            try:
                os.remove(self.instance_data['private_keypath'])
            except OSError as __e:
                self.__logger.error("Error: Deleting key")

    def delete_image(self, conn):
        """ Delete the image """
        image_to_delete = conn.image.find_image(
                  self.instance_data['image_name'])
        if image_to_delete:
            self.__logger.info("Deleting the image")
            conn.image.delete_image(image_to_delete, ignore_missing=False)
        else:
            self.__logger.warn("Image does not exist")

    def delete_flavor(self, conn):
        """ Delete the flavor """
        flavour_to_delete = conn.compute.find_flavor(
                self.instance_data['flavor_name'])
        if flavour_to_delete:
            self.__logger.info("Deleting the flavor")
            conn.compute.delete_flavor(flavour_to_delete)
        else:
            self.__logger.warn("Flavor does not exist")

    def instance_cleanup(self):
        """Instance deletion with all all the resources """
        conn = self.create_connection()
        self.delete_servers(conn)
        time.sleep(15)
        self.delete_network(conn)
        self.delete_security_group(conn)
        self.delete_keypair(conn)
        self.delete_image(conn)
        self.delete_flavor(conn)

    def run(self, **kwargs):
        """Xtesting Run"""
        self.start_time = time.time()
        try:
            self.instance_cleanup()
            self.result = 100
        except Exception as __e:
            self.__logger.error(__e)
            self.result = 0
        self.stop_time = time.time()
