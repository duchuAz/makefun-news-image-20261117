import json, math, html
from pathlib import Path
# 31 stories
S=[
(1,"Crimean Bridge partly collapses","EUROPE · WAR","BBC NEWS",45.3,34.4,"Ukraine says its missile-and-drone attack took weeks to plan; Zelensky hails an “unprecedented” strike on the bridge to occupied Crimea."),
(2,"Kuwait intercepts “hostile” drones","GULF · SECURITY","AL JAZEERA",29.3,48.0,"Kuwait’s air defences repelled “hostile” drones as Iran and the US traded attacks across the Gulf; Bahrain issued alerts."),
(3,"Knesset elects Kahana speaker","ISRAEL · POLITICS","AL JAZEERA",31.78,35.22,"Matan Kahana, an ally of Gadi Eisenkot, takes the speaker’s chair with Arab-bloc backing."),
(4,"Settlers kill Palestinian woman, 72","WEST BANK · CONFLICT","BBC NEWS",31.9,35.3,"Israeli settlers shot dead a 72-year-old Palestinian woman near Jericho, the health ministry says."),
(5,"Nvidia partner investigated over exports","US · TECH","BBC NEWS",37.35,-121.95,"US authorities are investigating Nvidia partner Megaspeed over chip exports; Jensen Huang will testify to Congress."),
(6,"US loses measles elimination status","US · HEALTH","BBC NEWS",39.0,-98.0,"The US has lost its measles elimination status after 26 years amid record case numbers."),
(7,"Russian military plane crash kills 19","RUSSIA · DISASTER","BBC NEWS",55.0,86.0,"A Russian military plane crashed in Siberia, killing all 19 people on board."),
(8,"Trump in Asia for APEC talks","ASIA · DIPLOMACY","BBC NEWS",22.5,114.0,"Trump arrives in Shenzhen for APEC talks with Xi and Putin as Washington presses new chip restrictions."),
(9,"UK sanctions Israeli settlement firms","UK · ISRAEL","BBC NEWS",51.5,-0.12,"Britain sanctioned firms over Israeli West Bank settlements, citing the two-state solution."),
]
B=[
(10,"PHILIPPINES","Police ask prosecutors to charge Thomas Markle over child sex abuse material"),
(11,"UK / US","American soldier arrested on suspicion of spying is handed to US military custody"),
(12,"UK","Government backs welfare shake-up to prevent a “lost generation”"),
(13,"UK","Home secretary plans to tackle “perception of two-tier policing”"),
(14,"UK / EU","Burnham to set out options next month for a long-term EU relationship"),
(15,"INDIA","William and Kate celebrate Earthshot Prize winners in Mumbai"),
(16,"UK","Rooney says he considered taking his own life at Manchester United"),
(17,"UK","British Airways plane veers off a Heathrow taxiway"),
(18,"UK","Charles Bronson denied parole for the ninth time"),
(19,"UK","Six in court accused of a high-value Pokemon card theft"),
(20,"UK","Gleneagles Hotel buys Scotland’s “ghost” golf course"),
(21,"EU / RWANDA","Five EU states announce plans for immigration “return hubs” in Rwanda"),
(22,"CARIBBEAN","Nations fear economic impact of shuttering citizenship programme after EU threats"),
(23,"BRAZIL","Isolated Awá tribe emerges amid alarm over threats to its way of life"),
(24,"HAITI / US","Eight-year-old Haitian boy returns home after release from ICE custody"),
(25,"BRAZIL","European-made pesticides named in 1,605 poisoning reports last year"),
(26,"US / TECH","Jensen Huang to testify before Congress on “potential breach of national security”"),
(27,"US / IRAN","Trump says US taking “very seriously” any Iranian plot against Washington"),
(28,"PHILIPPINES","Hundreds arrested in anti-Trump protests in Manila over Iran war and AI pact"),
(29,"UK / EU","New youth mobility scheme may not fully launch until 2030"),
(30,"NETHERLANDS","Kessler twins explained assisted-dying decision in a final letter"),
(31,"ISRAEL","Anti-Arab hate speech surged on social media during Israel’s election, report finds"),
]
# icons (inline SVG bodies, drawn white/red on colored bands)
ICONS={
1:"""<svg viewBox="0 0 100 100"><rect x="8" y="62" width="84" height="6" fill="#fff"/><rect x="20" y="42" width="6" height="20" fill="#fff"/><rect x="74" y="42" width="6" height="20" fill="#fff"/><path d="M26 62 L40 40 L54 62" stroke="#fff" stroke-width="4" fill="none"/><path d="M54 62 L68 40 L82 62" stroke="#fff" stroke-width="4" fill="none"/><path d="M44 62 l12 -9 l12 9" stroke="#f4c542" stroke-width="4" fill="none"/><rect x="46" y="70" width="3" height="10" fill="#fff"/><rect x="56" y="70" width="3" height="10" fill="#fff"/></svg>""",
2:"""<svg viewBox="0 0 100 100"><rect x="39" y="44" width="22" height="9" rx="3" fill="#fff"/><path d="M39 47 L25 34 M61 47 L75 34 M39 51 L25 64 M61 51 L75 64" stroke="#fff" stroke-width="3"/><circle cx="23" cy="31" r="6" fill="#fff"/><circle cx="77" cy="31" r="6" fill="#fff"/><circle cx="23" cy="67" r="6" fill="#fff"/><circle cx="77" cy="67" r="6" fill="#fff"/><path d="M16 82 q34 -20 68 0" stroke="#f4c542" stroke-width="3" fill="none"/></svg>""",
3:"""<svg viewBox="0 0 100 100"><rect x="22" y="52" width="56" height="28" fill="#fff"/><rect x="28" y="44" width="44" height="8" fill="#fff"/><rect x="34" y="60" width="5" height="16" fill="#8a6a1c"/><rect x="47" y="60" width="5" height="16" fill="#8a6a1c"/><rect x="60" y="60" width="5" height="16" fill="#8a6a1c"/><path d="M50 16 v22 M38 24 h24 M31 32 h38" stroke="#f4c542" stroke-width="4"/><circle cx="50" cy="16" r="3.5" fill="#f4c542"/><circle cx="38" cy="24" r="2.5" fill="#f4c542"/><circle cx="62" cy="24" r="2.5" fill="#f4c542"/><circle cx="31" cy="32" r="2.5" fill="#f4c542"/><circle cx="69" cy="32" r="2.5" fill="#f4c542"/></svg>""",
4:"""<svg viewBox="0 0 100 100"><path d="M20 64 C28 36 52 26 74 32 C68 39 66 45 66 51 C78 49 84 55 86 62 C70 59 61 65 53 74 C43 84 28 80 20 64 Z" fill="#fff"/><path d="M32 62 q10 -6 18 -2" stroke="#2e7d4f" stroke-width="3" fill="none"/><circle cx="67" cy="39" r="2.2" fill="#2e7d4f"/><path d="M30 82 q20 -8 40 0" stroke="#f4c542" stroke-width="3" fill="none"/></svg>""",
5:"""<svg viewBox="0 0 100 100"><rect x="28" y="28" width="44" height="44" rx="4" fill="#76b900"/><rect x="38" y="38" width="24" height="24" fill="#1c1c1c"/><g stroke="#76b900" stroke-width="4"><path d="M34 20 v8 M50 20 v8 M66 20 v8 M34 72 v8 M50 72 v8 M66 72 v8 M20 34 h8 M20 50 h8 M20 66 h8 M72 34 h8 M72 50 h8 M72 66 h8"/></g><text x="50" y="55" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#76b900" text-anchor="middle">NV</text></svg>""",
6:"""<svg viewBox="0 0 100 100"><path d="M16 54 L32 42 L46 52 L50 44 L64 54 L82 42" stroke="#fff" stroke-width="8" fill="none" stroke-linecap="round" stroke-linejoin="round"/><path d="M28 62 q14 12 28 0" stroke="#f4c542" stroke-width="4" fill="none" stroke-linecap="round"/><path d="M20 74 h60" stroke="#fff" stroke-width="4"/></svg>""",
7:"""<svg viewBox="0 0 100 100"><path d="M50 14 C56 14 58 22 56 32 L80 48 L76 57 L55 49 L53 68 L62 77 L59 83 L50 79 L41 83 L38 77 L47 68 L45 49 L24 57 L20 48 L44 32 C42 22 44 14 50 14 Z" fill="#fff"/><path d="M50 60 v14" stroke="#c8102e" stroke-width="4"/><path d="M44 74 l6 8 l6 -8" stroke="#c8102e" stroke-width="4" fill="none"/></svg>""",
8:"""<svg viewBox="0 0 100 100"><rect x="22" y="48" width="44" height="12" rx="2" fill="#fff" transform="rotate(-30 44 54)"/><rect x="56" y="26" width="10" height="10" fill="#fff" transform="rotate(-30 61 31)"/><rect x="30" y="56" width="4" height="16" fill="#fff" transform="rotate(-30 32 64)"/><circle cx="68" cy="66" r="18" fill="none" stroke="#f4c542" stroke-width="4"/><circle cx="62" cy="60" r="3" fill="#f4c542"/><circle cx="74" cy="60" r="3" fill="#f4c542"/><circle cx="68" cy="72" r="3" fill="#f4c542"/><path d="M50 42 l6 -8" stroke="#f4c542" stroke-width="3"/></svg>""",
9:"""<svg viewBox="0 0 100 100"><rect x="18" y="28" width="64" height="44" fill="#fff"/><path d="M18 28 L82 72 M82 28 L18 72" stroke="#c8102e" stroke-width="7"/><path d="M50 28 v44 M18 50 h64" stroke="#c8102e" stroke-width="9"/><rect x="18" y="28" width="64" height="44" fill="none" stroke="#0b2a4a" stroke-width="4"/><circle cx="50" cy="50" r="7" fill="#fff" stroke="#c8102e" stroke-width="3"/></svg>""",
}

COLORS={1:'#8a1c1c',2:'#0b3d6b',3:'#8a6a1c',4:'#8a1c1c',5:'#1c1c1c',6:'#1c3d6b',7:'#1c6b6b',8:'#0b2a4a',9:'#2e7d4f'}
# map paths
world=json.load(open(Path(__file__).with_name('world.geojson')))
W,H=330,262; lon0,lon1=-180,180; lat0,lat1=-60,85
def xy(lon,lat):
    return ((lon-lon0)/(lon1-lon0)*W, (lat1-lat)/(lat1-lat0)*H)
def ring(coords):
    pts=[]
    for lon,lat in coords:
        x,y=xy(lon,lat); pts.append(f"{x:.1f},{y:.1f}")
    return 'M'+'L'.join(pts)+'Z'
paths=[]
for f in world['features']:
    g=f['geometry']; typ=g['type']; coords=g['coordinates']
    polys=[coords] if typ=='Polygon' else coords
    for poly in polys:
        paths.append(ring(poly[0]))
map_svg=''.join(f'<path d="{p}"/>' for p in paths)
# dots 1-9 with jitter
jitter={1:(0,0),2:(2,2),3:(-3,3),4:(0,0),5:(0,0),6:(3,-3),7:(0,0),8:(0,0),9:(-2,-2)}
dots=[]
for n,title,tag,src,lat,lon,deck in S:
    x,y=xy(lon,lat); dx,dy=jitter.get(n,(0,0))
    dots.append(f'<g><circle cx="{x+dx:.1f}" cy="{y+dy:.1f}" r="8"/><text x="{x+dx:.1f}" y="{y+dy+3:.1f}">{n}</text></g>')
map_dots=''.join(dots)
# cards
cards=[]
for n,title,tag,src,lat,lon,deck in S:
    cards.append(f'''<article class="card"><div class="band" style="background:{COLORS[n]}"><div class="num">{n}</div>{ICONS[n]}</div><div class="cbody"><div class="tag">{tag}</div><h2>{title}</h2><p>{deck}</p><div class="src">{src}</div></div></article>''')
# briefs
briefs=[]
for n,country,title in B:
    briefs.append(f'<div class="brief"><div class="bnum">{n}</div><div class="btext"><b>{country}</b> — {title}</div></div>')
html_doc=f'''<!doctype html><html><head><meta charset="utf-8"><style>
*{{box-sizing:border-box}}html,body{{margin:0;padding:0;width:1024px;height:1024px;overflow:hidden;background:#efe9db;color:#141414;font-family:"Liberation Sans",Arial,sans-serif}}
.header{{position:absolute;left:0;top:0;width:1024px;height:155px;background:#0b2a4a;color:#fff;padding:14px 22px 0}}
.kicker{{font-family:"Liberation Mono",monospace;font-size:12px;letter-spacing:1.6px;color:#e8c766;display:flex;justify-content:space-between}}
.date{{font-family:"Liberation Serif",Georgia,serif;font-size:54px;line-height:1;font-weight:700;letter-spacing:-1.4px;margin-top:8px;white-space:nowrap}}
.sub{{font-size:12.5px;margin-top:5px;color:#e8e1d2}}
.gold{{position:absolute;left:22px;right:22px;top:150px;height:5px;background:#c9a227}}
.cards{{position:absolute;left:22px;right:22px;top:163px;display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:repeat(3,170px);gap:8px}}
.card{{background:#faf6ea;border:1px solid #d8d0be;overflow:hidden;display:flex;flex-direction:column}}
.band{{height:78px;position:relative;display:flex;align-items:center;justify-content:center;flex:none}}
.band svg{{width:64px;height:64px}}
.num{{position:absolute;left:7px;top:7px;width:21px;height:21px;border-radius:50%;background:#c8102e;color:#fff;font-family:"Liberation Mono",monospace;font-size:11px;font-weight:bold;display:flex;align-items:center;justify-content:center}}
.cbody{{padding:5px 8px 4px;display:flex;flex-direction:column;min-height:0}}
.tag{{font-family:"Liberation Mono",monospace;font-size:7.4px;letter-spacing:.5px;color:#c8102e;font-weight:bold;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;flex:none}}
.card h2{{font-family:"Liberation Serif",Georgia,serif;font-size:17.2px;line-height:1.02;margin:3px 0 3px;font-weight:700;letter-spacing:-.2px;flex:none}}
.card p{{font-size:8.9px;line-height:1.16;margin:0 0 3px;color:#222;flex:1 1 auto;min-height:0;overflow:hidden}}
.card .src{{font-family:"Liberation Mono",monospace;font-size:6.9px;letter-spacing:.3px;color:#555;flex:none;margin-top:auto}}
.bottom{{position:absolute;left:22px;right:22px;top:730px;height:258px}}
.mapbox{{position:absolute;left:0;top:0;width:330px;height:258px;background:#f7f3e8;border:1px solid #d8d0be}}
.mapbox .mtitle{{position:absolute;left:8px;top:6px;font-family:"Liberation Mono",monospace;font-size:9.5px;letter-spacing:1px;color:#0b2a4a;font-weight:bold}}
.mapbox svg{{position:absolute;left:0;top:20px;width:330px;height:240px}}
.mapbox path{{fill:#cfd8d2;stroke:#8b9aa8;stroke-width:.55}}
.mapbox circle{{fill:#c8102e;stroke:#fff;stroke-width:1.4}}
.mapbox text{{fill:#fff;font-family:"Liberation Mono",monospace;font-size:8.2px;font-weight:bold;text-anchor:middle}}
.mapbox .cap{{position:absolute;left:8px;bottom:5px;font-family:"Liberation Mono",monospace;font-size:7.2px;color:#555;letter-spacing:.3px}}
.also{{position:absolute;left:344px;top:0;width:636px;height:258px}}
.also .atitle{{font-family:"Liberation Mono",monospace;font-size:10px;letter-spacing:1.4px;color:#0b2a4a;font-weight:bold;border-bottom:2px solid #0b2a4a;padding-bottom:3px}}
.blist{{column-count:2;column-gap:14px;margin-top:4px}}
.brief{{break-inside:avoid;display:flex;gap:5px;padding:2px 0 2px;border-bottom:1px dotted #c9c1ae;font-size:8.25px;line-height:1.1}}
.bnum{{font-family:"Liberation Mono",monospace;font-size:7.2px;color:#c8102e;font-weight:bold;width:13px;flex:none;padding-top:1px}}
.btext{{flex:1}} .btext b{{color:#0b2a4a}}
.footer{{position:absolute;left:22px;right:22px;bottom:6px;height:16px;border-top:1.5px solid #141414;padding-top:3px;font-family:"Liberation Mono",monospace;font-size:7.6px;letter-spacing:.25px;color:#333;display:flex;justify-content:space-between}}
</style></head><body>
<div class="header"><div class="kicker"><span>THE WORLD TODAY</span><span>31 STORIES · SIX CONTINENTS · ONE PAGE</span></div><div class="date">Tuesday 17 November 2026</div><div class="sub">A day of war, diplomacy, disaster and discovery — reported across the world.</div></div>
<div class="gold"></div>
<div class="cards">{''.join(cards)}</div>
<div class="bottom"><div class="mapbox"><div class="mtitle">WHERE IT HAPPENED</div><svg viewBox="0 0 330 240">{map_svg}{map_dots}</svg><div class="cap">NUMBERED DOTS MARK STORIES 1–9</div></div><div class="also"><div class="atitle">ALSO ON TUESDAY 17 NOVEMBER — 22 MORE STORIES</div><div class="blist">{''.join(briefs)}</div></div></div>
<div class="footer"><span>SOURCES: BBC NEWS · AL JAZEERA · THE GUARDIAN · ORIGINAL VECTOR ILLUSTRATIONS</span><span>17 NOV 2026 · GLOBAL EDITION</span></div>
</body></html>'''
Path('entry.html').write_text(html_doc)
print('html',len(html_doc),'cards',len(cards),'briefs',len(briefs))
