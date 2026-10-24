const A=require('astronomy-engine');
function mod(x){return ((x%360)+360)%360}
function poc(d){const jd=d.getTime()/86400000+2440587.5;const T=(jd-2451545)/36525;return{Sun:mod(280.46646+36000.76983*T),Moon:mod(218.3165+481267.8813*T),Mercury:mod(252.2509+149472.6746*T),Venus:mod(181.9798+58517.8156*T),Mars:mod(355.4330+19140.2993*T),Jupiter:mod(34.3515+3034.7102*T),Saturn:mod(50.0774+1222.1138*T)}}
const S=['Ari','Tau','Gem','Can','Leo','Vir','Lib','Sco','Sag','Cap','Aqu','Pis'];
for(const iso of ['1977-01-13T12:00:00Z','2026-10-11T16:00:00Z','1969-07-20T20:17:00Z']){
 const d=new Date(iso);const p=poc(d);console.log('\n'+iso);
 for(const b of Object.keys(p)){const v=A.GeoVector(A.Body[b],d,true);const e=A.Ecliptic(v).elon;
  let diff=mod(p[b]-e);if(diff>180)diff-=360;
  console.log(b.padEnd(8),'POC',S[Math.floor(p[b]/30)],p[b].toFixed(1).padStart(6),' real',S[Math.floor(e/30)],e.toFixed(1).padStart(6),' err',diff.toFixed(1))}}
