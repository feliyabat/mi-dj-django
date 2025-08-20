(function(){
  const KEY='theme';
  const btn=document.createElement('button');
  btn.className='theme-toggle';
  btn.textContent='🌓';
  btn.title='Cambiar tema';
  document.addEventListener('DOMContentLoaded',()=>{
    document.body.appendChild(btn);
    const saved=localStorage.getItem(KEY);
    if(saved){ document.documentElement.setAttribute('data-theme', saved); }
    btn.onclick=()=>{
      const cur=document.documentElement.getAttribute('data-theme')==='dark'?'light':'dark';
      document.documentElement.setAttribute('data-theme', cur);
      localStorage.setItem(KEY, cur);
    };
  });
})();