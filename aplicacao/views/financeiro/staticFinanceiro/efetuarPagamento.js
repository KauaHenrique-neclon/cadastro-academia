var botaoAbrirModal = document.getElementById("buttonAbrirJanela");
var modal = document.getElementById("janelaModalAtualizar");
var botaoFechar = document.getElementsByClassName("fechar-modalFoto")[0];

botaoAbrirModal.onclick = function() {
  modal.classList.add('active');
}

botaoFechar.onclick = function() {
  modal.classList.remove('active');
}

window.onclick = function(event) {
  if (event.target === modal) {
    modal.classList.remove('active');
  }
}