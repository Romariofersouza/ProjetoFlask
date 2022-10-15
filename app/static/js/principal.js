function clique() {
    window.alert("voce clicou no botão!");
}
function incluirCurso() {
    var url_atual = window.location.href;
    var url_incluir = url_atual.replace("cursos", "incluir_curso");
    window.location.href = url_incluir;
   }

   function editarCurso(id) {
    var url_atual = window.location.href;
    var url_editar = url_atual.replace("cursos", id + "/editar_curso");
    window.location.href = url_editar;
   }
   function excluirCurso(id) {
    if (confirm("Deseja realmente excluir este curso?") == true) {
        var url_atual = window.location.href;
        var url_excluir = url_atual.replace("cursos", id + "/excluir_curso");
        window.location.href = url_excluir;
    
   }
}
function cadastrarDisciplinas(idCurso) {
    var url_atual = window.location.href;
    var url_disciplinas = url_atual.replace("cursos",
                                            idCurso + "/cadastrar_disciplinas");
     window.location.href = url_disciplinas;
}

function incluirDisciplina() {
    var url_atual = window.location.href;
    var url_incluir = url_atual.replace("cadastrar_disciplinas",
                                        "incluir_disciplina");
     window.location.href = url_incluir;
}
function editarDisciplina(idDisciplina) {
    var url_atual = window.location.href;
    var url_editar = url_atual.replace("cadastrar_disciplinas",
                                        idDisciplina + "/editar_disciplina");
    window.location.href = url_editar;
}
function excluirDisciplina(idDisciplina) {
    if (confirm("Deseja realmente excluir esta disciplina?") == true) {
        var url_atual = window.location.href;
        var url_excluir = url_atual.replace("cadastrar_disciplinas",
                                            idDisciplina + "/excluir_disciplina");
        window.location.href = url_excluir;
    }
}    





   
   


   

   