// Save theme in a cookie
function setTheme(theme) {
  document.body.classList.remove("light-theme", "dark-theme");
  document.body.classList.add(theme + "-theme");
  document.cookie = "theme=" + theme + "; path=/";
}

// Get theme from cookie
function getTheme() {
  const value = "; " + document.cookie;
  const parts = value.split("; theme=");
  if (parts.length === 2) return parts.pop().split(";").shift();
  return null;
}

// Toggle between dark and light
function toggleTheme() {
  if (document.body.classList.contains("dark-theme")) {
    setTheme("light");
  } else {
    setTheme("dark");
  }
}

// On page load, apply saved theme
document.addEventListener("DOMContentLoaded", () => {
  const savedTheme = getTheme();
  if (savedTheme) {
    setTheme(savedTheme);
  } else {
    setTheme("light"); // default
  }
});


let shadow;

function dragit(event) {
    shadow = event.target.closest('tr'); // Get the row
}

function dragover(e) {
    e.preventDefault(); // Important
    let tbody = e.target.closest('tbody');
    let targetRow = e.target.closest('tr');
    if (!targetRow || targetRow === shadow) return;

    let children = Array.from(tbody.children);
    if(children.indexOf(targetRow) > children.indexOf(shadow))
        targetRow.after(shadow);
    else
        targetRow.before(shadow);
}
