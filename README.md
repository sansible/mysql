# Mysql

Master: [![Build Status](https://travis-ci.org/sansible/mysql.svg?branch=master)](https://travis-ci.org/sansible/mysql)  
Develop: [![Build Status](https://travis-ci.org/sansible/mysql.svg?branch=develop)](https://travis-ci.org/sansible/mysql)

* [ansible.cfg](#ansible-cfg)
* [Installation and Dependencies](#installation-and-dependencies)
* [Tags](#tags)
* [Examples](#examples)

This roles installs the Mysql Server, the setup is very basic and is really only meant 
local MySQL testing in VMs.




## ansible.cfg

This role is designed to work with merge "hash_behaviour". Make sure your
ansible.cfg contains these settings

```INI
[defaults]
hash_behaviour = merge
```




## Installation and Dependencies

To install run `ansible-galaxy install sansible.mysql` or add this to your
`roles.yml`.

```YAML
- name: sansible.mysql
  version: v1.0
```

and run `ansible-galaxy install -p ./roles -r roles.yml`




## Tags

This role uses one tag: **build** 

* `build` - Installs Mysql and all it's dependencies.
* `configure` - Configures mysql.




## Settings

```YAML
mysql:
  # Root user and pass should be stored using ansible-vault
  root_user: root
  root_password: P4ssword!
  version: 5.5
```




## Examples

To install:

```YAML
- name: Install and configure Mysql Server
  hosts: "somehost"

  roles:
    - role: sansible.mysql
```

Setup Mysql with root user and password:

```YAML
- name: Install and configure Mysql
  hosts: "somehost"

  roles:
    - role: sansible.mysql
      mysql:
        root_user: different_root_user
        root_password: secure_password
```
