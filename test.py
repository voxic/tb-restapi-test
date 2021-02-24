import logging
import json
# Importing models and REST client class from Community Edition version
from tb_rest_client.rest_client_ce import *
# Importing the API exception
from tb_rest_client.rest import ApiException


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(module)s - %(lineno)d - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

# ThingsBoard REST API URL
url = "https://demo.thingsboard.io"
# Default Tenant Administrator credentials
username = "mailitb"
password = "password"


# Creating the REST client object with context manager to get auto token refresh
with RestClientCE(base_url=url) as rest_client:
    try:
        # Auth with credentials
        rest_client.login(username=username, password=password)

        device = rest_client.get_tenant_device("Thermometer 1")
        print(device)
        print(rest_client.get_timeseries_keys(device.id))
        
        print(rest_client.save_entity_telemetry(device.id,'DEVICE',{'temp':34}))
        print(rest_client.get_timeseries(device.id,'temp'))


    except ApiException as e:
        logging.exception(e)