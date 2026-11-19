from http.server import BaseHTTPRequestHandler,HTTPServer
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]/'exports'
ROOT.mkdir(parents=True,exist_ok=True)
class Handler(BaseHTTPRequestHandler):
 def do_OPTIONS(self):
  self.send_response(204);self.send_header('Access-Control-Allow-Origin','*');self.send_header('Access-Control-Allow-Headers','Content-Type');self.send_header('Access-Control-Allow-Methods','POST, OPTIONS');self.end_headers()
 def do_POST(self):
  try:
   length=int(self.headers.get('Content-Length','0'))
   if not 0<length<30_000_000:raise ValueError('Invalid size')
   raw=self.rfile.read(length);data=json.loads(raw);n=int(data['lab'])
   if n not in {2,3,4,5,8}:raise ValueError('Invalid laboratory')
   (ROOT/f'figma-lab-{n}.json').write_bytes(raw)
   self.send_response(200);self.send_header('Access-Control-Allow-Origin','*');self.end_headers();self.wfile.write(b'Saved');print('Saved Figma export',n,len(raw),flush=True)
  except Exception as e:self.send_response(400);self.send_header('Access-Control-Allow-Origin','*');self.end_headers();self.wfile.write(str(e).encode())
HTTPServer(('127.0.0.1',8092),Handler).serve_forever()
