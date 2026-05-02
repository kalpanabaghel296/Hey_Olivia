const API = "http://127.0.0.1:5000";

let count = 0;

function addAction(val="") {
  const input = document.createElement("input");
  input.value = val;
  input.placeholder = "App or URL";
  document.getElementById("actions").appendChild(input);
}

function getActions() {
  return [...document.querySelectorAll("#actions input")]
    .map(i => i.value.trim())
    .filter(v => v);
}

async function save() {
  const keyword = document.getElementById("keyword").value;
  const actions = getActions();

  await fetch(API+"/command",{
    method:"POST",
    headers:{"Content-Type":"application/json"},
    body: JSON.stringify({keyword,actions})
  });

  load();
}

async function load() {
  const res = await fetch(API+"/commands");
  const data = await res.json();

  const div = document.getElementById("list");
  div.innerHTML="";

  data.forEach(c=>{
    div.innerHTML += `
      <div class="command">
        <b>${c.keyword}</b> → ${c.actions.join(", ")}
        <br>
        <button onclick="run('${c.keyword}')">Run</button>
        <button onclick="del('${c.keyword}')">Delete</button>
      </div>
    `;
  });
}

async function run(k){
  await fetch(API+"/execute",{
    method:"POST",
    headers:{"Content-Type":"application/json"},
    body:JSON.stringify({keyword:k})
  });
}

async function del(k){
  await fetch(API+"/command/"+k,{method:"DELETE"});
  load();
}

window.onload = ()=>{
  addAction();
  load();
};