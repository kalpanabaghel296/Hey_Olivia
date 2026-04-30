const API = "http://127.0.0.1:5000";

let actionCount = 0;

function toast(msg, err=false) {
  const t = document.getElementById("toast");
  t.innerText = msg;
  t.style.background = err ? "#ef4444" : "#22c55e";
  t.style.display = "block";

  setTimeout(() => t.style.display = "none", 2000);
}

function addAction(val="") {
  if (actionCount >= 5) {
    toast("Max 5 actions allowed", true);
    return;
  }

  const input = document.createElement("input");
  input.value = val;
  input.placeholder = "Enter app or URL";

  document.getElementById("actions").appendChild(input);
  actionCount++;
}

function getActions() {
  return [...document.querySelectorAll("#actions input")]
    .map(i => i.value.trim())
    .filter(v => v);
}

async function save() {
  const keyword = document.getElementById("keyword").value.trim();
  const actions = getActions();

  if (!keyword) return toast("Keyword required", true);
  if (actions.length === 0) return toast("Add at least one action", true);

  const res = await fetch(API + "/command", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ keyword, actions })
  });

  if (res.ok) {
    toast("Saved");
    document.getElementById("actions").innerHTML = "";
    actionCount = 0;
    addAction();
    load();
  } else {
    toast("Error saving", true);
  }
}

async function load() {
  const res = await fetch(API + "/commands");
  const data = await res.json();

  const list = document.getElementById("list");
  list.innerHTML = "";

  data.forEach(c => {
    const div = document.createElement("div");
    div.className = "command";

    div.innerHTML = `
      <strong>${c.keyword}</strong>
      <div class="command-actions">${c.actions.join(", ")}</div>
      <div class="command-buttons">
        <button onclick="run('${c.keyword}')">Run</button>
        <button onclick="del('${c.keyword}')">Delete</button>
      </div>
    `;

    list.appendChild(div);
  });
}

async function run(keyword) {
  await fetch(API + "/execute", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ keyword })
  });

  toast("Executed");
}

async function del(keyword) {
  await fetch(API + "/command/" + keyword, {
    method: "DELETE"
  });

  toast("Deleted");
  load();
}

window.onload = () => {
  addAction();
  load();
};