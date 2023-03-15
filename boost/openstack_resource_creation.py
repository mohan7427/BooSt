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

"""Class to create Openstack resources"""
import logging
import time
import os
import pathlib
import openstack
import paramiko
import yaml
import pkg_resources
from keystoneauth1 import exceptions as _exc
from k8s_resiliency_validator.onboard_files import resource_deletion
from xtesting.core import testcase


class ResourceCreation(testcase.TestCase):
    """Class to create Openstack resources"""
    __logger = logging.getLogger('xtesting.ci.run_tests')
    current_dir = pathlib.Path(__file__).parent
    current_dir = str(current_dir)
    instance_conf_yaml = pkg_resources.resource_filename(
            'k8s_resiliency_validator',
            'onboard_files/conf/instance_info.yaml')
    host_conf_yaml = pkg_resources.resource_filename(
            'k8s_resiliency_validator',
            'onboard_files/conf/host_info.yaml')
    instance_data = yaml.safe_load(open(instance_conf_yaml, 'r'))
    host_data = yaml.safe_load(open(host_conf_yaml, 'r'))
    tests_launcher_user = host_data['tests-launcher_user']
    tests_launcher_pass = host_data['tests-launcher_pass']
    tests_launcher_port = host_data['tests-launcher_port']
    clouds_data = yaml.safe_load(open('/etc/openstack/clouds.yml', 'r'))
    cloud_key = clouds_data['clouds']
    for key, value in cloud_key.items():
        cloud_name = key
    address = None

    # pylint: disable=logging-format-interpolation
    # pylint: disable=C0209,E1101,W1201,W0612

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
            self.result = 0
        except Exception as __e:
            self.__logger.error(__e)
            self.__logger.error("Connection Failed")
            self.result = 0
        return conn

    def upload_image(self, conn):
        """ Check for image, Upload if doesnt exist """
        self.__logger.info("Image Upload Check")
        image = conn.compute.find_image(self.instance_data['image_name'])
        if image and image.name == self.instance_data['image_name']:
            self.__logger.info("Image Already Exists, Skipping Image Upload")
        else:
            self.__logger.info("Creating a new openstack Image")
            qcow2_name = self.instance_data['qcow2_name']
            try:
                image = conn.create_image(
                        self.instance_data['image_name'],
                        filename='/opt/images/' + qcow2_name,
                        wait=True)
                if image.id:
                    self.__logger.info("Image Creation Successful")
            except Exception as __e:
                self.__logger.error(__e)
                self.__logger.error("Error Creating Image")
                self.result = 0
        return image

    def verify_images_and_status(self, conn):
        "function to validate the image creation"
        time.sleep(10)
        for image in conn.image.images():
            if image.name == self.instance_data['image_name'] and \
                    image.status == "active":
                self.__logger.info("Image Verified")

    def create_flavor(self, conn):
        """ Check for flavor, Create if doesnt exist """
        self.__logger.info("Checking Openstack Flavor")
        flavor = conn.compute.find_flavor(
                self.instance_data['flavor_name'])
        if flavor and flavor.name == self.instance_data['flavor_name']:
            self.__logger.info("Flavor Already Exist,Skipping Flavor Creation")
        else:
            self.__logger.info("Creating New Flavor")
            try:
                flavor = conn.create_flavor(
                        name=self.instance_data['flavor_name'],
                        ram=self.instance_data['ram'],
                        vcpus=self.instance_data['vcpus'],
                        disk=self.instance_data['disks'])
                if flavor.id:
                    self.__logger.info("Flavor Created Successfully")
            except Exception as __e:
                self.__logger.error(__e)
                self.__logger.error("Error Creating Flavor")
        return flavor

    def create_network(self, conn):
        """ Check for network, Create if doesnt exist """
        self.__logger.info("Checking Network")
        network = conn.network.find_network(self.instance_data['network_name'])
        if network and network.name == self.instance_data['network_name']:
            self.__logger.info(
                    "Network Already Exist,Skipping Network Creation")
        else:
            self.__logger.info("Creating New Network")
            try:
                network = conn.network.create_network(
                    name=self.instance_data['network_name'])
                subnet = conn.network.create_subnet(
                        name=self.instance_data['subnet_name'],
                        network_id=network.id,
                        ip_version=self.instance_data['ip_version'],
                        cidr=self.instance_data['cidr'],
                        gateway_ip=self.instance_data['gateway_ip'])
                if network.id:
                    self.__logger.info(
                            "Network %s Subnet %s Created Successfully",
                            network.name, subnet.name)
            except Exception as __e:
                self.__logger.error(__e)
                self.__logger.error("Error Creating Network")
        return network

    def create_router(self, conn):
        """ To create the router """
        self.__logger.info("Checking Router")
        router = conn.network.find_router(self.instance_data['router_name'])
        if router and router.name == self.instance_data['router_name']:
            self.__logger.info("Router Already Exist,Skipping Router Creation")
        else:
            self.__logger.info("Creating the router")
            try:
                network = conn.network.find_network(
                        self.instance_data['ex_nw_name'])
                router = conn.network.create_router(
                        name=self.instance_data['router_name'],
                        external_gateway_info={"network_id": network.id})
            except Exception as __e:
                self.__logger.error(__e)
                self.__logger.error("Error Creating Router")
        return router

    def add_router_interface(self, conn):
        """ To add an interface to the router """
        self.__logger.info("Adding interface to the router")
        router = conn.network.find_router(self.instance_data['router_name'])
        subnet = conn.network.find_subnet(self.instance_data['subnet_name'])
        conn.network.add_interface_to_router(router, subnet.id)

    def create_security_group(self, conn):
        """ To create the security group with rules """
        self.__logger.info("Create_security_group check")
        security_group = conn.network.find_security_group(
                self.instance_data['sec_grp_name'])
        if security_group and \
                security_group.name == self.instance_data['sec_grp_name']:
            self.__logger.info(
                    " Security group Already Exist,Skipping Creation")
        else:
            self.__logger.info("Creating security Group ")
            try:
                security_group = conn.network.create_security_group(
                    name=self.instance_data['sec_grp_name'])
                all_tcp_from_local = {
                    'direction': self.instance_data['tcp_direction'],
                    'remote_ip_prefix': self.instance_data['tcp_ip_prefix'],
                    'protocol': self.instance_data['tcp_protocol'],
                    'port_range_min': self.instance_data['tcp_port_min'],
                    'port_range_max': self.instance_data['tcp_port_max'],
                    'security_group_id': security_group.id,
                    'ethertype': self.instance_data['tcp_ethertype']
                }
                all_icmp_from_local = {
                    'direction': self.instance_data['icmp_direction'],
                    'remote_ip_prefix': self.instance_data['icmp_rmt_ip_px'],
                    'protocol': self.instance_data['icmp_protocol'],
                    'port_range_min': self.instance_data['icmp_port_min'],
                    'port_range_max': self.instance_data['icmp_port_max'],
                    'security_group_id': security_group.id,
                    'ethertype': self.instance_data['icmp_ethertype']
                }
                ssh_from_external = {
                    'direction': self.instance_data['ssh_from_ex_direction'],
                    'remote_ip_prefix': self.instance_data['ssh_ex_rmt_ip_px'],
                    'protocol': self.instance_data['ssh_from_ex_protocol'],
                    'port_range_min': self.instance_data['ssh_ex_port_min'],
                    'port_range_max': self.instance_data['ssh_ex_port_max'],
                    'security_group_id': security_group.id,
                    'ethertype': self.instance_data['ssh_ex_ethertype']
                }
                conn.network.create_security_group_rule(**all_tcp_from_local)
                conn.network.create_security_group_rule(**all_icmp_from_local)
                conn.network.create_security_group_rule(**ssh_from_external)
                if security_group.id:
                    self.__logger.info("Security group created successfully")
            except Exception as __e:
                self.__logger.error(__e)
                self.__logger.error("Error Creating Security Group")
        return security_group

    def create_keypair(self, conn):
        """ To create key pair and store it """
        keypair = conn.compute.find_keypair(self.instance_data['keyname'])
        if not keypair:
            self.__logger.info("Create Key Pair")
            keypair = conn.compute.create_keypair(
                    name=self.instance_data['keyname'])
            with open(self.instance_data['private_keypath'], 'w') as __f:
                __f.write(f"{keypair.private_key}")
            os.chmod(self.instance_data['private_keypath'], 0o400)
        return keypair

    def create_instance(self, conn):
        """ To create the instance with required details """
        self.__logger.info("Checking if the instance already exists")
        server = conn.compute.find_server(self.instance_data['instance_name'])
        if server and server.name == self.instance_data['instance_name']:
            self.__logger.info("instance already exists")
        else:
            self.__logger.info("Creating the Instance")
            image = conn.compute.find_image(self.instance_data['image_name'])
            flavor = conn.compute.find_flavor(
                    self.instance_data['flavor_name'])
            network = conn.network.find_network(
                    self.instance_data['network_name'])
            secgroup = conn.network.find_security_group(
                    self.instance_data['sec_grp_name'])
            data = {
                       "avai_zone": self.instance_data['avail_zone'],
                       "name": self.instance_data['instance_name'],
                       "image_id": image.id,
                       "flavor_id": flavor.id,
                       "config_drive": True,
                       "key_name": self.instance_data['keyname'],
                       "security_groups": [{
                                            "name": secgroup.name
                                          }],
                       "networks": [{
                                       "uuid": network.id
                                   }]
                   }
            try:
                server = conn.compute.create_server(**data)
                server = conn.compute.wait_for_server(server)
                self.__logger.info('Instance created successfully')
            except Exception as __e:
                self.__logger.error(__e)
                self.__logger.error("Error Creating Instance")
        return server

    def add_floating_ip(self, conn):
        """ To add floatingIP to the instance """
        server = self.create_instance(conn)
        self.__logger.info('Attach floating ip to an instance')
        address = conn.available_floating_ip(
                 network=self.instance_data['ex_nw_name'])['floating_ip_address']  # noqa: F401
        if not address:
            try:
                self.__logger.info('Creating a floating ip')
                address = conn.network.create_floating_ip(
                    network=self.instance_data['ex_nw_name'])
            except Exception as __e:
                self.__logger.error(__e)
                self.__logger.error("Error Attaching Floating IP")
        conn.compute.add_floating_ip_to_server(server.id, address)
        self.__logger.info("Floating ip %s is attached successfully "
                           "to server" % (address))
        return address

    def check_vm_ping(self, count, address):
        """Connect to a virtual machine via ssh
        """
        self.__logger.info('Check VM Ping')
        cmd = 'ping -c{} {}'.format(count, address)
        ssh2 = paramiko.SSHClient()
        ssh2.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
        ssh2.connect('m1-tst0001', self.tests_launcher_port,
                     self.tests_launcher_user, self.tests_launcher_pass)
        stdin, stdout, stderr = ssh2.exec_command(cmd, get_pty=True)
        status = stdout.read()
        lines = status.decode('utf-8')
        for line in lines.splitlines():
            self.__logger.info(line)
        exit_status = stdout.channel.recv_exit_status()
        if exit_status == 0:
            self.__logger.info("Able to ping server")
        else:
            raise Exception("Unable to ping server")

    def run(self, **kwargs):

        """ Xtesting Run """
        self.start_time = time.time()
        instance_destroy = resource_deletion.ResourceDeletion()
        try:
            self.__logger.info("Cleanup resources if exists")
            instance_destroy.instance_cleanup()
            conn = self.create_connection()
            self.upload_image(conn)
            self.verify_images_and_status(conn)
            self.create_flavor(conn)
            self.create_network(conn)
            self.create_router(conn)
            self.add_router_interface(conn)
            self.create_security_group(conn)
            self.create_keypair(conn)
            address = self.add_floating_ip(conn)
            #self.check_vm_ping(5, address)
            self.result = 100
        except Exception as __e:
            self.__logger.error(__e)
            #self.__logger.info("Cleaning Up Resources")
            #instance_destroy.instance_cleanup()
            self.result = 0
        self.stop_time = time.time()
