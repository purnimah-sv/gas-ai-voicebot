async function ask(){
  let q = document.getElementById("q").value

  let res = await fetch("http://localhost:8000/ask",{
    method:"POST",
    body:q
  })

  let t = await res.text()
  document.getElementById("r").innerText = t
}
