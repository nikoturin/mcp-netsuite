# server.py
import requests
import json
from requests_oauthlib import OAuth1
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

@mcp.tool()
def ns_monthly_report(text: str)  -> json:
    """ Obtener número de transacción"""

    try:
        URL="https://xxxxxx.restlets.api.netsuite.com/app/site/hosting/restlet.nl?script=9999&deploy=1"

        auth = OAuth1(

                    client_key="",
                    client_secret="",
                    resource_owner_key="",
                    resource_owner_secret="",
                    realm="",
                    signature_method="HMAC-SHA256",
        )
        headers = {"Content-Type": "application/json"}
        response = requests.request("GET", URL, auth=auth, headers=headers)
        r_response=json.loads(response.json())
        return str(r_response[0])

    except:
        return "No se logró encontrar la información solicitada"

        #return str

if __name__ == "__main__":
    mcp.run(transport="stdio")
