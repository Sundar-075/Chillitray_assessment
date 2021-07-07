window.onload = function () {
  document.querySelector(".message > a").click(function () {
    document
      .querySelector("form")
      .animate({ height: "toggle", opacity: "toggle" }, "slow");
  });
};
