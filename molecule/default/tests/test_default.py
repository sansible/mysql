import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('package', [
    ('mysql-server'),
    ('mysql-common'),
])
def test_installed_apt_packages(host, package):
    assert host.package(package).is_installed


@pytest.mark.parametrize('filename', [
    ('/etc/mysql/conf.d/custom.cnf'),
])
def test_config_files(host, filename):
    with host.sudo():
        assert host.file(filename).is_file
