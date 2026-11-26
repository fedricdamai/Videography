/* Nika UI kit builders. Deterministic: everything is built synchronously at load. */
(function () {
  const K = (window.NK = {});
  K.rng = (seed) => () => (seed = (seed * 16807) % 2147483647) / 2147483647;
  K.series = (n, seed, up = true, noise = 0.12) => {
    const r = K.rng(seed), out = [];
    for (let i = 0; i < n; i++) { const t = i / (n - 1); let v = 0.1 + 0.8 * Math.pow(t, 1.4) + (r() - 0.5) * noise; out.push(up ? v : 1 - v); }
    return out;
  };
  K.pathD = (vals, w, h, pad = 4) => vals.map((v, i) => `${i ? "L" : "M"}${(pad + (i / (vals.length - 1)) * (w - 2 * pad)).toFixed(1)},${(pad + (1 - v) * (h - 2 * pad)).toFixed(1)}`).join("");
  K.spark = (seed, up = true, w = 120, h = 44) => `<svg class="nk-spark" width="${w}" height="${h}"><path d="${K.pathD(K.series(24, seed, up), w, h)}" fill="none" stroke="${up ? "#22c55e" : "#ef4444"}" stroke-width="2.5" stroke-linejoin="round"/></svg>`;
  K.av = (c) => `<i class="nk-av" style="background:${c}"></i>`;
  K.status = () => `<div class="nk-status">9:41</div>`;

  K.traderCard = (t, id) => `<div class="nk-card" ${id ? `id="${id}"` : ""}>
    <div class="nk-row">${K.av(t.c)}${t.h}<span class="ago">${t.ago || "12M AGO"}</span></div>
    <div class="nk-stats"><div><small>30D ROI</small><em class="${t.up === false ? "nk-r" : "nk-g"}" ${id ? `id="${id}-roi"` : ""}>${t.roi}</em></div>
      <div><small>Win rate</small><em>${t.win}</em></div>${K.spark(t.seed || 7, t.up !== false)}</div>
    <div class="nk-btns"><span class="nk-ghost">View Details</span><span class="nk-blue">Subscribe →</span></div></div>`;

  K.strategies = (traders, o = {}) => `<div class="nk-scr" ${o.id ? `id="${o.id}"` : ""}>${K.status()}
    <div class="nk-h1">Strategies <span class="nk-mini">My strategies ↗</span></div>
    <div class="nk-tabs"><span class="on">Nika</span><span>Global</span></div>
    ${o.search ? `<div class="nk-filters"><span style="flex:1;color:#fff" id="${o.id}-q">⌕ </span></div>` : `<div class="nk-filters"><span>30D ▾</span><span>Highest ROI ▾</span></div>`}
    ${o.just ? `<div class="nk-just" ${o.id ? `id="${o.id}-just"` : ""}><b>● Just traded</b> · 6M AGO<div>${o.just} TSLA <span class="nk-tag s">Short</span></div></div>` : ""}
    <div ${o.id ? `id="${o.id}-list"` : ""}>${traders.map((t, i) => K.traderCard(t, o.id ? `${o.id}-c${i}` : null)).join("")}</div></div>`;

  K.detail = (t, o = {}) => `<div class="nk-scr" id="${o.id}">${K.status()}
    <div class="nk-row" style="font-size:22px;margin:4px 2px 14px">${K.av(t.c)}${t.h}</div>
    <div class="nk-panel"><small style="color:#8c8f9c;font-size:13px">30D PnL</small>
      <div class="nk-big ${t.up === false ? "nk-r" : "nk-g"}" id="${o.id}-pnl">${t.pnl}</div>
      <svg id="${o.id}-chart" width="330" height="150" style="margin-top:6px"><path id="${o.id}-line" d="${K.pathD(K.series(40, t.seed || 11, t.up !== false, 0.1), 330, 150)}" fill="none" stroke="${t.up === false ? "#ef4444" : "#22c55e"}" stroke-width="3" stroke-linejoin="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="0"/></svg>
      <div class="nk-ranges"><span>24H</span><span>7D</span><span class="on">30D</span><span>90D</span><span>All</span></div>
      <div class="nk-kv"><div><small>30D ROI</small><b class="${t.up === false ? "nk-r" : "nk-g"}">${t.roi}</b></div><div style="text-align:right"><small>Win rate</small><b>${t.win}</b></div></div></div>
    <div class="nk-sub">Open positions</div>
    <div id="${o.id}-pos">${(t.pos || []).map((p) => `<div class="nk-pos"><span class="a">${p[0]}<span class="nk-tag ${p[1] === "Long" ? "l" : "s"}" data-side="${p[1]}">${p[2]} ${p[1]}</span></span><span class="v">${p[3]}</span><span class="p ${p[4][0] === "-" ? "nk-r" : "nk-g"}">${p[4]}</span></div>`).join("")}</div></div>`;

  K.sheet = (t, o = {}) => `<div class="nk-sheet" id="${o.id}">
    <h3>${K.av(t.c)}Subscribe to ${t.h}</h3>
    <div class="nk-kv"><div><small>30D ROI</small><b class="${t.up === false ? "nk-r" : "nk-g"}">${t.roi}</b></div><div><small>30D PnL</small><b class="${t.up === false ? "nk-r" : "nk-g"}">${t.pnlShort || t.pnl}</b></div><div style="text-align:right"><small>Win rate</small><b>${t.win}</b></div></div>
    <div class="nk-tog"><i class="knob" id="${o.id}-knob"></i><span>Mirror</span><span>Inverse</span></div>
    <div class="nk-hint" id="${o.id}-hint">Copy this trader's positions in the same direction.</div>
    <div class="nk-alloc">Allocation</div><div class="nk-amt" id="${o.id}-amt">$0</div>
    <div class="nk-quick"><span>MIN</span><span>25%</span><span>50%</span><span>MAX</span></div>
    <div class="nk-keys">${["1","2","3","4","5","6","7","8","9",".","0","⌫"].map((k) => `<span>${k}</span>`).join("")}</div>
    <div class="nk-slide"><div class="fill" id="${o.id}-fill"></div><b>Slide to subscribe</b><i id="${o.id}-thumb">»</i></div></div>`;

  K.success = (title, lines, id) => `<div class="nk-ok" id="${id}"><div class="c">✓</div><h2>${title}</h2><p>${lines}</p></div>`;

  K.portfolio = (cards, o = {}) => `<div class="nk-scr" id="${o.id}">${K.status()}
    <div style="display:flex;justify-content:space-between;align-items:center;margin:6px 2px 4px"><div class="nk-bal">${o.bal || "$927.58"}</div><span class="nk-dep">Deposit</span></div>
    <svg width="364" height="110" style="margin:10px 0 6px"><path d="${K.pathD(K.series(30, 5, true, 0.05), 364, 110)}" fill="none" stroke="#5662ff" stroke-width="2.5"/></svg>
    <div class="nk-tabs"><span>Assets</span><span class="on">Strategies (${cards.length})</span><span>Perps</span><span>Earn</span></div>
    <div class="nk-panel nk-kv"><div><small>Strategies value</small><b>${o.value || "$750.00"}</b></div><div style="text-align:right"><small>Total PnL</small><b class="nk-g" id="${o.id}-total">+$0.00</b></div></div>
    ${cards.map((c, i) => `<div class="nk-panel" id="${o.id}-s${i}"><div class="nk-row">${K.av(c.c)}${c.h}<span class="nk-badge ${c.mode === "Inverse" ? "i" : "m"}">${c.mode}</span></div>
      <div class="nk-kv" style="margin-top:12px"><div><small>Value</small><b>${c.val}</b></div><div style="text-align:right"><small>Total PnL</small><b class="nk-g" id="${o.id}-p${i}">+$0.00</b></div></div></div>`).join("")}</div>`;

  K.toast = (id, title, line, amt) => `<div class="nk-toast" id="${id}"><div class="ic">N</div><div><b>${title}</b><small id="${id}-line">${line}</small></div>${amt ? `<em id="${id}-amt">${amt}</em>` : ""}</div>`;

  K.logo = (size = 120) => `<div class="nk-logo" style="font-size:${size}px"><i style="width:${size * 0.8}px;height:${size * 0.8}px;border-width:${size * 0.16}px"></i>nika</div>`;

  K.scene = (id, o) => `<div class="nk-scene" id="${id}" style="background:${o.bg}">${o.deco || ""}
    ${o.clean ? "" : `<div class="cap">${o.cap}</div><div class="tagline">ANIMATIC · LIVE-ACTION MOOD CARD</div>`}
    ${o.act && !o.clean ? `<div class="act" id="${id}-act">${o.act}</div>` : ""}<div class="subt" id="${id}-sub"></div></div>`;

  // Timeline helpers
  K.money = (v, d = 2) => "$" + v.toLocaleString("en-US", { minimumFractionDigits: d, maximumFractionDigits: d });
  K.count = (tl, sel, from, to, dur, at, fmt) => {
    const o = { v: from }, el = () => document.querySelector(sel);
    tl.to(o, { v: to, duration: dur, ease: "power2.out", onUpdate: () => { el().textContent = fmt(o.v); } }, at);
  };
  K.type = (tl, sel, text, at, step = 0.05) => {
    for (let i = 1; i <= text.length; i++) tl.to(sel, { duration: 0.001, onStart: () => {}, textContent: text.slice(0, i) }, at + i * step);
  };
  K.say = (tl, sel, text, at) => tl.to(sel, { textContent: text, duration: 0.001 }, at);
})();
