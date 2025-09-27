// app.js
const output = document.getElementById("output");
document.getElementById("run").onclick = async () => {
  const url = document.getElementById("url").value.trim();
  const kws = document.getElementById("keywords").value.split(",").map(s=>s.trim()).filter(Boolean);
  const pw  = document.getElementById("password").value || null;
  if(!url || kws.length===0){
    output.textContent = "URL とキーワードは必須です。";
    return;
  }
  output.textContent = "⏳ 実行中…";
  try {
    const res = await fetch("/api/scrape", {
      method:"POST",
      headers:{ "Content-Type":"application/json" },
      body: JSON.stringify({ url, keywords:kws, password:pw })
    });
    const json = await res.json();
    if(json.error) {
      output.textContent = "❌ " + json.error;
    } else {
      output.textContent = JSON.stringify(json, null, 2);
    }
  } catch(e){
    output.textContent = "❌ 通信エラー：" + e;
  }
};

// PWA インストール誘導
let deferredPrompt;
window.addEventListener("beforeinstallprompt", e => {
  e.preventDefault();
  deferredPrompt = e;
  const btn = document.createElement("button");
  btn.textContent = "📲 インストール";
  btn.onclick = ()=> {
    deferredPrompt.prompt();
    deferredPrompt.userChoice.then(()=> deferredPrompt = null);
  };
  document.body.insertBefore(btn, output);
});
