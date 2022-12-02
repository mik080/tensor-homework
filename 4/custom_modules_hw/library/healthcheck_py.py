#!/usr/bin/python
# -*- coding: utf-8 -*-

from ansible.module_utils.basic import AnsibleModule
import requests

DOCUMENTATION = r'''
---
module: healthcheck
author: Pupkin V.
short_description: healthcheck of site
description:
  - healthcheck of site with or without TLS
version_added: 1.0.0
requirements:
  - requests
  - python >= 3.6
options:
  addr:
    description:
      - Address of site we want to check
      - This is a required parameter
    type: str
  tls:
    description:
      - Whether site using certificates or not
      - Default value is 'True'
    type: bool
'''

EXAMPLES = r'''
- name: Check availability of site
  healthcheck:
    addr: mysite.example
  connection: local

- name: Check availability of site without certs
  healthcheck:
    addr: mysite.example
    tls: false
  connection: local
'''

RETURN = r'''
msg:
  description: Errors if occured
  returned: always
  type: str
  sample: ""
site_status:
  description: State status
  returned: always
  type: str
  sample: Available
rc:
  description: Return code
  returned: always
  type: int
  sample: 200
'''
def check_status(addr,tls):
    if tls==False:
      get_rc=requests.get("http://"+addr).status_code
    else:
      get_rc=requests.get("https://"+addr, verify=False).status_code
    
    return get_rc

def main():
    # Аргументы для модуля
    arguments = dict(
        addr=dict(required=True, type='str'),
        tls=dict(type='bool', default="True")
    )
    # Создаем объект - модуль
    module = AnsibleModule(
        argument_spec=arguments,
        supports_check_mode=False
    )
    # Получаем аргументы
    addr = module.params["addr"]
    tls = module.params["tls"]
    message="Failed"
    try:
      rc_code=check_status(addr,tls)
    except requests.exceptions.ConnectionError as e:
      message = "Can`t connect to host"
      rc_code = 1

    # Если задача успешно завершилась
    if rc_code==200:
        module.exit_json(changed=False,
                         failed = False,
                         site_status='Avaible',
                         rc=rc_code,
                         msg="Avaible")
        
    # Если задача завершилась не успешно
    else:
        module.fail_json(changed=False,
                         failed = True,
                         site_status='Error',
                         rc=rc_code,
                         msg=message)
        

if __name__ == "__main__":
    main()