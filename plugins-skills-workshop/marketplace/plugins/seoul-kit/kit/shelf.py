# -*- coding: utf-8 -*-
"""결과 보관함: out 폴더의 산출물 목록 페이지를 만들고, 브라우저로 볼 수 있게 작은 서버를 띄운다."""
import datetime
import json
import os
import socket
import subprocess
import sys
import time
import urllib.request

KIND = {".html": u"현황판", ".xlsx": u"통계표", ".pptx": u"브리핑"}

PAGE = u"""<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>결과 보관함</title>
<style>
body{margin:0;background:#f4f2ec;color:#15171c;font-family:"Pretendard Variable",Pretendard,"Apple SD Gothic Neo","Malgun Gothic","Noto Sans KR",system-ui,sans-serif}
main{max-width:980px;margin:0 auto;padding:48px 24px 80px}
h1{margin:0 0 6px;font-size:38px;font-weight:800;letter-spacing:-.02em}
p.lead{margin:0 0 30px;color:#6a7180;font-size:16px}
ul{list-style:none;margin:0;padding:0;display:grid;gap:12px}
li a{display:flex;align-items:center;gap:16px;padding:18px 22px;background:#fff;border:1px solid #e2ded3;border-radius:16px;color:inherit;text-decoration:none}
li a:hover{border-color:#15171c}
.kind{flex:none;min-width:64px;text-align:center;padding:4px 10px;border-radius:999px;color:#fff;font-size:13px;font-weight:700}
.k-html{background:#3457d5}.k-xlsx{background:#1e9e5a}.k-pptx{background:#d8643c}
.name{font-size:18px;font-weight:700;word-break:break-all}
.meta{margin-left:auto;flex:none;color:#6a7180;font-size:13.5px;text-align:right}
.new{margin-left:8px;padding:1px 8px;border-radius:999px;background:#15171c;color:#fff;font-size:11.5px;font-weight:700}
.empty{padding:40px;border:1px dashed #c9c4b6;border-radius:16px;color:#6a7180;text-align:center}
</style></head><body><main>
<h1>결과 보관함</h1>
<p class="lead">만든 결과가 여기에 쌓입니다. 현황판은 바로 열리고, 통계표와 브리핑은 누르면 내려받습니다. 이 화면은 스스로 새로 고칩니다.</p>
<div id="list"></div>
</main>
<script type="application/json" id="first">__ITEMS__</script>
<script>
(function(){
  var box=document.getElementById('list'),seen=null;
  function draw(items){
    box.textContent='';
    if(!items.length){var e=document.createElement('div');e.className='empty';e.textContent='아직 만든 결과가 없습니다.';box.appendChild(e);return}
    var ul=document.createElement('ul');
    items.forEach(function(it){
      var li=document.createElement('li'),a=document.createElement('a');a.href=encodeURIComponent(it.file);
      if(it.ext!=='html')a.setAttribute('download',it.file);else a.target='_blank';
      var k=document.createElement('span');k.className='kind k-'+it.ext;k.textContent=it.kind;
      var n=document.createElement('span');n.className='name';n.textContent=it.file;
      if(seen&&seen.indexOf(it.file+it.time)<0){var b=document.createElement('span');b.className='new';b.textContent='새 결과';n.appendChild(b)}
      var m=document.createElement('span');m.className='meta';m.textContent=it.time+' · '+it.size;
      a.appendChild(k);a.appendChild(n);a.appendChild(m);li.appendChild(a);ul.appendChild(li)});
    box.appendChild(ul);
    if(seen===null)seen=items.map(function(it){return it.file+it.time});
  }
  draw(JSON.parse(document.getElementById('first').textContent));
  if(location.protocol.indexOf('http')===0)setInterval(function(){
    fetch('shelf.json?'+Date.now()).then(function(r){return r.json()}).then(draw).catch(function(){});
  },3000);
})();
</script></body></html>
"""


def _size(count):
    return "%.0fKB" % (count / 1024.0) if count < 1024 * 1024 else "%.1fMB" % (count / 1048576.0)


def refresh(out_dir):
    """out_dir 안의 산출물을 최신 순으로 모아 index.html 과 shelf.json 을 다시 쓴다."""
    os.makedirs(out_dir, exist_ok=True)
    items = []
    for name in os.listdir(out_dir):
        ext = os.path.splitext(name)[1].lower()
        if ext not in KIND or name == "index.html":
            continue
        info = os.stat(os.path.join(out_dir, name))
        items.append(
            {
                "file": name,
                "ext": ext[1:],
                "kind": KIND[ext],
                "time": datetime.datetime.fromtimestamp(info.st_mtime).strftime("%H:%M:%S"),
                "size": _size(info.st_size),
                "stamp": info.st_mtime,
            }
        )
    items.sort(key=lambda item: -item["stamp"])
    for item in items:
        del item["stamp"]
    text = json.dumps(items, ensure_ascii=False)
    with open(os.path.join(out_dir, "shelf.json"), "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as handle:
        handle.write(PAGE.replace("__ITEMS__", text.replace("<", "\\u003c")))
    return items


def _listening(port):
    probe = socket.socket()
    probe.settimeout(0.4)
    try:
        return probe.connect_ex(("127.0.0.1", port)) == 0
    finally:
        probe.close()


def _ours(port):
    try:
        with urllib.request.urlopen("http://127.0.0.1:%d/shelf.json" % port, timeout=1.5) as reply:
            return isinstance(json.loads(reply.read().decode("utf-8")), list)
    except Exception:
        return False


def serve(out_dir, port):
    """보관함 서버를 뒤에서 띄운다. 이미 떠 있으면 그대로 둔다. 상태를 설명하는 문장을 돌려준다."""
    refresh(out_dir)
    hint = u"브라우저에서 code-server 주소 끝에 /proxy/%d/ 를 붙여 여세요. 내 컴퓨터에서 직접 실행했다면 http://127.0.0.1:%d/ 입니다." % (port, port)
    if _listening(port):
        if _ours(port):
            return True, u"결과 보관함이 이미 켜져 있습니다. " + hint
        return False, u"%d번 포트를 다른 프로그램이 쓰고 있습니다. kit.py serve --port 8001 처럼 다른 번호로 여세요." % port
    log = open(os.path.join(out_dir, ".shelf.log"), "a")
    subprocess.Popen(
        [sys.executable, "-m", "http.server", str(port), "--bind", "127.0.0.1", "--directory", out_dir],
        stdout=log,
        stderr=log,
        stdin=subprocess.DEVNULL,
        start_new_session=True,
    )
    for _ in range(20):
        time.sleep(0.15)
        if _listening(port):
            return True, u"결과 보관함을 켰습니다. " + hint
    return False, u"결과 보관함을 켜지 못했습니다. %s 를 확인하세요." % os.path.join(out_dir, ".shelf.log")
