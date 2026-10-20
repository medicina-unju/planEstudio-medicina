#!/usr/bin/env python3
import json, sys, datetime
d = json.load(open(sys.argv[1]))
t = open(sys.argv[2], encoding="utf-8").read()
payload = json.dumps({k: d[k] for k in ("ver", "subjects", "corrCambios", "sugerencias", "inconsistencias") if k in d},
                     ensure_ascii=False, separators=(",", ":"))
assert "/*__DATA__*/null" in t
out = t.replace("/*__DATA__*/null", payload)
stamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
assert "window.__BUILD__=" not in out
out = out.replace("<script>\n(function(){", '<script>\nwindow.__BUILD__=%s;\n(function(){' % json.dumps(stamp), 1)
import os
AUTOR = dict(nombre='Fabiola Paz', anio=datetime.datetime.now().year)
out = out.replace('<script>\nwindow.__BUILD__', '<script>\nwindow.__AUTOR__=%s;\nwindow.__BUILD__' % json.dumps(AUTOR, ensure_ascii=False), 1)
if os.path.exists("oficial.json"):
    o = json.load(open("oficial.json")); o = o.get("estado", o)
    out = out.replace("<script>\nwindow.__BUILD__", "<script>\nwindow.__OFICIAL__=%s;\nwindow.__BUILD__" % json.dumps(o, ensure_ascii=False, separators=(",", ":")), 1)
open(sys.argv[3], "w", encoding="utf-8").write(out)
print("ok", len(t) + len(payload))
