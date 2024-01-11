from aiosmtpd.smtp import SMTP
from aiosmtpd.controller import Controller
import asyncio

class CustomSMTPHandler:
    async def handle_DATA(self, server, session, envelope):
        print('Receiving message from:', session.peer)
        print('Message addressed from:', envelope.mail_from)
        print('Message addressed to  :', envelope.rcpt_tos)
        print('Message length        :', len(envelope.content))
        return '250 Message accepted for delivery'

handler = CustomSMTPHandler()
controller = Controller(handler, hostname='localhost', port=25)

controller.start()
try:
    asyncio.get_event_loop().run_forever()
except KeyboardInterrupt:
    pass
finally:
    controller.stop()