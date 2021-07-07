window.onload = function () {
  document.getElementById("clickMe").onclick = function () {
    fetch("http://127.0.0.1:8000/hierarchy/get_val")
      .then((response) => response.json())
      .then((data) => {
        setData(data);
      });
  };
};

function setData(data) {
  console.log(data);
}
