from mcstatus import JavaServer

class MCServer:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.server = JavaServer.lookup(f"{host}:{port}")

    def get_status(self):
        try:
            return self.server.status()
        except:
            return None

    def get_status_message(self):
        status = self.get_status()
        if status:
            return f'Kenfeudi Minecraft serveris ir **ONLINE**! :green_circle:\n' \
                   f'Geimeru skaits serverī: **{status.players.online}**\n' \
                   f'Latency: **{round(status.latency, 2)}** ms'
        else:
            return "Kenfeudi Minecraft serveris ir **OFFLINE**! :red_circle:"