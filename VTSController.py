import asyncio
import websockets
from json import dumps, loads

from dotenv import load_dotenv, set_key
from os import getenv

class VTSController:
    def __init__(self,port:int=8001, pluginName:str='AI-Waifu-test', pluginDeveloper:str='JarikDem-Bot') -> None:
        self.base_info = {
            'pluginName': pluginName,
            'pluginDeveloper': pluginDeveloper
        }
        self.port = port
        self.vts_token = None
        self.websocket = None

    async def send_request(self, message_type:str='APIStateRequest', data:dict=None) -> dict:
        request = {
            "apiName": "VTubeStudioPublicAPI",
            "apiVersion": "1.0",
            "requestID": "MyIDWithLessThan64Characters",
            "messageType": message_type,
            "data": data
        }
        await self.websocket.send(dumps(request))
        result = await self.websocket.recv()
        return loads(result)

    async def authentication(self) -> None:
        self.update_dotenv()

        if not self.vts_token:
            print("inside if")
            res = await self.send_request(message_type='AuthenticationTokenRequest', data=self.base_info)
            if res['messageType'] == 'APIError':
                raise Exception(f"Error occured:\n\t{res['data']['message']}")
            self.__update_token(res['data']['authenticationToken'])
            return
        
        res = await self.send_request(message_type='AuthenticationRequest', data={**self.base_info, 'authenticationToken': self.vts_token})
        if not res['data']['authenticated']:
            raise ConnectionError(f"Couldn't connect to the API: {res['data']['reason']}")

    async def initialise(self) -> None:
        self.update_dotenv()

        self.websocket = await websockets.connect(f"ws://localhost:{self.port}")

        res = await self.send_request(message_type='APIStateRequest')
        
        if not res['data']['currentSessionAuthenticated']:
            await self.authentication()

    async def inject_params(self, parameters:list) -> None:
        data = {
            "faceFound": False,
            "mode": "set",
            "parameterValues": list(dict(id=param[0], value=param[1]) for param in parameters)
        }

        await self.send_request(message_type='InjectParameterDataRequest', data=data)

    def update_dotenv(self) -> None:
        load_dotenv(override=True)
        self.vts_token = getenv("VTS_TOKEN")

    def __update_token(self,token:str) -> None:
        self.vts_token = token
        set_key('.env', 'VTS_TOKEN', token)
        

    

async def main():
    vtsc = VTSController()
    await vtsc.initialise()
    while True:
        await vtsc.inject_params([['MouthOpen', 0.0]])
        await asyncio.sleep(1)
        await vtsc.inject_params([['MouthOpen', 1.0]])
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())